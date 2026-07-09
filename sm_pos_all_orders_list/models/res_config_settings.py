from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_order_load_type = fields.Selection(
        related='pos_config_id.pos_order_load_type', readonly=False)
    pos_order_load_days = fields.Integer(
        related='pos_config_id.pos_order_load_days', readonly=False)
