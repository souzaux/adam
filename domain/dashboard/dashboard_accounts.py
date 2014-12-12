# -*- coding: utf-8 -*-
"""
    adam.domain.dashboard_accounts.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'dashboard_accounts' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from domain.dashboard.common import month_series
from domain.common import required_integer, base_def, base_schema, \
    required_datetime

_schema = {
    'y': required_datetime,
    'p': {                              # accounts payable
        'd': required_integer,          # debit due
        's': month_series,              # months series
    },
    'r': {                              # accounts receivable
        'c': required_integer,          # credit due
        's': month_series,              # month series
    }
}
_schema.update(base_schema)

definition = {
    'url': 'dashboard-accounts',
    'item_title': 'accounts payable and receivable',
    'schema': _schema,
}
definition.update(base_def)
