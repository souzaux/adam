# -*- coding: utf-8 -*-
"""
    adam.domain.fees.py
    ~~~~~~~~~~~~~~~~~~~

    'fees' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import copy

from common import base_def, base_schema, topology, required_string
from vat import definition as vat_definition

url = topology.fees

_schema = {
    'name': required_string,
    'amount': {'type': 'float'},
    'vat': {
        'type': 'dict',
        'schema': copy.deepcopy(vat_definition['schema'])
    }
}

_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
}
definition.update(base_def)
