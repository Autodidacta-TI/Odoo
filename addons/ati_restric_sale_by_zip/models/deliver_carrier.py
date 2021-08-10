# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2021 Autodidactati now <http://www.autodidactati.com/>
#
##############################################################################
from odoo import api, fields, models, exceptions
from odoo import tools
import logging

logger = logging.getLogger(__name__)

class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'
    
    restrics_zip = fields.Many2many(
        comodel_name='ati.restric.zip',
        string = 'CP restringidos',
        store = True
    )

    partner_not_restrics = fields.Many2many(
        comodel_name='res.partner',
        string = 'Clientes no restringidos',
        store = True
    )



    def _match_address(self, partner):
        self.ensure_one()
        partner_rest = True
        for p in self.partner_not_restrics:
            if p == partner:
                partner_rest = False
        for zips in self.restrics_zip:
            if self.country_ids and partner.zip == zips.name and partner_rest:
                return False
        if self.country_ids and partner.country_id not in self.country_ids:
            return False
        if self.state_ids and partner.state_id not in self.state_ids:
            return False
        if self.zip_from and (partner.zip or '').upper() < self.zip_from.upper():
            return False
        if self.zip_to and (partner.zip or '').upper() > self.zip_to.upper():
            return False
        return True

class RestricSaleZip(models.Model):
    _name="ati.restric.zip"

    name = fields.Char(string="Codigo Postal")