# -*- coding: utf-8 -*-
"""
    adam.domain.accounts.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    'accounts' (payable/receivable) resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from domain.common import base_def, base_schema, required_datetime, \
    required_integer

amount_key = 't'
date_key = 'd'
type_key = 't'

_schema = {
    date_key: required_datetime,              # account date
    amount_key: required_integer,             # amount
    type_key: {                               # p = payable; r = receivable
        'type': 'string',
        'allowed': ['p', 'r'],
        'required': True
    }
    }
_schema.update(base_schema)

definition = {
    'schema': _schema,
}
definition.update(base_def)
