# -*- coding: utf-8 -*-
"""
    adam.domain.accounts.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    'accounts' resource and schema settings.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple
from common import base_schema, required_string

SchemaKey = namedtuple('SchemaKey', 'token, roles, username, password')
key = SchemaKey(
    username='username',
    password='password',
    token='token',
    roles='toles'
)

_schema = {
    key.username: required_string,
    key.password: required_string,
    key.token: required_string,
    key.roles: {
        'type': 'list',
        'allowed': ['admin', 'app', 'user'],
        'required': True,
    }
}

definition = {
    'item_title': 'account',
    # only admins and apps are allowed to consume this endpoint.
    'allowed_roles': ['admin', 'app'],
    'cache_control': '',
    'cache_expires': 0,
    'additional_lookup': {
        'url': 'regex("[\w]+")',     # to be unique
        'field': key.username
    },
    'schema': _schema,
}
definition.update(base_schema)
