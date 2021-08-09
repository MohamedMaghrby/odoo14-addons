# -*- coding: utf-8 -*-

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    dest_location_id = fields.Many2one(
        'stock.location',
        string='Locación Destino',
        groups='hr.group_hr_user'
    )

