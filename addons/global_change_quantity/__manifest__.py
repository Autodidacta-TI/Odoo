# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2021 Autodidactati now <http://www.autodidactati.com/>
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Global Change Quantity on SO',
    'category': 'Sale',
    'summary': 'Global Change Quantity on SO orders.',

    'version': '11.0.1',
    'description': """
Global Change Quantity on SO, PO and Invoice
================================
This module provides the feature to change quantity for negative or positive on sale orders.
        """,

    'author': 'Autodidacta TI',
    'website': 'http://www.autodidactati.com/',
    'license': 'Other proprietary',

    'depends': [
        'sale',
        'purchase',
        'account'
        ],

    'data': [
        'views/global_change_quantity_view.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
