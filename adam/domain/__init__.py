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
import countries
import documents
import user_accounts
from common import topology
from dashboard import dashboard_accounts, dashboard_documents


DOMAIN = {
    topology.countries: countries.definition,
    topology.companies: companies.definition,
    topology.dashboard_accounts: dashboard_accounts.definition,
    topology.dashboard_documents: dashboard_documents.definition,
    topology.accounts: user_accounts.definition,
    topology.documents: documents.definition,
    topology.accounts: accounts.definition,
}
