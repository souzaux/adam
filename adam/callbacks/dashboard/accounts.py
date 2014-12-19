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

import adam.domain.accounts as accounts
from adam.domain.dashboard.common import key as months_key
from adam.domain.dashboard.dashboard_accounts import key

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


def accounts_insert(new_accounts):
    """ Accounts have been inserted; update dashboard accordingly """

    for account in new_accounts:
        delta = account[accounts.key.amount]
        _dashboard_update(delta, 1, *_meta(account))


def account_replace(new, original):
    """ Account has been replaced; update dashboard accordingly """

    delta = new[accounts.key.amount] - original[accounts.key.amount]
    _dashboard_update(delta, 0, *_meta(new))


def account_delete(account):
    """ Document has been deleted; update dashboard accordingly """

    delta = account[accounts.key.amount] * -1
    _dashboard_update(delta, -1, *_meta(account))


def _meta(account):
    """ Return document date and company """
    return account[accounts.key.date], account[accounts.key.company], \
        account[accounts.key.type]


def _dashboard_update(delta, quantity, date, company, type):
    """ Updates a documents dashboard """

    year, month = date.year, date.month-1
    lookup = {key.company: company, key.year: year}

    array = empty_month_series()
    empty = {
        key.year: year,
        key.payable: {
            key.debit_due: 0,
            key.month_series: array
        },
        key.receivable: {
            key.credit_due: 0,
            key.month_series: array
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
    due = '%s.%s' % (type, key.credit_due
                     if type == key.receivable else key.debit_due)

    item = '%s.%s.%d' % (type, key.month_series, month)
    amount_item = '%s.%s' % (item, months_key.amount)
    quantity_item = '%s.%s' % (item, months_key.quantity)

    bulk.find(lookup).update({'$inc': {due: delta, amount_item: delta,
                                       quantity_item: quantity}})
    r = bulk.execute()

    # TODO remove or log?
    if app.config['DEBUG'] is True:
        from pprint import pprint
        pprint(r)
