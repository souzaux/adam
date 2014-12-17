# -*- coding: utf-8 -*-
"""
    callbacks.common.py
    ~~~~~~~~~~~~~~~~~~~

    Common methods used by callback functions.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from flask import current_app as app

from adam.domain.dashboard.common import amount_key, quantity_key


def auth(resource):
    """ Return current app's auth_field and auth_value """
    resource_def = app.config['DOMAIN'][resource]
    auth = resource_def['authentication']
    auth_field = resource_def['auth_field']
    auth_value = auth.get_request_auth_value() if auth and auth_field else None
    return auth_field, auth_value


def empty_month_series():
    """ Return an empty month series for the dashboards """
    return [{amount_key: 0, quantity_key: 0} for k in range(12)]
