# -*- coding: utf-8 -*-
"""
    adam.run.py
    ~~~~~~~~~~~

    The API launch script.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os
import sys
from eve import Eve
from adam.oauth2 import BearerAuth
from adam.callbacks.dashboard import dashboard


# Load the settings file using a robust path so it works when
# the script is imported from the test suite.
this_directory = os.path.dirname(os.path.realpath(__file__))
settings_file = os.path.join(this_directory, 'settings.py')

port = os.environ.get('PORT')
if port:
    # Heroku
    host = '0.0.0.0'
    port = int(port)
else:
    host = '127.0.0.1'
    port = 5000


app = Eve(auth=None if 'noauth' in sys.argv else BearerAuth,
          settings=settings_file)

# Attach callbacks event hooks.
dashboard.init(app)

if __name__ == '__main__':
    app.run(host=host, port=port)
