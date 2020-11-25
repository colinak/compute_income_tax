#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ComputeIsr(models.TransientModel):
    _name = 'compute.isr.wizard'
    _description = 'Calculo de ISR segun cuentas Comtable'

    start_date = fields.Date(
        string="Fecha Inicio"
    )
    end_date = fields.Date(
        string="Fecha Final"
    )
