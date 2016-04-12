# -*- coding: utf-8 -*-
"""
    adam.domain.common.py
    ~~~~~~~~~~~~~~~~~~~~~

    Commonly used schema and domain definitions.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple

TopologyKey = namedtuple('TopologyKey', 'countries, companies, ' +
                         'dashboard_accounts, dashboard_documents, ' +
                         'documents, accounts, contacts, vat, ' +
                         'payment_methods, fees, payments')
topology = TopologyKey(
    accounts='accounts',
    companies='companies',
    contacts='contacts',
    countries='countries',
    dashboard_accounts='dashboard-accounts',
    dashboard_documents='dashboard-documents',
    documents='documents',
    fees='fees',
    payment_methods='payment-methods',
    payments='payments',
    vat='vat',
)


SchemaKey = namedtuple('SchemaKey', 'company, account, amount, date, type, ' +
                       'total, quantity, category, currency')
key = SchemaKey(
    company='company_id',
    account='account',
    amount='amount',
    date='date',
    type='type',
    total='total',
    quantity='quantity',
    category='category',
    currency='currency',
)

# common data types
required_integer = {
    'type': 'integer',
    'required': True
}

unique_integer = required_integer.copy()
unique_integer['unique'] = True

required_string = {
    'type': 'string',
    'required': True,
    'empty': False
}
unique_string = required_string.copy()
unique_string['unique'] = True

required_objectid = {
    'type': 'objectid',
    'required': True,
}
required_datetime = {
    'type': 'datetime',
    'required': True
}

required_boolean = {
    'type': 'boolean',
    'required': True,
}

required_float = {
    'type': 'float',
    'required': True
}

to_upper = lambda v: v.upper()  # noqa

# common fields
company = {
    'type': 'objectid',
    'required': True,
    'data_relation': {
        'resource': topology.companies,
        'field': '_id',
    },
}

currency = {
    'type': 'dict',
    'schema': {
        'name': required_string,
        'code': required_string,
        'symbol': {'type': 'string'},
    }
}

address = {
    'type': 'dict',
    'schema': {
        'street': {'type': 'string'},
        'town': {'type': 'string'},
        'state_or_province': {'type': 'string'},
        'country': {'type': 'string'},
        'postal_code': {'type': 'string'},
    }
}

contact_details = {
    'phone': {'type': 'string'},
    'mobile': {'type': 'string'},
    'fax': {'type': 'string'},
    'mail': {'type': 'string'},
    'pec_mail': {'type': 'string'},
    'web_site': {'type': 'string'},
}

address_ex = {
    'type': 'dict',
    'schema': contact_details
}
address_ex['schema'].update(address['schema'])

amount = {'type': 'integer', 'default': 0}

bank = {
    'type': 'dict',
    'required': True,
    'schema': {
        'name': {'type': 'string', 'required': True},
        # TODO switch to coerce to_upper when Cerberus 1.0 is released
        # 'iban': {'type': 'iban', 'coerce': _to_upper},
        'iban': {'type': 'iban'},
        'bic_swift': {'type': 'swift'}
    }
}

# most resources share the following settings
base_def = {
    'auth_field': key.account
}

# most collections share the following schema definition
base_schema = {
    key.company: company,
}
