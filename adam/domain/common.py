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
                         'documents, accounts, contacts')

topology = TopologyKey(
    countries='countries',
    companies='companies',
    contacts='contacts',
    accounts='accounts',
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

# common fields
company = {
    'type': 'objectid',
    'required': True,
    'data_relation': {
        'resource': topology.companies,
        'field': '_id',
    },
}

contact_minimal = {
    'name': required_string,
    'vat': unique_string,
    'address': {'type': 'string'}
}

# most resources share the following settings
base_def = {
    'auth_field': key.account
}

# most collections share the following schema definition
base_schema = {
    key.company: company,
}
