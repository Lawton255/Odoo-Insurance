from odoo import models, fields, api

class insurance(models.Model):
    _name = 'insurance.insurance'
    _rec_name = 'truck'

    @api.multi
    def button_expire(self):
        for rec in self:
            rec.write({'state': 'expire'})

    @api.multi
    def button_closed(self):
        for rec in self:
            rec.write({'state': 'closed'})

    certificate_no = fields.Integer(string='Insurance Certificate number', unique=True, required=True)
    truck          = fields.Many2one('fleet.vehicle', string='Truck',required=True)
    insurer        = fields.Many2one('res.partner', string='Insurer' , required=True)
    amount      = fields.Integer(string="Amount", required=True)
    commence_date  = fields.Date(string='Start Date' , required=True)
    exp_date       = fields.Date(string='Expiry Date' , required=True)

    state = fields.Selection([('open', 'In Progress'), ('expire', 'Expired'),
   ('closed', 'Closed'),], required=True, default='open')
