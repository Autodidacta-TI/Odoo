# -*- coding: utf-8 -*-
import logging

from odoo import fields, models, api


logger = logging.getLogger(__name__)
class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('street')
    def _direccion_completa(self):
        if self.street != False and self.city != False and self.state_id.name != False:
            self.direccion_completa = self.street + ", " + self.city + ", " + self.state_id.name
        else:
            self.direccion_completa = ''

    direccion_completa = fields.Char(string="Direccion completa", compute=_direccion_completa)