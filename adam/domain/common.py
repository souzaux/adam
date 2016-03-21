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
                         'payment_options')

topology = TopologyKey(
    countries='countries',
    companies='companies',
    contacts='contacts',
    accounts='accounts',
    vat='vat',
    payment_options='payment-options',
    documents='documents',
    dashboard_accounts='dashboard-accounts',
    dashboard_documents='dashboard-documents'
)


SchemaKey = namedtuple('SchemaKey', 'company, account, amount, date, type, ' +
                       'total, quantity')
key = SchemaKey(
    company='company_id',
    account='account',
    amount='amount',
    date='date',
    type='type',
    total='total',
    quantity='quantity'
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
        'name': {'type': 'string'},
        'code': {'type': 'string'},
        'symbol': {'type': 'string'}
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

address_ex = {
    'type': 'dict',
    'schema': {
        'phone': {'type': 'string'},
        'mobile': {'type': 'string'},
        'fax': {'type': 'string'},
        'mail': {'type': 'string'},
        'pec_mail': {'type': 'string'},
        'web_site': {'type': 'string'},
    }
}
address_ex['schema'].update(address['schema'])

contact_minimal = {
    'name': required_string,
    'vat_id_number': {'type': 'vat'},
    'tax_id_number': {'type': 'tax_id_number'},
}
contact_minimal.update(address['schema'])

# most resources share the following settings
base_def = {
    'auth_field': key.account
}

# most collections share the following schema definition
base_schema = {
    key.company: company,
}
