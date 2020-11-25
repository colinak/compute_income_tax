#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class AccountAccount(models.Model):
    _inherit = 'account.account'
    _description = 'Cuentas Contables'
    
    allow_compute_isr = fields.Boolean(
        string="Permitir Calculo ISR",
        help="Hace la cuenta contable como seleccinable para el calculo ISR"
    )

