# -*- coding: utf-8 -*-
"""
    adam.domain.countries.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'countries' resource and schema settings.

    :copyright: (c) 2014 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import required_string

_schema = {
    'n': required_string,                       # name
}

definition = {
    'url': 'countries',
    'item_title': 'country',
    'schema': _schema,
}
