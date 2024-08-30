from odoo import fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    # El campo iface_lk_pos_payment_category se eliminó de este modelo