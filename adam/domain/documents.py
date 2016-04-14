# -*- coding: utf-8 -*-
"""
    adam.domain.documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'documents' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import copy
from collections import namedtuple

from common import base_def, base_schema, required_datetime, \
    key as common_key, required_string, topology, address, required_objectid, \
    required_integer, currency, address_ex, contact_details, required_boolean,\
    amount
from payments import definition as payment_definition
from vat import definition as vat_definition


DocumentCategory = namedtuple(
    'DocumentCategory', 'delivery_note, shipping_invoice, deposit_invoice, '
    'proforma, invoice')
categories = DocumentCategory(
    delivery_note=1,
    shipping_invoice=2,
    deposit_invoice=3,
    invoice=4,
    proforma=22,
)

DocumentStatus = namedtuple(
    'DocumentStatus', 'draft, invoiced_delivery_note, issued')
status = DocumentStatus(
    draft=1,
    invoiced_delivery_note=2,
    issued=3,
)

url = topology.documents

billing_address = {
    'type': 'dict',
    'required': True,
    'schema': {
        'contact_id': required_objectid,
        'name': required_string,
        'vat_id_number': {'type': 'vat'},
        'tax_id_number': {'type': 'tax_id_number'},
    }
}
billing_address['schema'].update(address['schema'])

delivery_address = {
    'type': 'dict',
    'schema': {
        'name': {'type': 'string'}
    }
}
delivery_address['schema'].update(address_ex['schema'])

document_number = {
    'type': 'dict',
    'required': True,
    'schema': {
        'numeric': required_integer,
        'string': {'type': 'string'},
        'complete': {'type': required_string}
    }
}

payment = {
    'type': 'dict',
    'required': True,
    'schema': payment_definition['schema']
}

vat = {
    'type': 'dict',
    'schema': copy.deepcopy(vat_definition['schema'])
}
vat['schema']['code']['unique'] = False

social_security = {
    'type': 'dict',
    'schema':{
        'rate': {'type': 'float'},
        'amount': amount,
        'vat': vat,
    }
}

agent_courier = {
    'type': 'dict',
    'schema': {
        'contact_id': required_objectid,
        'name': required_string,
    }
}
agent_courier['schema'].update(contact_details)

witholding_tax = {
    'type': 'dict',
    'schema': {
        'rate': {'type': 'float'},
        'amount': amount,
        'taxable_share': {'type': 'float'},
        'is_social_security_included': required_boolean
    }
}

category = {
    'type': 'dict',
    'required': True,
    'schema': {
        'code': {
            'type': 'integer',
            'required': True,
            'allowed': categories._asdict().values(),
        },
        'description': {'type': 'string'}
    }
}
status = {
    'type': 'dict',
    'required': True,
    'schema': {
        'code': {
            'type': 'integer',
            'required': True,
            'allowed': status._asdict().values(),
        },
        'description': {'type': 'string'}
    }
}

_schema = {
    common_key.date: required_datetime,             # docment date
    common_key.category: category,
    'status': status,
    common_key.currency: currency,
    'reason': required_string,
    #'number': document_number,
    #'payment': payment,
    #'bill_to': billing_address,
    #common_key.total: {
    #    'type': 'integer',
    #    'default': 0,
    #},             # total amount
    #'ship_to': delivery_address,
    #'agent': agent_courier,
    #'courier': agent_courier,
    #'social_security': vat,
    'witholding_tax': witholding_tax,
    #'items': {
    #    'type': 'list',
    #    'schema': {
    #        'type': 'dict',
    #        'schema': {
    #            'sku': {'type': 'string'},
    #            'description': required_string
    #        }
    #    }
    #}
}
_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
    # 'allow_unknown': True
}
definition.update(base_def)
