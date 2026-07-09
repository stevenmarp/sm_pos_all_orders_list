from datetime import timedelta

from odoo import api, fields, models
from odoo.osv import expression


class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def _load_pos_data_domain(self, data, config):
        domain = super()._load_pos_data_domain(data, config)
        if config.pos_order_load_type == 'current':
            return domain
        past = [('state', '!=', 'draft'), ('config_id', '=', config.id)]
        if config.pos_order_load_type == 'days':
            cutoff = fields.Datetime.now() - timedelta(days=config.pos_order_load_days or 0)
            past.append(('date_order', '>=', cutoff))
        return expression.OR([domain, past])

    @api.model
    def search_paid_order_ids(self, config_id, domain, limit, offset):
        config = self.env['pos.config'].browse(config_id)
        extra_domain = []
        if config.pos_order_load_type == 'current':
            session = self.env['pos.session'].search([
                ('config_id', '=', config_id),
                ('state', '=', 'opened')
            ], limit=1)
            extra_domain = [('session_id', '=', session.id)] if session else [('id', '=', 0)]
        elif config.pos_order_load_type == 'days':
            cutoff = fields.Datetime.now() - timedelta(days=config.pos_order_load_days or 0)
            extra_domain = [('date_order', '>=', cutoff)]

        if extra_domain:
            domain = expression.AND([domain, extra_domain])

        return super().search_paid_order_ids(config_id, domain, limit, offset)

