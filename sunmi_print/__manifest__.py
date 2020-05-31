{
    'name': 'Sunmi Print',
    'version': '1.0',
    'category': 'Sale',
    'sequence': 100,
    'summary': 'Sunmi Print',
    'description': """
Sunmi Print Module
==================================
    """,
    'author': '7th Computing',
    'website': 'http://www.7thcomputing.com',
    'images': [],
    'depends': ['sale', 'stock', 'account'],
    'data': [           
        'views/sale_order_view.xml',
        'views/assets.xml',
        'reports/report_actions.xml',
        'reports/report_assets.xml',
        'reports/report_sale_order_template_mobile.xml',
        'reports/report_delivery_order_template_mobile.xml',
        'reports/report_invoice_template_mobile.xml',
        'views/stock_picking_view.xml',
        'views/account_move_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
