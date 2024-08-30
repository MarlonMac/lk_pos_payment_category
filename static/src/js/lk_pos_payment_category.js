odoo.define('lk_pos_payment_category.payment_screen', function (require) {
    "use strict";

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require('web.custom_hooks');
    const rpc = require('web.rpc');

    const PwPosPaymentCategoryPaymentScreen = (PaymentScreen) =>
        class extends PaymentScreen {
            constructor() {
                super(...arguments);
                useListener('click-payment-category', this.onClickPaymentCategory);
                this.state = {
                    selectedCategoryId: false,
                };
                this.paymentMethods = [];
                this.paymentCategories = [];
                this.loadPaymentCategories();
            }

            async loadPaymentCategories() {
                const result = await rpc.query({
                    model: 'pos.payment.category',
                    method: 'get_pos_payment_category',
                });
                this.paymentMethods = result.payment_methods;
                this.paymentCategories = result.payment_categories;
                this.render();
            }

            get filteredPaymentMethods() {
                if (this.state.selectedCategoryId) {
                    return this.paymentMethods.filter(
                        (method) => method.category_id && method.category_id[0] === this.state.selectedCategoryId
                    );
                } else {
                    return this.paymentMethods;
                }
            }

            onClickPaymentCategory(event) {
                this.state.selectedCategoryId = event.detail.categoryId;
                this.render();
            }
        };

    Registries.Component.extend(PaymentScreen, PwPosPaymentCategoryPaymentScreen);

    return PaymentScreen;
});