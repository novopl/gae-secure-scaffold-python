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

The scaffold is using **peltak** for projects scripts to help out with daily
repetitive dev tasks. If you do not wish to use peltak, after you clone the
scaffold just delete `pelconf.yaml` file and remove `peltak==0.24.2` from
`requirements.txt`.


### Setup virtualenv for local packages

All packages required for deployment should live in the `third_party` directory.
This does not include the packages that are required for development. We do not
want to deploy them to AppEngine so we use a virtualenv to install them locally:

```bash
$ virtualenv -p python2 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

### Enable peltak autocompletion (if using peltak).

You can enable autocompletion for peltak in the current shell with:

```bash
$ eval "$(_PELTAK_COMPLETE=source peltak)"          # If you're using Bash
$ eval "$(_PELTAK_COMPLETE=source_zsh peltak)"      # If you're using ZSH
```

You can auto-enable completion every time you activate the virtualenv with:

```bash
$ echo 'eval "$(_PELTAK_COMPLETE=source peltak)"' >> .venv/bin/activate
```


### Running tests

The scaffold uses **py.test** to as a test runner. To run tests use one of the
following commands

```bash
$ peltak test
```

### Running code checks

```bash
$ peltak lint
```


## Differences between the upstream version

Each change was done in a separate commit so they are easy to track.

### Fixes

- Fix tests that used functionality deprecated in python2.6

### Changes

- Remove frontend code. The decision on how to build the frontend can be made
  on a per project basis, not in a scaffold shared across all of them.
- The old build that copied all files to `out/` directory has been deleted in
  the previous commit. Use `appengine_config.py` to setup the paths and not
  require that whole copy on build approach.
- Move all tests provided with the scaffold to `tests/google`
- Move all templates to `src/templates`
- Move all app source code to `src/app`
- Use py.test to run tests.
- Moved the examples templates to a dedicated `templates/scaffold_examples/`
  directory
- Change the abstract method names for authenticated handlers from
  `DenyAccess`/`XsrfFail` to `deny_access`/`xsrf_fail`. This was done so that
  linting against PEP8 can be enabled for the project. The scaffold base code
  has been excluded from linting since it’s too far from being compliant and
  changing it would introduce too much work during security review).
- `RootHandler` now renders the examples index.html file instead of redirecting
  to it. This is just so we can avoid redirects and remove static/ directory
  from the scaffold (it’s up to the project how it organizes the static files
  since the frontend is defined entirely by the project)
- Added docker integration. You can use the provided makefile to run the app
  with docker (unify dev environments). To get the list of available commands,
  run `make help`.
