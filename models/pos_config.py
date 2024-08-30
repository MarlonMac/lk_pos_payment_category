from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    iface_lk_pos_payment_category = fields.Boolean(string='Habilitar categorías de pago', default=True,
                                                  help="Habilita el uso de categorías para los métodos de pago en el punto de venta")