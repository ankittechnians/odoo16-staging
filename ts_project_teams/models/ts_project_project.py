from odoo import models, fields, api, _


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def _task_message_auto_subscribe_notify(self, users_per_task):
        # Utility method to send assignation notification upon writing/creation.
        template_id = self.env['ir.model.data']._xmlid_to_res_id('project.project_message_user_assigned', raise_if_not_found=False)
        if not template_id:
            return
        task_model_description = self.env['ir.model']._get(self._name).display_name
        for task, users in users_per_task.items():
            if not users:
                continue
            values = {'object': task, 'model_description': task_model_description, 'access_link': task._notify_get_action_link('view')}
            for user in users:
                values.update(assignee_name=user.sudo().name)
                assignation_msg = self.env['ir.qweb']._render('project.project_message_user_assigned', values, minimal_qcontext=True)
                assignation_msg = self.env['mail.render.mixin']._replace_local_links(assignation_msg)
                task.message_notify(
                    subject=_('You have been assigned to %s in %s', task.display_name, task.project_id.name),
                    body=assignation_msg,
                    partner_ids=user.partner_id.ids,
                    record_name=task.display_name,
                    email_layout_xmlid='mail.mail_notification_layout',
                    model_description=task_model_description,
                    mail_auto_delete=False,
                )


class Projects(models.Model):
    _inherit = 'project.project'

    project_team_id = fields.Many2one('project.team', string='Project Team',
                                      help='The Project team is the group of people responsible for '
                                           'executing the tasks and working together towards a common goal '
                                           'by producing deliverables outlined in the project plan and '
                                           'schedule, as directed by the project manager, at whatever level '
                                           'of effort or participation defined for them.')
    team_member_ids = fields.Many2many('res.users', string='Team Members', ondelete="cascade")
    account_manager_id = fields.Many2one('res.users', string='Account Manager',
                                         help='Account managers act as client advocates and work with '
                                              'Project Manager, Project Team, and internal departments to '
                                              'ensure that client needs are understood and satisfied. They '
                                              'may assist with making sales, handling client complaints, '
                                              'collecting and analyzing data, and improving the overall '
                                              'customer experience.')

    def write(self, values):
        if 'project_team_id' in values:
            project_team_id = self.env['project.team'].browse(values['project_team_id'])
            if not self.user_id and project_team_id.project_manager_id:
                values['user_id'] = project_team_id.project_manager_id.id
            if not self.account_manager_id and project_team_id.account_manager_id:
                values['account_manager_id'] = project_team_id.account_manager_id.id
            if 'team_member_ids' not in values and project_team_id.team_member_ids:
                values['team_member_ids'] = [(6, 0, project_team_id.team_member_ids.ids)]
        return super(Projects, self).write(values)

    @api.onchange('project_team_id')
    def _onchange_partner_id(self):
        if self.project_team_id:
            if not self.user_id:
                self.write({'user_id': self.project_team_id.project_manager_id.id})
            if not self.account_manager_id:
                self.write({'account_manager_id': self.project_team_id.account_manager_id.id})
            self.write({'team_member_ids': self.project_team_id.team_member_ids})

    @api.onchange('team_member_ids')
    def _onchange_team_members(self):
        related_project_team = self.env['project.team'].search([('id', '=', self.project_team_id.id)])
        team_members = []
        if self.env['ir.config_parameter'].get_param('ts_project_teams.project_team'):
            for member_id in self.team_member_ids.ids:
                team_members.append((member_id))
            related_project_team.write({'team_member_ids': team_members})

    @api.onchange('user_id', 'account_manager_id')
    def _update_project_manager(self):
        if self.project_team_id:
            related_project_team = self.env['project.team'].search([('id', '=', self.project_team_id.id)])
            for rec in self:
                if rec.user_id:
                    related_project_team.write({'project_manager_id': rec.user_id.id})
                if rec.account_manager_id:
                    related_project_team.write({'account_manager_id': rec.account_manager_id.id})