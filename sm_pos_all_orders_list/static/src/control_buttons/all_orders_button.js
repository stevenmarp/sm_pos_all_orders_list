/** @odoo-module */

import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";

export class AllOrdersButton extends Component {
    static template = "sm_pos_all_orders_list.AllOrdersButton";

    setup() {
        this.pos = usePos();
    }
    click() {
        this.pos.showScreen("TicketScreen", {
            ui: { filter: "SYNCED" },
        });
    }
}

ProductScreen.addControlButton({
    component: AllOrdersButton,
    condition: function () {
        return true;
    },
});
