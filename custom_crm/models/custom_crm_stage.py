from odoo import api, fields, models
from odoo.exceptions import ValidationError


class CustomCrmStage(models.Model):
    _inherit = 'crm.stage'

    is_offer = fields.Boolean(
        string='Is Offering Stage ?',
        help='Checks if the stage is an offer stage'
    )


class ApprovalRequestInherit(models.Model):
    _inherit = 'approval.request'

    category_id = fields.Many2one('approval.category', string="Category", required=True, change_default=True)




class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    def _get_hours_per_day(self, date_from):
        calendars = self._get_calendars(date_from)
        return calendars[self.id].hours_per_day if calendars.get(self.id) else 24
