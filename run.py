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
from adam.auth import Auth
from adam.callbacks.dashboard import dashboard

# Load the settings file using a robust path so it works when
# the script is imported from the test suite.
this_directory = os.path.dirname(os.path.realpath(__file__))
settings_file = os.path.join(this_directory, 'settings.py')

port = os.environ.get('PORT')
if port:
    # Heroku
    auth = Auth
    host = '0.0.0.0'
    port = int(port)
else:
    # no auth when running in local for test purposes
    auth = None
    host = '127.0.0.1'
    port = 5000

app = Eve(auth=auth, settings=settings_file)

# Attach callbacks event hooks.
dashboard.init(app)

if __name__ == '__main__':
    app.run(host=host, port=port)
