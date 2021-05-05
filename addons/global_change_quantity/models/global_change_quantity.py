# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2021 Autodidacta TI now <http://www.autodidactati.com/>
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)
class SaleOrder(models.Model):
    _inherit = "sale.order"
    sale_type = fields.Boolean(string='Devolucion', default=False,readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})

    @api.onchange('sale_type')
    def onchange_change_quantity(self):
        for order in self:
            for line in order.order_line:
                if line.product_uom_qty >= 0 and self.sale_type is True:
                    line.product_uom_qty = (line.product_uom_qty - (line.product_uom_qty * 2))
                elif line.product_uom_qty < 0 and self.sale_type is False:
                    line.product_uom_qty = (line.product_uom_qty - (line.product_uom_qty * 2))
