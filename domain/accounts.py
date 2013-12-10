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
    't': required_string,   # token
    'r': {                  # role
        'type': 'list',
        'allowed': ['admin', 'app', 'user'],
        'required': True,
    }
}

definition = {
    'url': 'accounts',
    'item_title': 'account',
    # only admins and apps are allowed to consume this endpoint.
    'allowed_roles': ['admin', 'app'],
    'cache_control': '',
    'cache_expires': 0,
    'additional_lookup': {
        'url': 'regex("[\w]+")',     # to be unique
        'field': 'u'
    },
    'schema': _schema,
}
definition.update(base_schema)
