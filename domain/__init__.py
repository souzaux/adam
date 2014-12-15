# -*- coding: utf-8 -*-
"""
    adam.domain
    ~~~~~~~~~~~

    this package exposes the API domain and commonly used settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import countries
import companies
import accounts
import documents
from dashboard import dashboard_accounts, dashboard_documents

DOMAIN = {
    'countries': countries.definition,
    'companies': companies.definition,
    'dashboard-accounts': dashboard_accounts.definition,
    'dashboard-documents': dashboard_documents.definition,
    'accounts': accounts.definition,
    'documents': documents.definition,
}
