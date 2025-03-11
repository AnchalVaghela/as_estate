# # -*- coding: utf-8 -*-
# {
#     'name': "as_estate",

#     'summary': "Short (1 phrase/line) summary of the module's purpose",

#     'description': """
# Long description of module's purpose
#     """,

#     # 'author': "My Company",
#     # 'website': "https://www.yourcompany.com",

#     # Categories can be used to filter modules in modules listing
#     # check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
#     # for the full list
#     'category': 'Uncategorized',
#     'version': '0.1',

#     # any module necessary for this one to work correctly
#     'depends': ['base'],

#     # always loaded
#     # 'data': [
#     #     # 'security/ir.model.access.csv',
#     #     'views/views.xml',
#     #     'views/templates.xml',
#     # ],
#     # only loaded in demonstration mode
#     # 'demo': [
#     #     'demo/demo.xml',
#     # ],
# }

{
    'name': 'Estate Management',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/estate_property_wizard_views.xml',
        'views/estate_menus.xml',
        'views/estate_tag_views.xml',
        'views/estate_type_views.xml',
        'views/estate_views.xml',
        'views/res_users_views.xml',
        'report/ir_actions_report.xml',
        'report/estate_report_template.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'sequence':1
}
# 
