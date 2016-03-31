# -*- coding: utf-8 -*-
"""
    adam.domain.vat.py
    ~~~~~~~~~~~~~~~~~~

    'vat' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import base_def, base_schema, topology, required_string, \
    unique_string


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
