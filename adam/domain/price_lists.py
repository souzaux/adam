# -*- coding: utf-8 -*-
"""
    adam.domain.price_lists.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    'price-lists' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import copy

from common import base_def, base_schema, topology, unique_string


url = topology.price_lists

schema = {
    'name': unique_string,
}
schema.update(base_schema)

definition = {
    'url': url,
    'schema': schema,
}
definition.update(base_def)
