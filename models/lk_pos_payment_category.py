from odoo import fields, models, api


class LkPosPaymentCategory(models.Model):
    _name = 'lk.pos.payment.category'
    _description = 'Categorías de pago para el punto de venta'
    _order = 'sequence'

    name = fields.Char(string='Nombre', required=True, translate=True)
    sequence = fields.Integer(string='Secuencia', default=10, help="Define el orden en el que aparecerán las categorías")
    active = fields.Boolean(string='Activo', default=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "El nombre de la categoría debe ser único!")
    ]