#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

try:
    import simplejson as json
except ImportError:
    import json

if is_py2:
    str = unicode
    basestring = basestring
    numeric_types = (int, long, float)


elif is_py3:
    str = str
    basestring = (str, bytes)
    numeric_types = (int, float)


class Helper(object):

    @staticmethod
    def _transparent_params(_params):
        params = {}
        files = {}
        for k, v in _params.items():
            if hasattr(v, 'read') and callable(v.read):
                files[k] = v
            elif isinstance(v, bool):
                if v:
                    params[k] = 'true'
                else:
                    params[k] = 'false'
            elif isinstance(v, basestring) or isinstance(v, numeric_types):
                params[k] = v
            elif isinstance(v, list):
                try:
                    params[k] = ','.join(v)
                except TypeError:
                    params[k] = ','.join(map(str, v))
            else:
                continue
        return params, files