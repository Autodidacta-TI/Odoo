# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2021 Autodidactati now <http://www.autodidactati.com/>
#
##############################################################################
{
    'name': 'Resctriccion de carritos por ZIP',
    'category': 'Web',
    'summary': 'Resctriccion de carritos por ZIP',
    'version': '11.0.1',
    'description': """ Resctriccion de carritos por ZIP""",
    'author': 'Autodidacta TI',
    'website': 'http://www.autodidactati.com/',
    'license': '',
    'depends': [
        'sale',
        'delivery',
        'website_sale_delivery'
        ],
    'data': [
        'views/delivery_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}