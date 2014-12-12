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
from dashboard import dashboard_accounts, dashboard_documents
from common import account, account_key  # noqa (will raise W0611 on pyflakes)

DOMAIN = {
    'countries': countries.definition,
    'companies': companies.definition,
    'dashboard-accounts': dashboard_accounts.definition,
    'dashboard-documents': dashboard_documents.definition,
    'accounts': accounts.definition,
}
