# -*- coding: utf-8 -*-

# Part of GECOERP. See LICENSE file for full copyright and licensing details.

{
    'name': 'Integración de Requisición de Materiales en Hoja de Costos',
    'version': '2.5',
    'currency': 'MX',
    'price': 8700.0,
    'depends': [
        'gecoerp_job_costing_management',
    ],
    'support': 'contacto@gecoerp.com',
    'author': 'MSASTER CONSULTING RESOURCES & CO S.C.',
    'website': 'https://www.gecoerp.com',
    'license': 'Other proprietary',
    'category' : 'Projects',
    'summary': 'Integración de Requisición de Materiales en Hoja de Costos',
    'description': """
    Integración de Requisición de Materiales en Hoja de Costos
            """,
    'data': [
        'views/mpr_line_view.xml',
        'views/jobcost_line_view.xml',
        'views/job_cost_report.xml',
        'views/mpr_view.xml',
             ],
    'installable': True,
    'application': False,
}
