# -*- coding: utf-8 -*-
# from odoo import http


# class AsEstate(http.Controller):
#     @http.route('/as_estate/as_estate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/as_estate/as_estate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('as_estate.listing', {
#             'root': '/as_estate/as_estate',
#             'objects': http.request.env['as_estate.as_estate'].search([]),
#         })

#     @http.route('/as_estate/as_estate/objects/<model("as_estate.as_estate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('as_estate.object', {
#             'object': obj
#         })

