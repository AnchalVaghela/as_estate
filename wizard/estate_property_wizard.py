from odoo import api, fields, models

class EstatePropertyWizard(models.TransientModel):
    _name = 'estate.property.wizard'
    _description = 'Create Person Data Wizard'

    name = fields.Char("Name", required=False)
    age = fields.Integer("Age", required=False)
    number_of_records = fields.Integer("Number of Records", default=1, required=True)
    # website_id = fields.Many2one('website', string='Website', default=lambda self: self.env['website'].get_current_website())

    def create_records(self):
        stu_data = {
            'name': self.name,
            'age': self.age,
        }
        self.env['estate.property.wizard'].create(stu_data)

    def action_save(self):
        # self.ensure_one()
        return {'type': 'ir.actions.act_window_close'}

    def search_records(self):
        search_records = self.env['estate.property.wizard'].search([('age', '>=', 18)])      
        return {
            'name': 'Search Results',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'estate.property.wizard',
            'domain': [('id', 'in', search_records.ids)],
            'target': 'current',
        }
        # return search_records

    def write_records(self):
        find = self.env['estate.property.wizard'].search([('name', '=', 'Gauri')])
        if find:
            find.write({
                'age': 30,
            })
            print("Value is Updated")  

    
 
    def delete_records(self):
        name = self.name
        
        find = self.env['estate.property.wizard'].search([('name', '=', name)])
        if find:
            find.unlink()
            print("Value is Deleted")


    def show_records(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Search Results',
            'res_model': 'estate.property.wizard',
            'view_mode': 'list,form',
        }
    
    # def search_count(self):
    #     records = self.env['estate.property.wizard'].search_count([('age', '>=', 18)])
    #     print(f"Found {records} records with age >= 18")
        