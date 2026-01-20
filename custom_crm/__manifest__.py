# -*- coding: utf-8 -*-
{
    'name': "Custom Crm",

    'summary':  "Custom Crm",

    'description': "Custom Crm",

    'author': "ScandoSolution.co",

    'website': "https://www.scndosol.com",

    'category': 'Uncategorized',

    'version': '0.1',

    'depends': ['base', 'crm','website','portal','website_crm_partner_assign' , 'approvals' , 'hr_holidays'],

    'data': [
        'security/ir.model.access.csv',
        'security/custom_crm_security.xml',
        'views/custom_crm_view.xml',
        'views/custom_crm_stage_view.xml',
        'views/custom_portal_opportunity.xml',
    ],
    'installable': True,

    'application': True,

    'auto_install': False,
}

