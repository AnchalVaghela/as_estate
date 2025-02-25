from odoo import models,fields,api,exceptions
from datetime import timedelta

from odoo.exceptions import UserError

class as_estate_offer(models.Model):
    _name = 'as.estate.offer.model'
    _description = 'Estate Offer Model'
    _order = 'price desc'

    price = fields.Float(string="price", required=True)
    status = fields.Selection([
        ('accepted','Accepted'),
        ('refused','Refused'),
    ],copy=False)

    partner_id = fields.Many2one("res.partner", string="Buyer", required=True)
    property_id = fields.Many2one("as.estate.model", string="Property", ondelete='cascade')
    
    property_type_id = fields.Many2one(
        related='property_id.property_type_id',
        store=True,
        string='Property Type'
    )
    

    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline", store=True)

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            create_date = record.create_date or fields.Date.today()
            record.date_deadline = create_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date:
                record.validity = (record.date_deadline - record.create_date.date()).days

    def action_accept(self):
        for offer in self:
            offer.status = 'accepted'
            offer.property_id.selling_price = offer.price
            offer.property_id.buyer = offer.partner_id
            offer.property_id.state="offerAccepted"

    def action_refuse(self):
        for offer in self:
            offer.status = 'refused'


    _sql_constraints = [
        ('check_price', 'check(price >= 0)','The price must be positive.')
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'property_id' in vals:
                property_id = self.env['as.estate.model'].browse(vals['property_id'])
                
                if property_id.offer_ids:
                    max_offer = max(property_id.offer_ids.mapped('price'))
                    if vals.get('price', 0) <= max_offer:
                        raise exceptions.UserError(f"The offer must be higher than {max_offer}")
                
                property_id.write({'state': 'offerReceived'})

        return super().create(vals_list)


