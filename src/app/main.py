# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
"""Main application entry point."""
from __future__ import absolute_import

import app.base.api_fixer       # pylint: disable=unused-import

# 3rd party imports
import webapp2

# local imports
from app import handlers
from app.base import constants
from app.examples import example_handlers
from .config import CONFIG


# These should all inherit from base.handlers.BaseHandler
_UNAUTHENTICATED_ROUTES = [
    ('/', handlers.RootHandler),
    ('/examples/xss', example_handlers.JinjaXssHandler),
    ('/examples/csp', example_handlers.CspHandler),
    ('/examples/xssi', example_handlers.XssiHandler),
]

# These should all inherit from base.handlers.BaseAjaxHandler
_UNAUTHENTICATED_AJAX_ROUTES = [
    ('/csp', handlers.CspHandler),
]

# These should all inherit from base.handlers.AuthenticatedHandler
_USER_ROUTES = [
    ('/examples/xsrf', example_handlers.XsrfHandler),
]

# These should all inherit from base.handlers.AuthenticatedAjaxHandler
_AJAX_ROUTES = []

# These should all inherit from base.handlers.AdminHandler
_ADMIN_ROUTES = []

# These should all inherit from base.handlers.AdminAjaxHandler
_ADMIN_AJAX_ROUTES = []

# These should all inherit from base.handlers.BaseCronHandler
_CRON_ROUTES = []

# These should all inherit from base.handlers.BaseTaskHandler
_TASK_ROUTES = []


#################################
# DO NOT MODIFY BELOW THIS LINE #
#################################

# pylint: disable=invalid-name
app = webapp2.WSGIApplication(
    routes=(_UNAUTHENTICATED_ROUTES + _UNAUTHENTICATED_AJAX_ROUTES +
            _USER_ROUTES + _AJAX_ROUTES + _ADMIN_ROUTES + _ADMIN_AJAX_ROUTES +
            _CRON_ROUTES + _TASK_ROUTES),
    debug=constants.DEBUG,
    config=CONFIG)
