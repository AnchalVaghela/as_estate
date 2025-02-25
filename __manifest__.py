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
    'data' : [
        'security/ir.model.access.csv',
        'views/estate_views.xml',
        'views/estate_menus.xml',
        'views/res_users_views.xml',
    #     'views/estate_menus.xml',
    #     'views/estate_property_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True
}