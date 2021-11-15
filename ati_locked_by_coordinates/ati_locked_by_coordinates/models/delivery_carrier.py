# -*- encoding: utf-8 -*-
import logging
import requests
import json

from odoo import fields, models
from shapely.geometry import Point, Polygon

logger = logging.getLogger(__name__)

class DeliveryCarrierArea(models.Model):
    """ Inherit Drawing mixins model 'google_maps.drawing.shape.mixin' """
    _name = 'delivery.carrier.area'
    _inherit = ['mail.thread', 'google_maps.drawing.shape.mixin']
    _description = 'Delivery Area'

    delivery_carrier_id = fields.Many2one(
        'delivery.carrier', required=True, ondelete='cascade')


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    shape_line_ids = fields.One2many(
        'delivery.carrier.area', 'delivery_carrier_id', string='Area')

    def _match_address(self, partner):
        self.ensure_one()
        if self.is_coor(partner):
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

    def is_coor(self,partner):
        direccion = partner.street + ',' + partner.city + ', Argentina'
        url = "https://maps.googleapis.com/maps/api/geocode/json?address="
        key = "&key=YOUR-KEY"

        #Se buscan todas las areas restringidas del tipo de envio
        restricted_areas = self.env['delivery.carrier.area'].search([("delivery_carrier_id.id",'=',self.id)])


        #Se busca con api geocode la coordenada de la direccion del cliente
        r = requests.get(url + direccion + key)
        lat_dir = r.json()["results"][0]["geometry"]['location']["lat"]
        lng_dir = r.json()["results"][0]["geometry"]['location']["lng"]
        # Se guarda coordenada en pt_dir para luego comparar con las areas y ver si el punto esta en los polygonos
        pt_dir = Point(lat_dir,lng_dir)

        #Se decalara variable para guardar puntos de polygono para luego crear dicho polygono con Polygon()
        pts_poly =[]
        

        for ra in restricted_areas:
            paths = json.loads(ra.shape_paths)['options']['paths']
            for coor in paths:
                pts_poly.append((coor['lat'],coor['lng']))
            poly = Polygon(pts_poly)
            if (poly.contains(pt_dir)):
                return True
            pts_poly = []