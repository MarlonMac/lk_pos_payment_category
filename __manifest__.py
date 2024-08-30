{
    'name': "LK POS Payment Category",
    'summary': """
        Categorías de pago en el punto de venta""",
    'description': """
        Este módulo le permitirá crear categorías de pagos en el punto de venta para clasificar los métodos de pago.
    """,
    'author': "Marlon Macario",
    'website': "https://link-gt.com",
    'category': 'Point of Sale',
    'version': '16.0.1.0.0',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/pw_pos_payment_category_view_tree.xml',
        'views/pw_pos_payment_category_view_form.xml',
        'views/pos_config_view_form.xml'
    ],
    'qweb': [
        'static/src/xml/pos.xml'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}