# -*- coding: utf-8 -*-
"""
    adam.domain.companies.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'companies' resource and schema settings.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import required_string, base_def

_schema = {
    # company id ('id')
    'name': required_string,                       # name
    'password': {'type': 'string', 'nullable': True},  # password
}

definition = {
    'url': 'companies',
    'item_title': 'company',
    'schema': _schema,
}
definition.update(base_def)
