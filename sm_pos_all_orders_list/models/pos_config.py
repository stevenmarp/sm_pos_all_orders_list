from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_order_load_type = fields.Selection(
        [
            ('current', 'Load Orders Of Current Session'),
            ('all', 'Load All Past Orders'),
            ('days', "Load Orders Of Last 'n' Days"),
        ],
        string='Orders Loading Option',
        default='current',
    )
    pos_order_load_days = fields.Integer(string='Number Of Days', default=7)
