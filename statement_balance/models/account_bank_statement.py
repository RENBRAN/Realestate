# -*- coding: utf-8 -*-

from pickle import TRUE
from odoo import models, fields, api, _

class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"
    statement_balance = fields.Monetary('Statement Balance', 
                                       compute='_compute_statement_balance', readonly=True, store=False, tracking=False,
                                       )
    
    @api.depends('balance_end', 'balance_start')
    def _compute_statement_balance(self):
        for record in self:
            record.statement_balance = (record.balance_end - record.balance_start)      
 