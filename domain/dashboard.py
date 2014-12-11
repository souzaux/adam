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


_meta = {
    'b': {
        'type': 'dict',
        'required': True,
        'schema': {
            'c': {
                'type': 'list',
                'maxlength': 2,
            },
            'p': {
                'type': 'list',
                'maxlength': 2,
            },
        },
    },
}

_schema = {
    'y': required_datetime,             # current year
    'b': _meta,                         # billed
    'o': _meta,                         # orders
    'p': {
        'd': required_integer,    # due
        'o': required_integer,    # overdue
        'r': _meta,                     # received
    },
}
_schema.update(base_schema)

definition = {
    'url': 'dashboard',
    'item_title': 'dashboard',
    'additional_lookup': company_lookup,
    'schema': _schema,
}
definition.update(base_def)
