from odoo import models, fields, api
from odoo.exceptions import UserError

class TaskEmailWizard(models.TransientModel):
    _name = 'task.email.wizard'
    _description = 'Custom Task Email Wizard'

    partner_id = fields.Many2one('res.partner', string="Recipient", required=True)
    subject = fields.Char(string="Subject", required=True)
    body = fields.Html(string="Body", required=True)
    task_id = fields.Many2one('project.task', string="Task")
    sale_id = fields.Many2one('sale.order', string="Sale Order")
    template_id = fields.Many2one('mail.template',string='Load template')
    crm_id = fields.Many2one('crm.lead', string="CRM Lead")
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'task_email_wizard_ir_attachments_rel',
        'wizard_id', 'attachment_id',
        string='Attachments'
    )


    @api.onchange('template_id')
    def _onchange_template_id(self):
        if self.template_id:
            self.subject = self.subject or ''
            self.body = self.template_id.body_html

    def send_custom_email(self):
        if not self.partner_id.email:
            raise UserError("Recipient must have an email address.")

        mail_values = {
            'subject': self.subject,
            'body_html': self.body,
            'email_to': self.partner_id.email,
            'auto_delete': True,
            'message_type': 'email',
            'attachment_ids': [(6, 0, self.attachment_ids.ids)],
        }

        self.env['mail.mail'].create(mail_values).send()

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if res.get('crm_id'):
            crm = self.env['crm.lead'].browse(res['crm_id'])
            res['partner_id'] = crm.partner_id.id if crm.partner_id else False
        return res

