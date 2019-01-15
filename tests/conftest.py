# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# stdlib imports
import sys
import os
import subprocess
from os.path import dirname, join, normpath, relpath


def find_appengine_sdk():
    gcloud_path = subprocess.check_output('which gcloud', shell=True).strip()
    return normpath(join(gcloud_path, '../../platform/google_appengine'))


def setup_appengine_devenv(sdk_path):
    sys.path.insert(0, sdk_path)

    import dev_appserver
    dev_appserver.fix_sys_path()

    import google.appengine.tools.os_compat     # noqa


def pytest_configure(config):
    """Configures the App Engine SDK imports on py.test startup."""
    sdk_path = os.environ.get('APPENGINE_SDK')
    if sdk_path is None:
        sdk_path = find_appengine_sdk()

    print("\033[32mAppEngine SDK path: \033[33m{}\033[0m".format(sdk_path))

    setup_appengine_devenv(sdk_path)

    # Setup project paths
    import appengine_config     # noqa


def pytest_itemcollected(item):
    """ Prettier test names. """
    name = item.originalname or item.name
    if name.startswith('test_'):
        name = name[5:]

    name = name.replace('_', ' ').strip()
    name = name[0].upper() + name[1:]

    rel_path = relpath(item.fspath.strpath, dirname(item.fspath.dirname))
    item._nodeid = '{location:50} {name}'.format(
        name=name,
        location='{}:{}'.format(rel_path, item.location[1]),
    )
