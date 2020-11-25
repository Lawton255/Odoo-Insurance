from odoo import models, fields

class insurance(models.Model):
    _name = 'insurance.insurance'

    certificate_no = fields.Integer(string='Insurance Certificate number', unique=True, required=True)
    truck          = fields.Many2one('fleet.vehicle', string='Truck',required=True)
    insurer        = fields.Many2one('res.partner', string='Insurer' , required=True)
    commence_date  = fields.Date(string='Commencement Date' , required=True)
    exp_date       = fields.Date(string='Expiry Date' , required=True)

    #_sql_constraints = [( 'unique(certificate_no)',)]