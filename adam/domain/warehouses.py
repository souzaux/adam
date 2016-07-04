# -*- coding: utf-8 -*-
"""
    adam.domain.warehouses.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    'warehouses' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import base_def, base_schema, topology, unique_string, address

url = topology.warehouses

schema = {
    'name': unique_string,
    'notes': {'type': 'string'},
    'address': address,
}
schema.update(base_schema)

definition = {
    'url': url,
    'schema': schema,
}
definition.update(base_def)
