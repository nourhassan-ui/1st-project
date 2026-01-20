from odoo import http
from odoo.http import request
from odoo.addons.website.controllers import form


class OpportunityPortal(form.WebsiteForm):
    def insert_record(self, request, model, values, custom, meta=None):
        visitor_sudo = request.env['website.visitor']._get_visitor_from_request()
        visitor_partner = visitor_sudo.partner_id
        if visitor_partner.grade_id:
            values['partner_assigned_id'] = visitor_partner.id
        else:
            values['partner_assigned_id'] = False
        values['type'] = 'lead'
        result = super(OpportunityPortal, self).insert_record(request, model, values, custom, meta=meta)
        return result
