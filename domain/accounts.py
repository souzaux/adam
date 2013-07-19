# -*- coding: utf-8 -*-
"""
    adam.domain.accounts.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    'accounts' resource and schema settings.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import base_schema, required_string

_schema = {
    'u': required_string,   # username
    'p': required_string,   # password
    'r': required_string,   # role
    't': required_string,   # token
}

definition = {
    'url': 'accounts',
    'item_title': 'account',
    'additional_lookup': {
        'url': '[\w]+',     # to be unique
        'field': 'u'
    },
    'schema': _schema,
}
definition.update(base_schema)
