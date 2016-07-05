# -*- coding: utf-8 -*-
"""
    adam.domain.sizes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    'sizes' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import copy

from common import base_def, base_schema, topology, unique_string, address


url = topology.sizes

schema = {
    'name': unique_string,
    'number_collection': {'type': 'list', 'schema': {'type': 'string'}},
}
schema.update(base_schema)

definition = {
    'url': url,
    'schema': schema,
}
definition.update(base_def)
