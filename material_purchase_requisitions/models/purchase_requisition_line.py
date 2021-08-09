# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp

class MaterialPurchaseRequisitionLine(models.Model):
    _name = "material.purchase.requisition.line"
    _description = 'Solicitud de Compra de Material'

    
    requisition_id = fields.Many2one(
        'material.purchase.requisition',
        string='Requisiciones',
    )
    product_id = fields.Many2one(
        'product.product',
        string='Producto',
        required=True,
    )

    description = fields.Char(
        string='Descripción',
        required=True,
    )
    qty = fields.Float(
        string='Cantidad',
        digits=(16,6),
        default=1,
        required=True,
    )
    uom = fields.Many2one(
        'uom.uom',
        string='Unidad de Medida',
        required=True,
    )
    partner_id = fields.Many2many(
        'res.partner',
        string='Proveedor',
    )
    requisition_type = fields.Selection(
        selection=[
                    ('internal','Picking Interno'),
                    ('purchase','Orden de Compra'),
        ],
        string='Tipo de Requisición',
        default='purchase',
        required=True,
    )
    @api.onchange('product_id')
    def onchange_product_id(self):
        for rec in self:
            rec.description = rec.product_id.name
            rec.uom = rec.product_id.uom_id.id
