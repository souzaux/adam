# -*- coding: utf-8 -*-
"""
    adam.domain.payment_options.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'payment_methods' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import base_def, base_schema, topology, required_string, \
    unique_string


url = topology.payment_methods

_modalita_pa = {
    'type': 'dict',
    'schema': {
        'code': required_string,
        'description': required_string
    }
}

schema = {
    'name': unique_string,
    'is_bank_receipt': {'type': 'boolean'},
    'pagamento_pa': _modalita_pa,
}

schema.update(base_schema)

definition = {
    'url': url,
    'schema': schema,
}
definition.update(base_def)
