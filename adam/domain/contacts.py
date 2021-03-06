# -*- coding: utf-8 -*-
"""
    adam.domain.contacts.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    'contacts' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import copy
from collections import namedtuple
from common import base_def, base_schema, key as common_key, topology, \
    address_ex, required_string, currency, required_boolean, to_upper, bank

SchemaKey = namedtuple('SchemaKey', 'company, total, date')
key = SchemaKey(
    company=common_key.company,
    total=common_key.total,
    date=common_key.date,
)

url = topology.contacts

_is = {
    'type': 'dict',
    'required': True,
    'schema': {
        'active': required_boolean,
        'company': required_boolean,
        'client': required_boolean,
        'vendor': required_boolean,
        'courier': required_boolean,
        'agent': required_boolean,
        'area_manager': required_boolean,
    }
}

_other_address = copy.deepcopy(address_ex)
_other_address['schema']['name'] = required_string

bank['required'] = False

_schema = {
    'name': required_string,
    'id_code': {'type': 'string', 'unique': True},
    'vat_id_number': {'type': 'vat', 'unique': True, 'coerce': to_upper},
    'tax_id_number': {'type': 'tax_id_number', 'unique': True,
                      'coerce': to_upper},
    'pa_index': {'type': 'string', 'minlength': 6, 'maxlength': 6},
    'market_area': {'type': 'string'},
    'address': address_ex,
    'currency': currency,
    'is': _is,
    'bank': bank,
    'other_addresses': {
        'type': 'list',
        'schema': _other_address
    }
}

_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
}
definition.update(base_def)
