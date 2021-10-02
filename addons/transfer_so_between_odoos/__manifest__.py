# -*- coding: utf-8 -*-

{
    'name': 'Transfer SO Between Odoos',
    'version': '11.0.1.0.0',
    'category': 'Sale',
    'license': 'AGPL-3',
    'summary': "Transfer SO Between Odoos",
    'author': 'Ivan Arriola, Autodidacta TI',
    'website': 'https://autodidactati.com',
    'depends': ['sale','base','account','contacts'],
    'data': [
        'views/sale_order.xml',
        'views/res_partner.xml',
        'wizard/transfers_so.xml',
        ],
    'images': ['static/description/banner.png'],
    'installable': True,
}
