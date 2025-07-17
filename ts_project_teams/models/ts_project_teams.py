from odoo import models, fields,api


class ProjectTeam(models.Model):
    _name = 'project.team'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Project Team'

    name = fields.Char(string='Name', required=True)
    team_member_ids = fields.Many2many('res.users', string='Team Members', ondelete="cascade",
                                       help='The Project team is the group of people responsible for '
                                            'executing the tasks and working together towards a common '
                                            'goal by producing deliverables outlined in the project plan '
                                            'and schedule, as directed by the project manager, at whatever '
                                            'level of effort or participation defined for them.')
    account_manager_id = fields.Many2one('res.users', string='Account Manager',
                                         help='Account managers act as client advocates and work with '
                                              'Project Manager, Project Team, and internal departments to '
                                              'ensure that client needs are understood and satisfied. They '
                                              'may assist with making sales, handling client complaints, '
                                              'collecting and analyzing data, and improving the overall '
                                              'customer experience.')
    project_manager_id = fields.Many2one('res.users', string='Project Manager',
                                         help='A Project Manager is in charge of ensuring their teams '
                                              'complete all projects, tasks, and milestones on time and '
                                              'within budget. They manage individual tasks for their '
                                              'respective teams with keen attention to detail to avoid any '
                                              'unpleasant surprises.')

    @api.onchange('project_manager_id')
    def _onchange_project_manager(self):
        for rec in self:
            if rec.project_manager_id:
                team_members = rec.team_member_ids.ids
                team_members.append(rec.project_manager_id.id)
                rec.write({'team_member_ids': team_members})


class ProjectTeamMembers(models.Model):
    _name = 'project.team.members'
    _description = 'Project Team Members'