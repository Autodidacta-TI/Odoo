# -*- coding: utf-8 -*-
# @author: Ivan Arriola <admin@autodidactati.com>



from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"


    transfer_so = fields.Boolean(string='Orden Trasnferida')

