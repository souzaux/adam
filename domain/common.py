# -*- coding: utf-8 -*-
"""
    adam.domain.common.py
    ~~~~~~~~~~~~~~~~~~~~~

    Commonly used schema and domain definitions.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
company_key = 'c'
account_key = 'a'

# common data types
required_integer = {
    'type': 'integer',
    'required': True
}

unique_integer = required_integer.copy()
unique_integer['unique'] = True

required_string = {
    'type': 'string',
    'required': True,
    'empty': False
}
unique_string = required_string.copy()
unique_string['unique'] = True

required_datetime = {
    'type': 'datetime',
    'required': True
}

# common fields
company = {
    'type': 'objectid',
    'required': True,
    'data_relation': {
        'resource': 'companies',
        'field': '_id',
    },
}
account = required_string

# common resource settings
company_lookup = {
    'field': company_key
}

# most resources share the following settings
base_def = {
    'auth_field': account_key
}

# most collections share the following schema definition
base_schema = {
    company_key: company,
    # account_key: account,
}
