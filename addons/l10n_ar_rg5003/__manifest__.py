{
    "name": "l10n_ar_rg5300",
    'version': '11.0.1',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'ADHOC SA,Moldeo Interactive,Odoo Community Association (OCA), Autodidacta TI',
    'license': 'AGPL-3',
    'summary': '',
    'depends': [
        'l10n_ar_account',
    ],
    'external_dependencies': {
        'python': ['pyafipws', 'pysimplesoap.client'],
    },
    'data': [
        'data/account_document_letter.xml',
    ],
    'demo': [
    ],
    'images': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}