from odoo import models, fields, api, exceptions
from datetime import timedelta
from odoo.exceptions import UserError,ValidationError

class as_estate(models.Model):
    _name = 'as.estate.model'
    _description = 'Estate Model'
    _order = 'id desc'
    

    property_type_id = fields.Many2one("as.estate.type.model", string="Property Type")
    buyer = fields.Many2one("res.partner")
    seller = fields.Many2one("res.users",string="Seller",default=lambda self: self.env.user)
    seller_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    tag_id = fields.Many2many("as.estate.tag.model")

    offer_ids = fields.One2many("as.estate.offer.model", "property_id", string="Offers")

    best_price = fields.Float(string="Best Offer",compute="_compute_best_price",store=True)
    
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price"),default=0)


    name = fields.Char(string='Title',default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string='Available Date', copy=False, default=lambda self: fields.Datetime.today() + timedelta(days=90))  
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False,default=0.0)
    
    _sql_constraints = [
        ('check_expected_price', 'check(expected_price >= 0)',
         'The expected price must be strictly positive.'),
         ('check_selling_price', 'check(selling_price >= 0)',
         'The selling price must be positive.')
    ]

    bedrooms = fields.Integer(default=2)
    facades = fields.Integer()
    garage = fields.Boolean()
    living_area = fields.Float(string="Living Area")
    total_area = fields.Float(string="Total Area",compute="_compute_total_area", store=True)
    state = fields.Selection(selection=[("new","New"), ("offerReceived","OfferReceived",) ,("offerAccepted","OfferAccepted"), ("Sold","Sold"), ("cancelled" ,"Cancelled" )],default="new")

    # active = fields.Boolean(default=True)
    # last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area



    garden = fields.Boolean(string="Garden")
    garden_area = fields.Float(string="Garden Area")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation")

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    def action_sold(self):
        for record in self:
            if record.state == "cancelled":
                raise UserError("A cancelled property cannot be sold.")
        self.state = 'Sold'
        
    
    def action_cancel(self):
        for record in self:
            if record.state=="Sold":
                raise UserError("A sold property cannot be cancelled.")
        self.state = 'cancelled'

    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price and record.expected_price:  
                minimum_price = record.expected_price * 0.9
                if record.selling_price < minimum_price:
                    raise ValidationError("The selling price must be at least 90% of the expected price!")

    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_or_cancelled(self):
        for record in self:
            if record.state not in ['new', 'cancelled']:
                raise exceptions.UserError("You can't delete a property that is not in 'New' or 'Cancelled' state")
