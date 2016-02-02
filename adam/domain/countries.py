# -*- coding: utf-8 -*-
"""
    adam.domain.countries.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'countries' resource and schema settings.

    :copyright: (c) 2014 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import required_string, base_schema, base_def

_schema = {
    'name': required_string,                       # name
}
_schema.update(base_schema)

definition = {
    'url': 'countries',
    'item_title': 'country',
    'schema': _schema,
}
definition.update(base_def)
