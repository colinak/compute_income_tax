#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Compute Income Tax",
    "version": "12.0.1.1.0",
    "category": u"Account",
    "website": "https://github.com/colinak",
    "author": "Kewitz Colina",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        'base',
        'account'
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/income_tax_menuitem.xml',
        'views/income_tax_rate_view.xml',
        'views/utility_coefficient_view.xml',
        'views/account_account_view.xml',
        'wizard/compute_isr_wizar.xml',
    ],
    "demo": [
    ],
}
