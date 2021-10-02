# -*- coding: utf-8 -*-
# @author: Ivan Arriola <admin@autodidactati.com>



from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    url_odoo = fields.Char(string='Url Odoo')
    port_odoo = fields.Char(string='Puerto')
    db_name_odoo = fields.Char(string='Nombre DB')
    user_odoo = fields.Char(string='Usuario')
    passw_odoo = fields.Char(string='Contraseña')