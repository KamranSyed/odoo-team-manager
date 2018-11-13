# -*- coding: utf-8 -*-
from odoo import http

# class Ksteam(http.Controller):
#     @http.route('/ksteam/ksteam/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ksteam/ksteam/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ksteam.listing', {
#             'root': '/ksteam/ksteam',
#             'objects': http.request.env['ksteam.ksteam'].search([]),
#         })

#     @http.route('/ksteam/ksteam/objects/<model("ksteam.ksteam"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ksteam.object', {
#             'object': obj
#         })