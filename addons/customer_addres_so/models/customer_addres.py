# -*- coding: utf-8 -*-
# @author: Ivan Arriola <admin@autodidactati.com>



from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"


    customer_addres = fields.Char(related='partner_id.street', string='Direccion', readonly=1)
    customer_city = fields.Char(related='partner_id.city', string='Ciudad', readonly=1)
    customer_state = fields.Many2one(related='partner_id.state_id', string='Procincia', readonly=1)

