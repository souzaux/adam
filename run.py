# -*- coding: utf-8 -*-

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
    # Heroku support: bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    app = Eve()
    app.run(host='0.0.0.0', port=port)
