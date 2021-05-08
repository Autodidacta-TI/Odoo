# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2021 Autodidactati now <http://www.autodidactati.com/>
#
##############################################################################
{
    'name': 'Metodo de Orden E-Commerce',
    'category': 'Web',
    'summary': 'Modulo que crea metodo para un ordenamiento en E-Commerce segun la ultima fecha de modificacion',
    'version': '11.0.1',
    'description': """ Este modulo crea un metodo en el modelo product.template el cual debe ser llamado por una accion planificada para ser ejecutado.
	 El metodo ordena los productos por fecha de moficacion en E-Commerce por medio de su secuencia, tambien se creo un campo llamado "Ordenado" para ques cada vez que el metodo ordene los productos los convierta en True y de esta manera no los vuelva a ordenar, si el usuario lo decea puede desmarcarlos para volver a ordenarlos.
        """,
    'author': 'Autodidacta TI',
    'website': 'http://www.autodidactati.com/',
    'license': '',
    'depends': [
        'sale',
        ],,
    'data': ['views/order_product.xml'],
    'installable': True,
    'application': False,
    'auto_install': False
}
