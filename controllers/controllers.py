# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class RasaHelper(http.Controller):
    @http.route('/rasa-helper/module-install', auth='public', type="http", methods=["POST"], csrf=False)
    def install_module(self, **kw):
        try:
            module_name = kw.get('module_name')
            ir_module = request.env["ir.module.module"]
            is_module_installed = ir_module.sudo().search(
                [('name', "=", module_name)], limit=1)

            if is_module_installed.state == "uninstalled":
                is_module_installed.button_immediate_install()
                return json.dumps({"Success": True, "message": "Successfully Installed"})
            return json.dumps({"Success": True, "message": "Already Installed"})
        except Exception as e:
            return json.dumps({"Success": False, "message": e})
    # @http.route('/rasa-helper/rasa-helper/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('rasa-helper.listing', {
    #         'root': '/rasa-helper/rasa-helper',
    #         'objects': http.request.env['rasa-helper.rasa-helper'].search([]),
    #     })

    # @http.route('/rasa-helper/rasa-helper/objects/<model("rasa-helper.rasa-helper"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('rasa-helper.object', {
    #         'object': obj
    #     })
