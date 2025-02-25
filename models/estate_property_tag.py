from odoo import models,fields

class as_estate_tag(models.Model):
    _name = 'as.estate.tag.model'
    _description = "Estate Tag Model"
    _order = 'name'

    name = fields.Char(required=True)

    color = fields.Integer(string="Color")  
    _sql_constraints = [
        ('unique_tag_name', 'UNIQUE(name)', 'The property tag name must be unique.')
    ]