# -*- coding: utf-8 -*-
"""
    adam.domain.dashboard_accounts.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'dashboard_accounts' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple
from adam.domain.dashboard.common import month_series, year, key as db_key
from adam.domain.common import required_integer, base_def, base_schema, \
    key as common_key
from adam.domain.accounts import key as accounts_key

# TODO db index on company+year

SchemaKey = namedtuple('SchemaKey', 'credit_due, debit_due, month_series,'
                       + 'year, payable, receivable, company')
key = SchemaKey(
    credit_due='cd',
    debit_due='dd',
    month_series='s',
    year=db_key.year,
    payable=accounts_key.payable,
    receivable=accounts_key.receivable,
    company=common_key.company
)

_schema = {
    key.year: year,
    key.payable: {
        key.debit_due: required_integer,
        key.month_series: month_series,
    },
    key.receivable: {
        key.credit_due: required_integer,
        key.month_series: month_series,
    }
}
_schema.update(base_schema)

definition = {
    'url': 'dashboard-accounts',
    'item_title': 'accounts payable and receivable',
    'datasource': {'source': 'dashboard_accounts'},
    'resource_methods': ['GET'],
    'item_methods': ['GET'],
    'schema': _schema,
}
definition.update(base_def)
