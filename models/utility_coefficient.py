#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class UtilityCoefficient(models.Model):
    _name = 'utility.coefficient'
    _description = 'Coeficiente de Utilidad'


    @api.depends('date')
    def _compute_name(self):
        months = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre"
        }
        if self.date != False:
            month = int(self.date.month)
            self.name = "CU-{}-{}".format(months.get(month), self.date.year)


    name = fields.Char(
        string="Nombre",      
        # required=True,
        compute=_compute_name,
        store=True,
        help=u"Nombre o Descripción del Coeficiente de Utilidad."
    )
    date = fields.Date(
        string="Fecha",
        required=True,
        help="Fecha para el C.U"
    )
    utility_coefficient = fields.Float(
        string="Coeficiente de Utilidad",
        required=True,
        help="Valor para el Coeficiente de Utilidad"
    )
    income_tax_rate_id = fields.Many2one(
        "income.tax.rate",
        required=True,
        string="Tasa ISR"
    )

    @api.constrains('income_tax_rate_id', 'date')
    def _constrains_date_cu(self):
        if self.income_tax_rate_id and self.date:
            start_date = self.income_tax_rate_id.start_date
            end_date = self.income_tax_rate_id.end_date
            if int(self.date.year) < int(start_date.year):
                raise ValidationError(
                    '¡ERROR!\n'+
                    'La Fecha del C.U No Puede ser Menor a la Fecha Inicial de la Tarifa Seleccionada'
                )
            elif int(self.date.year) > int(end_date.year):
                if int(self.date.month) > 3:
                    raise ValidationError(
                        '¡ERROR!\n'+
                        'La Fecha del C.U No Puede ser Mayor al 31 de Marzo del Año Siguiente'
                    )
 


