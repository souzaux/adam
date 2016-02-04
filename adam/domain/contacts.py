# -*- coding: utf-8 -*-
"""
    adam.domain.contacts.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    'contacts' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple
from common import base_def, base_schema, key as common_key, topology, \
    contact_minimal

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


url = topology.contacts

# TODO add missing schema fields besides contact_minimal ones.
_schema = {}

_schema.update(contact_minimal)
_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
}
definition.update(base_def)
