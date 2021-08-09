# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class JobCostLine(models.Model):
    _inherit = 'job.cost.line'

    @api.depends('custom_mpr_line_ids', 'custom_mpr_line_ids.qty', 'custom_mpr_line_ids.requisition_id.state')
    def _compute_actual_requisition_quantity(self):
        for rec in self:
            rec.actual_requisition_qty = sum([p.requisition_id.state not in ['cancel'] and p.qty for p in rec.custom_mpr_line_ids])

    actual_requisition_qty = fields.Float(
        string='Cnt. Requisitada',
        compute='_compute_actual_requisition_quantity',
        store=True,
        digits=(16, 6),
    )
    custom_mpr_line_ids = fields.One2many(
        'material.purchase.requisition.line',
        'custom_job_costing_line_id',
        string="Solicitud de Compra de Materiales",
    )