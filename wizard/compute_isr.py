#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import xlwt
import base64
from openpyxl import Workbook
import logging
_logger = logging.getLogger(__name__)


class ComputeIsr(models.TransientModel):
    _name = 'compute.isr.wizard'
    _description = 'Calculo de ISR segun cuentas Contable'

    start_date = fields.Date(
        string="Fecha Inicio"
    )
    end_date = fields.Date(
        string="Fecha Final"
    )

    @api.multi
    def get_account_move_line(self):
        # _logger.info("Ini: " + str(self.start_date))
        # _logger.info("Fin: " + str(self.end_date))
        account_move_line = self.env['account.move.line'].search(
            [
                # ('date', '>=', self.start_date),
                # ('date', '<=', self.end_date),
                ('account_id.allow_compute_isr', '=', True)
            ]
        )
        _logger.info("Cuentas: "+ str(account_move_line))
        # for account in account_move_line:
            # _logger.info("Apunte: " + str(account))
            # _logger.info("Cuenta: " + str(account.account_id.name))
            # _logger.info("Codigo: " + str(account.account_id.code))
            # _logger.info("Haber: " + str(account.credit))
        return account_move_line


    @api.multi
    def excel_report_generate(self):
        return self.env.ref('compute_income_tax.isr_xlsx_report').report_action(self)
        # return self.env.ref('compute_income_tax.isr_xlsx_report').report_action(self)
        # # Recordar Validar Las Fechas ante de imprimir el reporte
        # if self.start_date > self.end_date:
            # raise ValidationError('La Fecha de Inicio NO Puede ser Mayor a la Fecha Final')
        # else:
            # report_xlsx_isr = self.env['income.tax.rate'].generate_excel_report()
            # return report_xlsx_isr
            # return self.env.ref('compute_income_tax.report_isr_xlsx').report_action(self)
        # # pass
