
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    ts_allow_multi_user = fields.Boolean(
        string='Allow Multi User To Start Task')