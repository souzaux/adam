# -*- coding: utf-8 -*-
"""
    adam.domain.documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'documents' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple
from common import base_def, base_schema, required_datetime, \
    key as common_key, required_string, topology, contact_minimal

SchemaKey = namedtuple('SchemaKey', 'company, total, date, type')
key = SchemaKey(
    company=common_key.company,
    total=common_key.total,
    date=common_key.date,
    type=common_key.type
)

DocumentTypes = namedtuple('DocumentTypes', 'customer_order, invoice')

doctype = DocumentTypes(
    customer_order=10,
    invoice=4
)


url = topology.documents

contact = {
    'type': 'dict',
    'required': True,
    'schema': {
        'contact_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': topology.contacts,
                'field': '_id',
            }
        }
    }
}
contact['schema'].update(contact_minimal)
contact['schema']['vat']['unique'] = False

_schema = {
    key.date: required_datetime,             # docment date
    key.total: {
        'type': 'integer',
        'default': 0,
    },             # total amount
    key.type: {
        'type': 'integer',
        'min': 1,
        'max': 22,
        'allowed': doctype._asdict().values(),
        'required': True
    },
    'contact': contact,
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'sku': {'type': 'string'},
                'description': required_string
            }
        }
    }
}
_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
    # 'allow_unknown': True
}
definition.update(base_def)
