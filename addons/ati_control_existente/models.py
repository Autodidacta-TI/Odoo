# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import base64
import csv
from datetime import date as dt
import logging

_logger = logging.getLogger(__name__)


class ProductControlExistente(models.Model):
    _name = 'ati.control.existente'
    _description = 'ati.control.existente'

    def btn_process(self):
        _procesados = ""
        _procesados_stock = ""
        _procesados_sin_stock = ""
        _noprocesados = ""
        self.ensure_one()
        if not self.product_match:
            raise ValidationError('Debe seleccionar metodo de busqueda de productos')
        if not self.delimiter:
            raise ValidationError('Debe ingresar el delimitador')
        if not self.product_file:
            raise ValidationError('Debe seleccionar el archivo')
        if self.state != 'draft':
            raise ValidationError('Archivo procesado!')
        self.file_content = base64.decodestring(self.product_file)
        lines = self.file_content.split('\n')
        for i,line in enumerate(lines):
            if self.skip_first_line and i == 0:
                continue
            lista = line.split(self.delimiter)
            if len(lista) == 2:
                default_code = lista[0]
                nombre = lista[1]
                product = self.env['product.template'].search([(self.product_match,'=',default_code)])
                if product:
                    _procesados += "[{}] {} \n".format(default_code, nombre)
                    if product.qty_available > 0:
                        _procesados_stock += "[{}] {} \n".format(default_code, nombre)
                    else:
                        _procesados_sin_stock += "[{}] {} \n".format(default_code, nombre)
                else:
                    _noprocesados += "[{}] {} \n".format(default_code, nombre)
            else:
                _noprocesados += "[{}] {} \n".format(default_code, nombre)
        self.productos_existentes = _procesados
        self.productos_en_stock = _procesados_stock
        self.productos_fuera_stock = _procesados_sin_stock
        self.not_processed_content = _noprocesados
        self.state = 'processed'

    name = fields.Char('Nombre')
    product_file = fields.Binary('Archivo')
    delimiter = fields.Char('Delimitador',default=";")
    state = fields.Selection(selection=[('draft','Borrador'),('processed','Procesado')],string='Estado',default='draft')
    file_content = fields.Text('Texto archivo')
    not_processed_content = fields.Text('Texto no procesado')
    productos_existentes = fields.Text('Productos existentes')
    productos_en_stock = fields.Text('Productos en stock')
    productos_fuera_stock = fields.Text('Productos en stock')
    skip_first_line = fields.Boolean('Saltear primera linea',default=True)
    product_match = fields.Selection(selection=[('default_code','Referencia Interna'),('barcode','Codigo de barras')],string='Buscar producto por...',default='default_code')
	
