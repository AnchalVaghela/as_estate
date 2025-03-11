from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = 'as.estate.type.model'
    _description = 'Estate Property Type'
    _order = 'sequence, name'

    name = fields.Char('Name', required=True)
    sequence = fields.Integer('Sequence', default=1)
    company_id = fields.Many2one("res.company", string="Company", default=lambda self: self.env.company)
    offer_count = fields.Integer(compute='_compute_offer_count', string='Offer Count')

    property_ids = fields.One2many('as.estate.model', 'property_type_id', string="Properties")
    offer_ids = fields.One2many('as.estate.offer.model', 'property_type_id', string='Offers')
    
    _sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'The property type name must be unique.')
    ]
    
    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)