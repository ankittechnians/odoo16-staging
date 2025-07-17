from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def open_email_wizard_from_sale(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Send Custom Email',
            'res_model': 'task.email.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_id': self.id,
            }
        }