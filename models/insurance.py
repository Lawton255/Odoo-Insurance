from odoo import models, fields, api

class insurance(models.Model):
    _name = 'insurance.insurance'
    _rec_name = 'truck_type'
    _order    = 'exp_date asc'

    @api.one
    @api.depends('exp_date', 'state')
    def _compute_days_left(self):
        """return a dict with as value for each contract an integer
        if contract is in an open state and is overdue, return 0
        if contract is in a closed state, return -1
        otherwise return the number of days before the contract expires
        """
        for record in self:
            if  (record.exp_date and (record.state == 'open' or record.state == 'expire' or record.state == 'closed')):
                today = fields.Date.from_string(fields.Date.today())
                renew_date = fields.Date.from_string(record.exp_date)
                diff_time = (renew_date - today).days
                record.days_left = diff_time



    @api.multi
    def button_expire(self):
        for rec in self:
            rec.write({'state': 'expire'})

    @api.multi
    def button_closed(self):
       for rec in self:
           rec.write({'state': 'closed'})
    

            

   # @api.onchange('truck_type')
   # def _truck_type(self):
   #     if self.truck_type == 'hose':
   #         self.truck = self.truck_hose
   #     else:
   #         self.truck = self.truck_trailer
    
    supplier_name  = fields.Selection([('insurance', 'Insurance'), ('sumatra', 'Sumatra'), 
    ('c28', 'C28'), ('comesa', 'Comesa'), ('carbon_tax', 'Carbon Tax'), ('permit_tax', 'Permit Tax')], required=True)
    agent = fields.Many2one('tax.agent')
    licence_no  = fields.Char(string="Licence no")
    receipt_no  = fields.Char(string="Receipt no", required=False)
    truck_type  = fields.Selection([('hose', 'Hose'), ('trailer', 'Trailer'),], required=True)
    #truck       = fields.Selection(string="Truck")
    truck_hose      = fields.Many2one('fleet.vehicle', string='Truck hose',required=False)
    truck_trailer   = fields.Many2one('trailer', string='Truck trailer', required=False)
    amount      = fields.Float(string="Amount", required=True)
    paid_by     = fields.Many2one('res.partner', string="Paid by" , required=True)
    paid        = fields.Boolean(string="Paid", default=True , required=True)
    payment_method = fields.Selection([('cash', 'Cash'), ('cheque', 'Cheque'), ('mobile_money', 'Mobile Money'),], required=True)
    payment_reference = fields.Char(string='Payment reference', required=False)
    #payment_attach = fields.Many2one('ir.attachment', string='Payment Attachment(File)', ondelete='cascade')
    #payment_attach = fields.Binary(string="Payment attachment(File)")
    image = fields.Binary(string="Payment attachment")
    commence_date  = fields.Date(string='Start Date' , required=True)
    exp_date       = fields.Date(string='Expiry Date' , required=True)
    state = fields.Selection([('open', 'In Progress'), ('expire', 'Expired'),
    ('closed', 'Closed'),], required=True, default='open', track_visibility='onchange')
    days_left = fields.Integer(string="Days Left to Expire" ,compute="_compute_days_left")
