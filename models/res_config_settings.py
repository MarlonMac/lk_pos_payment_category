from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    iface_lk_pos_payment_category = fields.Boolean(
        string='Habilitar categorías de pago', 
        default=True,
        help="Habilita el uso de categorías para los métodos de pago en el punto de venta"
    )

    def set_values(self):
        """
        Almacena el valor del campo en la configuración de parámetros de Odoo 
        cuando se guardan los cambios en la configuración.
        """
        super(ResConfigSettings, self).set_values()
        config_parameters = self.env['ir.config_parameter'].sudo()
        config_parameters.set_param('lk_pos_payment_category.iface_lk_pos_payment_category', self.iface_lk_pos_payment_category)

    def get_values(self):
        """
        Recupera el valor del campo desde la configuración de parámetros de Odoo 
        cuando se carga la configuración.
        """
        res = super(ResConfigSettings, self).get_values()
        config_parameters = self.env['ir.config_parameter'].sudo()
        res.update(
            iface_lk_pos_payment_category=config_parameters.get_param('lk_pos_payment_category.iface_lk_pos_payment_category', default=True)
        )
        return res