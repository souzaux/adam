# -*- coding: utf-8 -*-
"""
    adam.domain.contacts.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    'contacts' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple
from common import base_def, base_schema, key as common_key, topology, \
    address_ex, required_string

SchemaKey = namedtuple('SchemaKey', 'company, total, date, type')
key = SchemaKey(
    company=common_key.company,
    total=common_key.total,
    date=common_key.date,
    type=common_key.type
)

url = topology.contacts

# TODO add missing schema fields besides contact_minimal ones.
_schema = {
    'name': required_string,
    'vat': {'type': 'string'},
    #'vat': {'type': 'string', 'unique': True},
    'address': address_ex
}

_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
}
definition.update(base_def)
