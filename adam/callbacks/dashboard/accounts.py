# -*- coding: utf-8 -*-
"""
    callbacks.dashboard.accounts.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Accounts (payable and receivables) dashboard.

    This module updates the dashboard each time an account receivable or
    payable is added, updated or deleted.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from flask import current_app as app

from adam.domain.common import company_key
from adam.domain.accounts import date_key, type_key, payable_key, \
    receivable_key
from adam.domain.dashboard.common import year_key, quantity_key, amount_key
from adam.domain.dashboard.dashboard_accounts import debit_due_key, \
    credit_due_key, month_series_key

from adam.callbacks.common import auth, empty_month_series

import datetime  # noqa

""" IMPORTANT

    Since the dashboard is supposed to be readonly for the clients and we
    also want to strive for best performance since it will be updated
    frequently, we choose to udpate it out-of-band (not via internal Eve
    methods like 'post_internal').

    Side effect is that some meta fields like _updated and _created are
    not going to be reliable (_etag will be computed by eve on the fly
    since missing).
"""


def accounts_insert(accounts):
    """ Accounts have been inserted; update dashboard accordingly """

    for account in accounts:
        delta = account[amount_key]
        _dashboard_update(delta, 1, *_meta(account))


def account_replace(new, original):
    """ Account has been replaced; update dashboard accordingly """

    delta = new[amount_key] - original[amount_key]
    _dashboard_update(delta, 0, *_meta(new))


def account_delete(account):
    """ Document has been deleted; update dashboard accordingly """

    delta = account[amount_key] * -1
    _dashboard_update(delta, -1, *_meta(account))


def _meta(account):
    """ Return document date and company """
    return account[date_key], account[company_key], account[type_key]


def _dashboard_update(delta, quantity, date, company, type):
    """ Updates a documents dashboard """

    year, month = date.year, date.month-1
    lookup = {company_key: company, year_key: year}

    array = empty_month_series()
    empty = {
        year_key: year,
        payable_key: {
            debit_due_key: 0,
            month_series_key: array
        },
        receivable_key: {
            credit_due_key: 0,
            month_series_key: array
        }
    }

    auth_field, auth_value = auth('accounts')
    if auth_value:
        empty.update({auth_field: auth_value})

    dashboard = app.data.driver.db['dashboard_accounts']

    bulk = dashboard.initialize_ordered_bulk_op()

    # add dashboard if needed
    bulk.find(lookup).upsert().update({'$setOnInsert': empty})

    # update dashboard
    due = '%s.%s' % (type, credit_due_key
                     if type == receivable_key else debit_due_key)

    item = '%s.%s.%d' % (type, month_series_key, month)
    amount_item = '%s.%s' % (item, amount_key)
    quantity_item = '%s.%s' % (item, quantity_key)

    bulk.find(lookup).update({'$inc': {due: delta, amount_item: delta,
                                       quantity_item: quantity}})
    r = bulk.execute()

    # TODO remove or log?
    if app.config['DEBUG'] is True:
        from pprint import pprint
        pprint(r)
