# -*- coding: utf-8 -*-
"""
    adam.domain.document_item.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'document_item' schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import variation
from vat import vat_field
from warehouses import warehouse_field


detail = {
    'type': 'dict',
    'schema': {
        'sku': {'type': 'string'},
        'description': {'type': 'string'},
        'color': {'type': 'string'},
        'unit_of_measure': {'type': 'string'},
        'notes': {'type': 'string'},
        'serial_number': {'type': 'string'},
        'lot': {
            'type': 'dict',
            'schema': {
                'number': {'type': 'string'},
                'date': {'type': 'datetime'},
                'expiration': {'type': 'datetime'},
            }
        },
        'size': {
            'type': 'dict',
            'schema': {
                'number': {'type': 'string'},
                'name': {'type': 'string'},
            }
        },
    }
}

item = {
    'type': 'dict',
    'schema': {
        'guid': {'type': 'string'},
        'quantity': {'type': 'float'},
        'processed_quantity': {'type': 'float'},
        'price': {'type': 'integer'},
        'net_price': {'type': 'integer'},
        'price_vat_inclusive': {'type': 'integer'},
        'total': {'type': 'integer'},
        'withholding_tax': {'type': 'boolean'},
        'commission': {'type': 'float'},
        'area_manager_commission': {'type': 'float'},
        'detail': detail,
        'vat': vat_field,
        'price_list': {'type': 'string'},
        'warehouse': warehouse_field,
        'variation_collection': variation,
    }
}
