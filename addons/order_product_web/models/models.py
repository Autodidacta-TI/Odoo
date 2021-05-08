# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class ProductOrderWeb(models.Model):
    _inherit = 'product.template'

    is_order = fields.Boolean(string='Ordenado')

    def order_product_web(self):
        order_qty = self.env['product.template'].search([('is_order', '=', True)], order='website_sequence desc', limit=1)
        products = self.env['product.template'].search([('website_published', '=', True),('is_order', '=', False)], order='write_date asc')
        contador = order_qty.website_sequence

        for product in products:
            contador += 1
            product.website_sequence = contador
            product.is_order = True
