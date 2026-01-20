{
    'name': "College ERP",
    'summary': "A comprehensive ERP system for managing college operations.",
    'description': """
        This module provides functionalities to manage students, courses, faculty, and administrative tasks in a college setting.
    """,
    'version': '18.0.1.1',
    'category': 'Education',
    'author': "Noureldin",
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir_model_data.xml',
        "security/ir.model.access.csv",
        'security/ir_model_access.xml',
        'views/college_erp_views.xml',
        'views/college_entities_views.xml',
    ],
    'installable': True,
    'application': True,
}