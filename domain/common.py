# -*- coding: utf-8 -*-

"""
    common.py
    ~~~~~~~~~

    Commonly used schema definitions.
"""


# schema fields
company_id = {
    'type': 'integer',
    'required': True,
}

account = {
    'type': 'string',
    # automatically handled but let's make sure it's always there
    'required': True,
}

# commonly used resource definitions
company_lookup = {
    'url': '^([1-9][0-9]*)$',   # to be unique field
    'field': 'c'
}

base = {
    'auth_username_field': 'a',
}
schema = {
    'c': company_id,
    'a': account,
}
