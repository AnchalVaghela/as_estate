from odoo import fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('as.estate.model','seller', string="Properties",
                                   domain="[('state', 'in', ['new', 'offerReceived'])]" ) 