# -*- coding: utf-8 -*-
"""
    adam.run.py
    ~~~~~~~~~~~

    The API launch script.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from eve import Eve
from eve.auth import BasicAuth
import os


class Auth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource):
        user = os.environ.get('AUTH_USERNAME')
        pw = os.environ.get('AUTH_PASSWORD')
        return username == user and password == pw


app = Eve(auth=Auth)

if __name__ == '__main__':
    # Heroku defines a $PORT environment variable, which we use to determine
    # if we're running locally or not.
    host = '0.0.0.0' if os.environ.get('PORT') else None
    app.run(host=host, port=int(os.environ.get('PORT', 5000)))
