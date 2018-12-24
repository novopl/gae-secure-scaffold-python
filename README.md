# Secure GAE Scaffold

## Introduction
----
Please note: this is not an official Google product.

This contains a boilerplate AppEngine application meant to provide a secure
base on which to build additional functionality.  Structure:

* / - top level directory for common files, e.g. app.yaml
* /src - directory for all source code
* /static - directory for static content
* /templates - directory for Django/Jinja2 templates your app renders.

The scaffold provides the following basic security guarantees by default through
a set of base classes found in `src/base/handlers.py`.  These handlers:

1. Set assorted security headers (Strict-Transport-Security, X-Frame-Options,
   X-XSS-Protection, X-Content-Type-Options, Content-Security-Policy) with
   strong default values to help avoid attacks like Cross-Site Scripting (XSS)
   and Cross-Site Script Inclusion.  See  `_SetCommonResponseHeaders()` and
   `SetAjaxResponseHeaders()`.
1. Prevent the XSS-prone construction of HTML via string concatenation by
   forcing the use of a template system (Django/Jinja2 supported).  The
   template systems have non-contextual autoescaping enabled by default.
   See the `render()`, `render_json()` methods in `BaseHandler` and
   `BaseAjaxHandler`. For contextual autoescaping, you should use Closure
   Templates in strict mode (<https://developers.google.com/closure/templates/docs/security>).
1. Test for the presence of headers that guarantee requests to Cron or
   Task endpoints are made by the AppEngine serving environment or an
   application administrator.  See the `dispatch()` method in `BaseCronHandler`
   and `BaseTaskHandler`.
1. Verify XSRF tokens by default on authenticated requests using any verb other
   that GET, HEAD, or OPTIONS.  See the `_RequestContainsValidXsrfToken()`
   method for more information.

In addition to the protections above, the scaffold monkey patches assorted APIs
that use insecure or dangerous defaults (see `src/base/api_fixer.py`).

Obviously no framework is perfect, and the flexibility of Python offers many
ways for a motivated developer to circumvent the protections offered.  Under
the assumption that developers are not malicious, using the scaffold should
centralize many security mechanisms, provide safe defaults, and structure the
code in a way that facilitates security review.

Sample implementations can be found in `src/handlers.py`.  These demonstrate
basic functionality, and should be removed / replaced by code specific to
your application.


## Setting up project

### Setup virtualenv for local packages

All packages required for deployment should live in the `third_party` directory.
This does not include the packages that are required for development. We do not
want to deploy them to AppEngine so we use a virtualenv to install them locally:

```bash
$ virtualenv -p python2 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

### Running tests

The scaffold uses **py.test** to as a test runner. To run tests use one of the
following commands

```bash
$ pytest -c ops/tools/pytest.ini tests          # Run all tests
$ pytest -c ops/tools/pytest.ini tests/google   # Run tests written by google
```
