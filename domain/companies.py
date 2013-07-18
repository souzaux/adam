# -*- coding: utf-8 -*-
"""
    adam.domain.companies.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'companies' resource and schema settings.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import common


_schema = {
    # company id ('id')
    common.companyid_key: common.integer,
    common.account['key']: common.account['definition'],
    # name
    'n': {
        'type': 'string',
        'required': True,
    },
    'pw': {
        'type': 'string',
    },
}

definition = {
    'url': 'companies',
    'item_title': 'company',
    'additional_lookup': common.company_lookup,
    'schema': _schema,
}
definition.update(common.base)
