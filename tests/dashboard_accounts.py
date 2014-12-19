# -*- coding: utf-8 -*-
"""
    adam.tests.dashboard-accounts.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test that the accounts dashboard is properly initialized and updated
    as accounts are added, edited and deleted.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""

import copy

from . import TestBase

from adam.domain import accounts as accounts
from adam.domain import dashboard_accounts as dbaccounts
from adam.domain.dashboard.common import key as month


class TestDashboardAccounts(TestBase):
    def setUp(self):
        super(TestDashboardAccounts, self).setUp()

        self.account_payable = {
            accounts.key.date: "Tue, 16 Dec 2014 13:53:14 GMT",
            accounts.key.amount: 1000,
            accounts.key.type: accounts.key.payable,
            accounts.key.company: self.company_id
        }

        self.account_receivable = copy.copy(self.account_payable)
        self.account_receivable[accounts.key.type] = accounts.key.receivable
        self.account_receivable[accounts.key.date] = \
            "Wed, 05 Nov 2014 13:53:14 GMT"

    def _post_one_account(self, account):
        doc, status = self.post(accounts.url, account)
        self.assert201(status)
        return account

    def test_dashboard_accounts_post(self):
        # dashboard is empty
        r, status = self.get(dbaccounts.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 0)

        self._post_one_account(self.account_payable)
        r, status = self.get(dbaccounts.url)
        self.assert200(status)
        # one item in the dashboard now
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        payable = item[dbaccounts.key.payable]
        dec = payable[dbaccounts.key.month_series][11]

        # year is 2014
        self.assertEqual(item[dbaccounts.key.year], 2014)
        # debit due has been updated
        self.assertEqual(payable[dbaccounts.key.debit_due], 1000)
        # 12th item (Dec) of the invoices array has been initialized to 1000,1
        self.assertEqual(dec[month.amount], 1000)
        self.assertEqual(dec[month.quantity], 1)

        self._post_one_account(self.account_payable)
        r, status = self.get(dbaccounts.url)
        self.assert200(status)
        # dashboard has still 1 item
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        payable = item[dbaccounts.key.payable]
        dec = payable[dbaccounts.key.month_series][11]

        # debit due has been updated
        self.assertEqual(payable[dbaccounts.key.debit_due], 2000)
        # but now we got 2 docs in dec, for a total of 2k
        self.assertEqual(dec[month.amount], 2000)
        self.assertEqual(dec[month.quantity], 2)

        # post one order now
        self._post_one_account(self.account_receivable)

        r, status = self.get(dbaccounts.url)
        self.assert200(status)

        # dashboard has still 1 item
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        receivable = item[dbaccounts.key.receivable]
        dec = payable[dbaccounts.key.month_series][11]
        nov = receivable[dbaccounts.key.month_series][10]

        # credit due has been increased
        self.assertEqual(receivable[dbaccounts.key.credit_due], 1000)
        # orders stats have been updated (Nov. month slot)
        self.assertEqual(nov[month.amount], 1000)
        self.assertEqual(nov[month.quantity], 1)

        # debit due has not been updated
        self.assertEqual(payable[dbaccounts.key.debit_due], 2000)
        self.assertEqual(dec[month.amount], 2000)
        self.assertEqual(dec[month.quantity], 2)
