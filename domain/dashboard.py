# -*- coding: utf-8 -*-
"""
    adam.domain.dashboard.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'dashboard' resource and schema settings.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import required_integer, company_lookup, base_def, base_schema, \
    required_datetime


_month_series = {
    'type': 'list',
    'maxlength': 12,
    'minlength': 12,
    'required': True,
    'schema': {
        'type': 'dict',
        'schema': {
            'a': required_integer,      # amount
            'q': required_integer,      # quantity
        }
    }
}

_year_series = {
    'type': 'dict',
    'required': True,
    'schema': {
        'c': _month_series,             # current year
        'p': _month_series,             # previous year
    },
}

_accounts_payable_receivable = {
    'p': {                              # accounts payable
        'd': required_integer,          # debit due
        's': _month_series,             # month series
    },
    'r': {                              # account receivable
        'c': required_integer,          # credit due
        's': _month_series,             # month series
    }
}

_schema = {
    'y': required_datetime,             # current year
    'b': _year_series,                  # billed
    'o': _year_series,                  # orders
    'a': _accounts_payable_receivable,  # accounts payable and receivable
    }
_schema.update(base_schema)

definition = {
    'url': 'dashboard',
    'item_title': 'dashboard',
    'additional_lookup': company_lookup,
    'schema': _schema,
}
definition.update(base_def)
