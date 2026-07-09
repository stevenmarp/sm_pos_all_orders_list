odoo.define('sm_pos_all_orders_list.AllOrdersButton', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require('web.custom_hooks');

    class AllOrdersButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this._onClick);
        }
        _onClick() {
            this.showScreen('OrderManagementScreen');
        }
    }
    AllOrdersButton.template = 'sm_pos_all_orders_list.AllOrdersButton';

    ProductScreen.addControlButton({
        component: AllOrdersButton,
        condition: function () {
            return true;
        },
    });

    Registries.Component.add(AllOrdersButton);

    return AllOrdersButton;
});
