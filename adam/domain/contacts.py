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
    address_ex, required_string, currency, required_boolean

SchemaKey = namedtuple('SchemaKey', 'company, total, date, type')
key = SchemaKey(
    company=common_key.company,
    total=common_key.total,
    date=common_key.date,
    type=common_key.type
)

url = topology.contacts

_to_upper = lambda v: v.upper()  # noqa

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

# TODO validation of iban and bic_swift should be done against static banks
# service when available.
_bank = {
    'type': 'dict',
    'schema': {
        'name': {'type': 'string'},
        # TODO switch to coerce to_upper when Cerberus 1.0 is released
        # 'iban': {'type': 'iban', 'coerce': _to_upper},
        'iban': {'type': 'iban'},
        'bic_swift': {'type': 'swift'}
    }
}

_other_address = copy.deepcopy(address_ex)
_other_address['schema']['name'] = required_string

# TODO add missing schema fields besides contact_minimal ones.
_schema = {
    'name': required_string,
    'vat': {'type': 'vat', 'unique': True, 'coerce': _to_upper},
    'id_code': {'type': 'string', 'unique': True},
    'tax_id_number': {'type': 'tax_id_number', 'coerce': _to_upper},
    'pa_index': {'type': 'string'},
    'market_area': {'type': 'string'},
    'address': address_ex,
    'currency': currency,
    'is': _is,
    'bank': _bank,
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
