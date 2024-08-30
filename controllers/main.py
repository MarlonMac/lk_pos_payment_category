from odoo import http
from odoo.http import request


class PosPaymentCategoryController(http.Controller):

    @http.route('/get_pos_payment_category', type='json', auth='public')
    def get_pos_payment_category(self):
        payment_method_ids = request.env['pos.payment.method'].search([])
        payment_categories = request.env['lk.pos.payment.category'].search([])
        return {
            'payment_methods': [{
                'id': payment_method.id,
                'name': payment_method.name,
                'category_id': [payment_method.lk_pos_payment_category_id.id, payment_method.lk_pos_payment_category_id.name] if payment_method.lk_pos_payment_category_id else False
            } for payment_method in payment_method_ids],
            'payment_categories': [{
                'id': payment_category.id,
                'name': payment_category.name,
                'sequence': payment_category.sequence
            } for payment_category in payment_categories],
        }