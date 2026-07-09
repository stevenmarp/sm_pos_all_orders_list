# -*- coding: utf-8 -*-
{
    "name": "POS All Orders List",
    "version": "18.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Search & list all POS orders, search by customer/receipt, and choose how many past orders to preload.",
    "description": """
POS All Orders Search & List
============================

View all past POS orders, search by customer or receipt reference,
and choose how many past orders to preload, directly within the running POS session.

* Load orders of the current session, all past orders, or last 'n' days
* Search by customer name, date, or receipt number
* Open native Ticket Screen with pre-filtered synced orders
    """,
    "author": "Steven Marp",
    "website": "https://apps.odoo.com/apps/modules/browse?author=Steven Marp",
    "license": "OPL-1",
    "images": ["static/description/banner.gif"],
    "depends": ["point_of_sale"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "sm_pos_all_orders_list/static/src/control_buttons/all_orders_button.js",
            "sm_pos_all_orders_list/static/src/control_buttons/all_orders_button.xml",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "price": 18.00,
    "currency": "USD",
}
