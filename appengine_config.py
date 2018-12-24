# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import vendor
import sys
from os.path import dirname, join

sys.path.insert(0, join(dirname(__file__), 'src'))
vendor.add('third_party/py')
