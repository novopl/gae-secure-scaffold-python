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
""" A starting point for defining project route handlers. """
import json
import logging

from base import handlers


# Minimal set of handlers to let you display main page with examples
class RootHandler(handlers.BaseHandler):
    """ Main handler serving the root URL. """

    def get(self):
        """ Just redirect to /static/index.html """
        self.render('scaffold_examples/index.html')


class CspHandler(handlers.BaseAjaxHandler):
    """ Handle CSP violations. """

    def post(self):
        """ Log CSP violations to the console. """
        try:
            report = json.loads(self.request.body)
            logging.warn('CSP Violation: {}'.format(
                json.dumps(report['csp-report'])
            ))
            self.render_json({})
        except:
            self.render_json({'error': 'invalid CSP report'})
