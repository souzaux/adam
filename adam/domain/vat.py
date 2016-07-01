# -*- coding: utf-8 -*-
"""
    adam.domain.vat.py
    ~~~~~~~~~~~~~~~~~~

    'vat' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import copy

from common import base_def, base_schema, topology, required_string, \
    unique_string, required_objectid


url = topology.vat

_natura_pa = {
    'type': 'dict',
    'schema': {
        'code': required_string,
        'description': required_string
    }
}

_schema = {
    'name': unique_string,
    'code': {'type': 'string', 'required': True, 'unique': True},
    'rate': {'type': 'float'},
    'non_deductible': {'type': 'float'},
    'is_intra': {'type': 'boolean'},
    'is_split_payment': {'type': 'boolean'},
    'natura_pa': _natura_pa,
}

_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
}
definition.update(base_def)

vat_field = {
    'type': 'dict',
    'required': True,
    'schema': copy.deepcopy(definition['schema'])
}
vat_field['schema']['code']['unique'] = False
vat_field['schema']['name']['unique'] = False

agent_courier = {
    'type': 'dict',
    'schema': {
        'contact_id': required_objectid,
        'name': required_string,
    }
}
