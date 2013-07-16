# -*- coding: utf-8 -*-
"""
    adam.domain.companies.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'companies' resource and schema settings.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
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
    'url': 'companies',
    'item_title': 'company',
    'additional_lookup': common.company_lookup,
    'schema': _schema,
}
definition.update(common.base)
