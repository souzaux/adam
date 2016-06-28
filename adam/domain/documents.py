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
    amount, bank
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

SocialSecurityCategory = namedtuple(
    'SocialSecurityCategory', 'TC01, TC02, TC03, TC04, TC05, TC06, TC07, '
    'TC08, TC09, TC10, TC11, TC12, TC13, TC14, TC15, TC16, TC17, TC18, '
    'TC19, TC20, TC21, TC22')
ss_categories = SocialSecurityCategory(
    TC01=0,
    TC02=1,
    TC03=2,
    TC04=3,
    TC05=4,
    TC06=5,
    TC07=6,
    TC08=7,
    TC09=8,
    TC10=9,
    TC11=10,
    TC12=11,
    TC13=12,
    TC14=13,
    TC15=14,
    TC16=15,
    TC17=16,
    TC18=17,
    TC19=18,
    TC20=19,
    TC21=20,
    TC22=21,
)

DocumentTransportMode = namedtuple(
    'DocumentTransportMode', 'sender, recipient, courier')
transport_mode = DocumentTransportMode(
    sender=1,
    recipient=2,
    courier=3,
)

DocumentShippingTerms = namedtuple(
    'DocumentShippingTerms', 'delivery_duty_paid, ex_works')
shipping_terms = DocumentShippingTerms(
    delivery_duty_paid=1,
    ex_works=2,
)

DocumentVariation = namedtuple(
    'DocumentVariation', 'discount, payment_discount, raise_')
variations = DocumentVariation(
    discount=1,
    payment_discount=2,
    raise_=3,
)

url = topology.documents

bill_to = {
    'type': 'dict',
    'required': True,
    'schema': {
        'contact_id': required_objectid,
        'name': required_string,
        'vat_id_number': {'type': 'vat'},
        'tax_id_number': {'type': 'tax_id_number'},
    }
}
bill_to['schema'].update(address['schema'])

ship_to = {
    'type': 'dict',
    'schema': {
        'name': {'type': 'string'}
    }
}
ship_to['schema'].update(address_ex['schema'])

document_number = {
    'type': 'dict',
    'required': True,
    'schema': {
        'numeric': required_integer,
        'string': {'type': 'string'},
        'complete': required_string,
    }
}

payment = {
    'type': 'dict',
    'required': True,
    'schema': {
        'current': {
            'type': 'dict',
            'schema': payment_definition['schema'],
        },
        'base_date_for_payments': {'type': 'datetime'},
    }
}

current = copy.deepcopy(currency)
current['required'] = True

document_currency = {
    'type': 'dict',
    'required': True,
    'schema': {
        'current': current,
        'exchange_rate': {'type': 'float', 'required': True},
    }
}
vat = {
    'type': 'dict',
    'required': True,
    'schema': copy.deepcopy(vat_definition['schema'])
}
vat['schema']['code']['unique'] = False
vat['schema']['name']['unique'] = False

agent_courier = {
    'type': 'dict',
    'schema': {
        'contact_id': required_objectid,
        'name': required_string,
    }
}
agent_courier['schema'].update(contact_details)


shipping = {
    'type': 'dict',
    'schema': {
        'volume': {'type': 'integer'},
        'unit_of_measure': {'type': 'string'},
        'weight': {'type': 'float'},
        'appearance': {'type': 'string'},
        'date': {'type': 'datetime'},
        'transport_mode': {
            'type': 'dict',
            'required': True,
            'schema': {
                'code': {
                    'type': 'integer',
                    'required': True,
                    'allowed': transport_mode._asdict().values(),
                },
                'description': {'type': 'string'}
            }
        },
        'terms': {
            'type': 'dict',
            'required': True,
            'schema': {
                'code': {
                    'type': 'integer',
                    'required': True,
                    'allowed': shipping_terms._asdict().values(),
                },
                'description': {'type': 'string'}
            }
        },
        'driver': {
            'type': 'dict',
            'schema': {
                'name': required_string,
                'license_id': {'type': 'string'},
                'plate_id': {'type': 'string'},
            },
        },
        'courier': agent_courier,
    }
}

social_security_category = {
    'type': 'dict',
    'required': True,
    'schema': {
        'category': {
            'type': 'integer',
            'required': True,
            'allowed': ss_categories._asdict().values(),
        },
        'description': {'type': 'string'}
    }
}

social_security = {
    'type': 'list',
    'schema': {
        'type': 'dict',
        'schema': {
            'rate': {'type': 'float'},
            'taxable': amount,
            'amount': amount,
            'withholding': {'type': 'boolean'},
            'vat': vat,
            'category': social_security_category,
        }
    }
}

variation_category = {
    'type': 'dict',
    'required': True,
    'schema': {
        'category': {
            'type': 'integer',
            'required': True,
            'allowed': variations._asdict().values(),
        },
        'description': {'type': 'string'}
    }
}

variation = {
    'type': 'list',
    'schema': {
        'type': 'dict',
        'schema': {
            'rate': {'type': 'float'},
            'amount': amount,
            'category': variation_category,
        }
    }
}

withholding_tax = {
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

fees = {
    'type': 'list',
    'schema': {
        'type': 'dict',
        'schema': {
            'name': required_string,
            'amount': {'type': 'integer', 'default': 0},
            'is_from_payment': {'type': 'boolean', 'required': True},
            'vat': vat,
        }
    }
}

_schema = {
    common_key.date: required_datetime,             # docment date
    common_key.category: category,
    'status': status,
    common_key.currency: document_currency,
    'reason': required_string,
    'number': document_number,
    'expiration_date': {'type': 'datetime'},
    'payment': payment,
    'bank': bank,
    'bill_to': bill_to,
    'ship_to': ship_to,
    'agent': agent_courier,
    'withholding_tax': withholding_tax,
    'rebate': {'type': 'integer', 'default': 0},
    'shipping': shipping,
    'notes': {'type': 'string'},
    'social_security_collection': social_security,
    'variation_collection': variation,
    'fee_collection': fees,
    #common_key.total: {
    #    'type': 'integer',
    #    'default': 0,
    #},             # total amount
}
_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
    # 'allow_unknown': True
}
definition.update(base_def)
