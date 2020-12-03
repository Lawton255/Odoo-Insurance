from odoo import models, fields

class TaxAgent(models.Model):
    _name = 'tax.agent'

    name = fields.Char(string="Agent name")