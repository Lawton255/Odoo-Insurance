from odoo import models, fields, api

class insurance(models.Model):
    _name = 'insurance.insurance'
    _rec_name = 'truck'
    _order    = 'exp_date asc'

    @api.multi
    def button_expire(self):
        for rec in self:
            rec.write({'state': 'expire'})

    @api.multi
    def button_closed(self):
        for rec in self:
            rec.write({'state': 'closed'})

    licence_no  = fields.Char(string="Licence no")
    receipt_no  = fields.Char(string="Receipt no", required=True)
    truck          = fields.Many2one('fleet.vehicle', string='Truck hose',required=True)
    supplier_name  = fields.Selection([('insurance', 'Insurance'), ('sumatra', 'Sumatra'), 
    ('c28', 'C28'), ('comesa', 'Comesa'), ('carbon_tax', 'Carbon Tax'), ('permit_tax', 'Permit Tax')], required=True)
    amount      = fields.Float(string="Amount", required=True)
    paid_by     = fields.Many2one('res.partner', string="Paid by" , required=True)
    paid        = fields.Boolean(string="Paid", default=True , required=True)
    commence_date  = fields.Date(string='Start Date' , required=True)
    exp_date       = fields.Date(string='Expiry Date' , required=True)

    state = fields.Selection([('open', 'In Progress'), ('expire', 'Expired'),
   ('closed', 'Closed'),], required=True, default='open')
