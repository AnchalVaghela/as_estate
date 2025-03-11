from odoo import models,fields

class as_estate_tag(models.Model):
    _name = 'as.estate.tag.model'
    _description = "Estate Tag Model"
    _order = 'name'

    name = fields.Char(required=True)
    color = fields.Integer(string="Color")  
    company_id = fields.Many2one("res.company", string="Company", default=lambda self: self.env.company)

    _sql_constraints = [
        ('unique_tag_name', 'UNIQUE(name)', 'The property tag name must be unique.')
    ]