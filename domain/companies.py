# -*- coding: utf-8 -*-

"""
    definition
    ~~~~~~~~~

    blah

"""

import common

_schema = {
    # name
    'n': {
        'type': 'string',
        'required': True,
    },
    'pw': {
        'type': 'string',
    },
}
_schema.update(common.schema)

definition = {
    'url': 'definition',                      # defaults to resource key
    'item_title': 'company',
    'additional_lookup': common.company_lookup,
    'schema': _schema,
}
definition.update(common.base)
