# -*- coding: utf-8 -*-
{
    'name': 'Locked by coordinates',
    'version': '13.0',
    'author': 'Ivan Arriola',
    'license': 'AGPL-3',
    'maintainer': 'Ivan Arriola',
    'support': 'admin@autodidactati.com',
    'category': 'Extra Tools',
    'description': """
Locked by coordinates
=======================

Locked sale order by coordinates in web site
""",
    'depends': [
        'web_google_maps',
        'web_google_maps_drawing',
        'website_sale_delivery'
    ],
    'demo': [],
    'images': [],
    'data': [
        'views/delivery_carrier_area.xml',
        'views/map_view_webiste_sale_delivery.xml',
    ],
    'qweb': [],
    'installable': True
}
