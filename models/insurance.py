from odoo import models, fields, api

class insurance(models.Model):
    _name = 'insurance.insurance'
    _rec_name = 'truck_type'
    _order    = 'exp_date asc'

    @api.multi
    def button_expire(self):
        for rec in self:
            rec.write({'state': 'expire'})

    @api.multi
    def button_closed(self):
        for rec in self:
            rec.write({'state': 'closed'})

    @api.multi
    def _truck_type(self):
        if self.truck_type == 'hose':
            self.truck_type = self.truck_hose
        else:
            self.truck_type = self.truck_trailer
    
    supplier_name  = fields.Selection([('insurance', 'Insurance'), ('sumatra', 'Sumatra'), 
    ('c28', 'C28'), ('comesa', 'Comesa'), ('carbon_tax', 'Carbon Tax'), ('permit_tax', 'Permit Tax')], required=True)
    agent = fields.Many2one('tax.agent')
    licence_no  = fields.Char(string="Licence no")
    receipt_no  = fields.Char(string="Receipt no", required=True)
    truck_type  = fields.Selection([('hose', 'Hose'), ('trailer', 'Trailer'),], required=True)
    truck_hose      = fields.Many2one('fleet.vehicle', string='Truck hose',required=False)
    truck_trailer   = fields.Many2one('trailer', string='Truck trailer', required=False)
    amount      = fields.Float(string="Amount", required=True)
    paid_by     = fields.Many2one('res.partner', string="Paid by" , required=True)
    paid        = fields.Boolean(string="Paid", default=True , required=True)
    payment_method = fields.Selection([('cash', 'Cash'), ('cheque', 'Cheque'), ('mobile_money', 'Mobile Money'),], required=True)
    payment_reference = fields.Char(string='Payment reference', required=True)
    #payment_attach = fields.Many2one('ir.attachment', string='Payment Attachment(File)', ondelete='cascade')
    #payment_attach = fields.Binary(string="Payment attachment(File)")
    image = fields.Binary(string="Payment attachment")
    commence_date  = fields.Date(string='Start Date' , required=True)
    exp_date       = fields.Date(string='Expiry Date' , required=True)
    state = fields.Selection([('open', 'In Progress'), ('expire', 'Expired'),
   ('closed', 'Closed'),], required=True, default='open')
