# -*- coding: utf-8 -*-

import logging
import xmlrpc.client
from odoo.exceptions import ValidationError
from odoo import models, api, fields

_logger = logging.getLogger(__name__)


class TransfersSO(models.TransientModel):
    _name = 'ati.transfers.so'
    _description = "Wizard - Transfers SO"

    @api.multi
    def transfer(self):
        ordenes = self._context.get('active_ids')
        
        for line in ordenes:
            _order = self.env['sale.order'].browse(line)
            _order_line = []

            
            _username = _order.partner_id.user_odoo
            _port_odoo = _order.partner_id.port_odoo
            _url_odoo = _order.partner_id.url_odoo
            _pwd = _order.partner_id.passw_odoo
            _dbname = _order.partner_id.db_name_odoo

            # Se arma ruta de Odoo y se comprueba que por lo menos los datos este
            if _url_odoo and _port_odoo:
                sock_common = xmlrpc.client.ServerProxy (str(_url_odoo) + ':' + str(_port_odoo) + '/xmlrpc/common')
            elif _url_odoo:
                sock_common = xmlrpc.client.ServerProxy (str(_url_odoo) + '/xmlrpc/common')
            else:
                raise ValidationError("El cliente no cuenta con datos de su Odoo")
            
            
            uid = sock_common.login(_dbname, _username, _pwd)

            if _url_odoo and _port_odoo:
                sock = xmlrpc.client.ServerProxy(str(_url_odoo) + ':' + str(_port_odoo) + '/xmlrpc/object')
            elif _url_odoo:
                sock = xmlrpc.client.ServerProxy(str(_url_odoo) + '/xmlrpc/object')

            # Se verifica que este creado el Partner en el Odoo a transferir, de lo contrario se crea
            if not len(sock.execute_kw(_dbname, uid, _pwd,'res.partner', 'search',[[['name', '=', self.env.user.company_id.name]]])) > 0:
                partner = {
                    'name': self.env.user.company_id.name,
                    'image': self.env.user.company_id.logo,
                    'supplier': True
                }
                sock.execute(_dbname, uid, _pwd, 'res.partner', 'create', partner)

            # Se verifica que los productos a transferir en la Orden tambien esten existan en el Odoo, de lo contrario se crean
            if _order.order_line != False:
                for line in _order.order_line:
                    if not len(sock.execute_kw(_dbname, uid, _pwd,'product.template', 'search',[[['default_code', '=', line.product_id.default_code]]])) > 0:
                        _product = {
                            'name': line.product_id.name,
                            'image_small': line.product_id.image_small,
                            'default_code': line.product_id.default_code,
                            'barcode': line.product_id.default_code,
                            'list_price': line.product_id.list_price,
                            'standard_price': (line.product_id.list_price/2),
                            'type': line.product_id.type
                        }
                        if len(sock.execute_kw(_dbname, uid, _pwd,'product.category', 'search',[[['name', '=', line.product_id.categ_id.name]]])) > 0:
                            _product['categ_id'] = sock.execute_kw(_dbname, uid, _pwd,'product.category', 'search',[[['name', '=', line.product_id.categ_id.name]]])[0]
                        if len(sock.execute_kw(_dbname, uid, _pwd,'pos.category', 'search',[[['name', '=', line.product_id.categ_id.name]]])) > 0:
                            _product['pos_categ_id'] = sock.execute_kw(_dbname, uid, _pwd,'pos.category', 'search',[[['name', '=', line.product_id.categ_id.name]]])[0]

                        sock.execute(_dbname, uid, _pwd, 'product.template', 'create', _product)
                        _logger.info('************* Se creo producto en odoo cliente: {0}'.format(line.product_id.default_code))

            # Se llena _order_line con _order.order_line
            if _order.order_line != False:
                for line in _order.order_line:
                    _product_line = (sock.execute_kw(_dbname, uid, _pwd,'product.template', 'search',[[['default_code', '=', line.product_id.default_code]]]))[0]
                    _order_line.append((0,0,{'product_id':_product_line,'product_qty':line.qty_delivered,'price_unit':line.price_unit,'name':line.name,'date_planned': fields.Datetime.now(),'product_uom':line.product_uom.id}))

            # Se crea orden
            so_order = {
               'partner_id': sock.execute_kw(_dbname, uid, _pwd,
                                                'res.partner', 'search',
                                                [[['name', '=', self.env.user.company_id.name]]])[0],
                'partner_ref': _order.name,
                'date_planned': fields.Datetime.now(),
                'order_line': _order_line,
                'origin': _order.name
            }
            sock.execute(_dbname, uid, _pwd, 'purchase.order', 'create', so_order)
            _order.transfer_so = True