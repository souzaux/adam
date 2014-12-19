# -*- coding: utf-8 -*-
"""
    adam.domain.accounts.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    'accounts' (payable/receivable) resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple
from common import key as common_key, required_datetime, required_integer, \
    base_def, base_schema

SchemaKey = namedtuple('SchemaKey', 'date, amount, type, payable, ' +
                       'receivable, company')
key = SchemaKey(
    date=common_key.date,
    amount=common_key.amount,
    type=common_key.type,
    payable='p',
    receivable='r',
    company=common_key.company
)

_schema = {
    key.date: required_datetime,              # account date
    key.amount: required_integer,             # amount
    key.type: {                               # p = payable; r = receivable
        'type': 'string',
        'allowed': [key.payable, key.receivable],
        'required': True
    }
    }
_schema.update(base_schema)

definition = {
    'schema': _schema,
}
definition.update(base_def)
