# -*- coding: utf-8 -*-
"""
    adam.domain
    ~~~~~~~~~~~

    this package exposes the API domain and commonly used settings.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import companies
import dashboard
import accounts
from common import account, account_key  # noqa (will raise W0611 on pyflakes)

DOMAIN = {
    'companies': companies.definition,
    'dashboard': dashboard.definition,
    'accounts': accounts.definition,
}
