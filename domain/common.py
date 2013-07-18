# -*- coding: utf-8 -*-
"""
    adam.domain.common.py
    ~~~~~~~~~~~~~~~~~~~~~

    Commonly used schema and domain definitions.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
companyid_key = 'id'

# common fields
company = {
    'definition': {
        'type': 'integer',
        'required': True,
        'data_relation': {
            'collection': 'companies',
            'field': companyid_key,
        }
    },
    'key': 'c',
}
account = {
    'definition': {
        'type': 'string',
        # automatically handled but let's make sure it's always there
        'required': True,
    },
    'key': 'a',
}

# common types
integer = {
    'type': 'integer',
    'required': True,
}

# common resource settings
company_lookup = {
    'url': '^([1-9][0-9]*)$',   # to be unique
    'field': company['key']
}

# most resources share the following settings
base = {
    'auth_username_field': account['key']
}

# most collections share the following schema definition
schema = {
    company['key']: company['definition'],
    account['key']: account['definition'],
}
