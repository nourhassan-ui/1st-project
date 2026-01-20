# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class CustomCrm(models.Model):
    _inherit = 'crm.lead'

    is_commit = fields.Boolean(
        string='Commitment',
        readonly=True,
        store=True,
        help='Check if the lead is committed to the project.'
    )

    is_offer_stage = fields.Boolean(
        string='Offer Stage',
        compute='compute_offer_stage',
        readonly=True
    )

    def make_commit(self):
        for rec in self:
            if float(rec.expected_revenue) <= 0.0:
                raise ValidationError(
                    'Expected Revenue must be greater than 0.'
                )
            if not rec.date_deadline:
                raise ValidationError(
                    'Date Deadline is required.'
                )
            if not rec.is_commit:
                rec.is_commit = True

    def make_un_commit(self):
        for rec in self:
            if rec.is_commit:
                rec.is_commit = False

    @api.onchange('stage_id')
    def onchange_stage_id(self):
        for rec in self:
            if rec.is_commit:
                if rec.stage_id.sequence < rec._origin.stage_id.sequence:
                    raise ValidationError('Cannot move to a stage with a lower sequence number.')

    @api.depends('expected_revenue')
    def _compute_prorated_revenue(self):
        for lead in self:
            lead.prorated_revenue = lead.expected_revenue or 0.0

    @api.depends('stage_id')
    def compute_offer_stage(self):
        for rec in self:
            rec.is_offer_stage = False
            if rec.stage_id.is_offer:
                if self.env.user.has_group("custom_crm.group_can_edit_offering_opportunities"):
                    rec.is_offer_stage = False
                else:
                    rec.is_offer_stage = True

    def write(self, vals):
        for rec in self:
            new_stage = self.env['crm.stage'].browse(vals.get('stage_id')) if vals.get('stage_id') else rec.stage_id
            if rec.is_commit and new_stage and new_stage.sequence < rec.stage_id.sequence:
                raise ValidationError('Cannot move to a stage with a lower sequence number.')
            if rec.is_offer_stage and new_stage and new_stage.sequence < rec.stage_id.sequence and rec.stage_id.is_offer:
                raise ValidationError('Cannot move to an offering stage with a lower sequence number.')
            if new_stage and new_stage.sequence < rec.stage_id.sequence and rec.stage_id.is_won:
                raise ValidationError('Cannot move to a Won stage with a lower sequence number.')
        return super(CustomCrm, self).write(vals)
