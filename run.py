# -*- coding: utf-8 -*-

from eve import Eve
from eve.auth import BasicAuth


class Auth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource):
        return username == 'admin' and password == 'secret'


app = Eve(auth=Auth)

if __name__ == '__main__':
    app = Eve()
    app.run(host='0.0.0.0', port=5000)
