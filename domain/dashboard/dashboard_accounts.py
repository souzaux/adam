# -*- coding: utf-8 -*-
"""
    adam.domain.dashboard_accounts.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'dashboard_accounts' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from domain.dashboard.common import month_series, year, year_key
from domain.common import required_integer, base_def, base_schema
from domain.accounts import payable_key, receivable_key

# TODO db index on company+year

debit_due_key = 'd'
credit_due_key = 'c'
month_series_key = 's'

_schema = {
    year_key: year,
    payable_key: {                          # accounts payable
        debit_due_key: required_integer,    # debit due
        month_series_key: month_series,     # months series
    },
    receivable_key: {                       # accounts receivable
        credit_due_key: required_integer,   # credit due
        month_series_key: month_series,     # month series
    }
}
_schema.update(base_schema)

definition = {
    'url': 'dashboard-accounts',
    'item_title': 'accounts payable and receivable',
    'datasource': {'source': 'dashboard_accounts'},
    'schema': _schema,
}
definition.update(base_def)
