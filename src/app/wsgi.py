"""Main application entry point."""
from __future__ import absolute_import

import app.base.api_fixer       # pylint: disable=unused-import

# 3rd party imports
import webapp2

# local imports
from .routes import ROUTES
from .config import CONFIG
from .base import constants


# pylint: disable=invalid-name
app = webapp2.WSGIApplication(
    routes=ROUTES,
    debug=constants.DEBUG,
    config=CONFIG
)
