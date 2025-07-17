from odoo import api, fields, models


class ResConfigSetting(models.TransientModel):
    _name = 'res.config.settings'
    _inherit = 'res.config.settings'

    project_team = fields.Boolean(string='PROJECT TEAM')

    @api.model
    def get_values(self):
        res = super(ResConfigSetting, self).get_values()
        res.update(project_team=self.env['ir.config_parameter'].sudo().get_param('ts_project_teams.project_team'))
        return res

    def set_values(self):
        super(ResConfigSetting, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('ts_project_teams.project_team', self.project_team)