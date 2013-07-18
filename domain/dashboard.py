# -*- coding: utf-8 -*-
"""
    adam.domain.dashboard.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'dashboard' resource and schema settings.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import common

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
    'b': _meta,                 # billed
    'o': _meta,                 # orders
    'p': {
        'd': common.integer,    # due
        'o': common.integer,    # overdue
        'r': _meta,             # received
    },
}
_schema.update(common.schema)

definition = {
    'url': 'dashboard',
    'item_title': 'dashboard',
    'additional_lookup': common.company_lookup,
    'schema': _schema,
}
definition.update(common.base)
