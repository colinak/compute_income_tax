#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
# from odoo.addons.compute_income_tax.wizard.compute_isr import ComputeIsr
import xlwt
import xlsxwriter
import logging
_logger = logging.getLogger(__name__)


class ComputeIsr(models.AbstractModel):
    _name = 'report.compute_income_tax.compute_isr_report'
    _inherit = 'report.report_xlsx.abstract'





    def generate_xlsx_report(self, workbook, data, partners):
        account_move_line = self.env['compute.isr.wizard'].get_account_move_line()

        for obj in partners:
            report_name = obj.name
            color_blue = '#8EB4E3'
            thead_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'bg_color': color_blue
                }
            )
            merge_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter'}
            )
            worksheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            worksheet.set_column('A:A', 50)
            worksheet.set_column('B5:N5', 15)
            worksheet.merge_range('B1:N1', 'Calculo ISR GR Consulting', merge_format)
            worksheet.merge_range('B2:N2',
                'DETERMINACIÓN DE LOS PAGOS PROVISIONALES DEL IMPUESTO SOBRE LA RENTA',
                merge_format
            )
            worksheet.merge_range('B3:N3', 'EJERCICIO 2020', merge_format)
            worksheet.write('A5', 'CONCEPTO', thead_format)
            worksheet.write('B5', 'Enero', thead_format)
            worksheet.write('C5', 'Febrero', thead_format)
            worksheet.write('D5', 'Marzo', thead_format)
            worksheet.write('E5', 'Abril', thead_format)
            worksheet.write('F5', 'Mayo', thead_format)
            worksheet.write('G5', 'Junio', thead_format)
            worksheet.write('H5', 'Julio', thead_format)
            worksheet.write('I5', 'Agosto', thead_format)
            worksheet.write('J5', 'Septiembre', thead_format)
            worksheet.write('K5', 'Octubre', thead_format)
            worksheet.write('L5', 'Noviembre', thead_format)
            worksheet.write('M5', 'Diciembre', thead_format)

            columns = ['A', 'B', 'C', 'D' 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
            column = 0
            counter = 7
            for account in account_move_line:
                name = str(account.account_id.code) + " " + str(account.account_id.name)
                # if account.account_id.name
                fila_a = "A" + str(counter)
                fila_b = "B" + str(counter)
                # fila_c = "C" + str(counter)
                worksheet.write(fila_a, str(name))
                worksheet.write(fila_b, str(account.credit))
                # worksheet.write(value, str(account.account_id.name))
                counter += 1
            for item in range(1):
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Ingresos Totales', bold)
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Ingresos  meses anteriores', bold)
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Ingresos acumulables', bold)
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Coeficiente de Utilidad')
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Utilidad fiscal estimada', bold)
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Inventario acumulable mensual')
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Anticipo a Socios')
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Utilidad base', bold)
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Pérdidas fiscales de ejercicios anteriores')
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Utilidad base del pago')
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Tasa de ISR vigente (%)', bold)
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Importe del pago provisional ISR', bold)
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Pagos provisionales efectuados')
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'Pagos del mes')
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'ISR Bancario')
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'TOTAL A PAGAR', bold)
                counter += 1
                fila_A = "A" + str(counter)
                worksheet.write(fila_A, 'DECLARACIONES PRESENTADAS:')
                counter += 1
                counter = 7
            workbook.close()
