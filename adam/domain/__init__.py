# -*- coding: utf-8 -*-
"""
    adam.domain
    ~~~~~~~~~~~

    this package exposes the API domain and commonly used settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import accounts
import companies
import contacts
import countries
import documents
import fees
import payment_methods
import payments
import user_accounts
import vat
import warehouses
import sizes
import price_lists
from common import topology
from dashboard import dashboard_accounts, dashboard_documents


DOMAIN = {
    topology.accounts: accounts.definition,
    topology.accounts: user_accounts.definition,
    topology.companies: companies.definition,
    topology.contacts: contacts.definition,
    topology.countries: countries.definition,
    topology.dashboard_accounts: dashboard_accounts.definition,
    topology.dashboard_documents: dashboard_documents.definition,
    topology.documents: documents.definition,
    topology.fees: fees.definition,
    topology.payment_methods: payment_methods.definition,
    topology.payments: payments.definition,
    topology.vat: vat.definition,
    topology.warehouses: warehouses.definition,
    topology.sizes: sizes.definition,
    topology.price_lists: price_lists.definition
}
