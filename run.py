# -*- coding: utf-8 -*-
"""
    adam.run.py
    ~~~~~~~~~~~

    The API launch script.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os

from eve import Eve

from auth import Auth
from dashboard import dashboard_insert, dashboard_delete, dashboard_replace


app = Eve(auth=Auth)

app.on_inserted += dashboard_insert
app.on_replaced += dashboard_replace
app.on_deleted_item += dashboard_delete

# Heroku defines a $PORT environment variable that we use to determine
# if we're running locally or not.
port = os.environ.get('PORT')
if port:
    host = '0.0.0.0'
    port = int(port)
else:
    host = '127.0.0.1'
    port = 5000

if __name__ == '__main__':
    app.run(host=host, port=port)
