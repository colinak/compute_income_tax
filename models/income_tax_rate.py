#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date
import logging
_logger = logging.getLogger(__name__)

class IncomeTaxRate(models.Model):
    _name = 'income.tax.rate'
    _description = 'Tasa de Impuesto Sobre la Renta'

    @api.depends('start_date')
    def _compute_name(self):
        if self.start_date != False:
            self.name = "Tasa ISR - {}".format(self.start_date.year)


    name = fields.Char(
        string="Description",      
        # required=True,
        compute="_compute_name",
        store=True,
        help=u"Nombre o Descripción de la Tasa ISR"
    )
    rate_isr = fields.Float(
        string="Tasa ISR",
        help="Valor de la Tasa ISR."
    )
    start_date = fields.Date(
        string="Fecha Inicial",
        required=True,
        help="Seleccione una Fecha de Inicio para la Tasa ISR"
    )
    end_date = fields.Date(
        string="Fecha Final",
        required=True,
        help="Seleccione una Fecha de Culminación para la Tasa ISR"
    )
    active = fields.Boolean(
        string="Activo.?",
        default=False,
        help="Define si la Tasa esta Acticva o no."
    )
    utility_coefficient_ids = fields.One2many(
        "utility.coefficient",
        "income_tax_rate_id",
        string="Coeficiente de Utilidad"
    )

    _sql_constraints = [
        (
            'name_unique',
            'UNIQUE(name)',
            '¡ERROR!\n'+
            u'No Puede Existir Más de Una Tarida ISR con en Mismo Año de Vigencia'
        ),
    ]


    @api.constrains('active')
    def _constrains_active(self):
        if self.active:
            isr = self.env['income.tax.rate'].search([])
            if len(isr) > 1:
                raise ValidationError(
                    '¡ERROR!\n'+
                    'No Puede Existir mas de una Tarifa ISR Activa.'
                )


    # @api.constrains('name')
    # def _constrains_active(self):
        # if self.name:
            # domain = [('name', '=', self.name)]
            # isr_name = self.env['income.tax.rate'].search(domain)
            # _logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            # _logger.info("RES: " + str(isr_name))
        # raise ValidationError(
            # '¡ERROR!\n'+
            # u'No Puede Existir Más de Una Tarida ISR con en Mismo Año de Vigencia'
        # )


    @api.constrains('start_date', 'end_date')
    def _constrains_date(self):
        today = date.today()
        if self.start_date or self.end_date:
            if int(self.start_date.year) > int(today.year):
                raise ValidationError(
                    '¡ERROR!\n'+
                    u'No puede Crear una Tasa ISR con una Año mayor al Año Actual'
                )
            elif int(self.start_date.year) > int(self.end_date.year):
                raise ValidationError(
                    '¡ERROR!\n'+
                    'La Fecha Inicial NO Puede ser Mayor a la Fecha Final'
                )
            elif int(self.start_date.year) != int(self.end_date.year):
                raise ValidationError(
                    '¡ERROR!\n'+
                    u'La Fecha Final No Puede ser Mayor a Un Año de Vigencia'
                )

