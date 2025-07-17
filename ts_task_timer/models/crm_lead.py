from odoo import models, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def open_email_wizard_from_crm(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Send Custom Email',
            'res_model': 'task.email.wizard',  # 👈 Reuse the same wizard if it's generic
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_crm_id': self.id,
            }
        }