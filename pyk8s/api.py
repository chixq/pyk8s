#!/usr/bin/env python
# -.- coding: utf-8 -*-
import requests

from pyk8s import __version__
from pyk8s.endpoints import EndpointMixin
from pyk8s.exceptions import PyK8SAuthError, PyK8SError
from pyk8s.helper import Helper

try:
    import simplejson as json
except ImportError:
    import json


class PyK8S(EndpointMixin, object):
    def __init__(self, user_id=None, user_password=None, headers=None, client_args=None, base_url=None):
        if not user_id or not user_password:
            #raise PyK8SAuthError("user id and password required")
            print "auth not set"
            self.auth=None
        else:
            self.user_id = user_id
            self.user_password = user_password
            self.auth = (user_id, user_password)

        default_headers = {
            'User-Agent': 'PyK8S v' + __version__
        }
        if isinstance(headers, dict):
            default_headers.update(headers)
        self.headers = default_headers

        self.client_args = client_args or {}
        if not base_url:
            raise PyK8SError("base url is empty")
        else:
            self.base_url = base_url

        self.client = requests.Session()


    def get(self, endpoint):
        return self.request(endpoint)

    def post(self, endpoint, params=None):
        return self.request(endpoint, 'POST', params)

    def delete(self, endpoint, params=None):
        return self.request(endpoint, 'DELETE', params)

    def put(self, endpoint, params=None):
        return self.request(endpoint, 'PUT', params)

    def _request(self, url, method='GET', params=None):
        """Internal request method"""
        method = method.lower()
        params = params or {}

        verb_func = getattr(self.client, method)
#         params, _ = Helper._transparent_params(params)
        
        

        requests_args = {}
        if self.auth:
            requests_args['auth'] = self.auth
        for k, v in self.client_args.items():
            # To be added with k8s development
            if k in ('timeout', 'cache', 'verify'):
                requests_args[k] = v

        if method == 'get':
            requests_args['params'] = params
        else:
            requests_args.update({
#                 'data': params,
                  'data': json.dumps(params)
            })

        try:
            response = verb_func(url, **requests_args)
        except requests.RequestException as e:
            raise PyK8SError(str(e))

        # greater than 304 (not modified) is an error
        if response.status_code > 304:
            if response.status_code == 401:
                ExceptionType = PyK8SAuthError
            else:
                ExceptionType = PyK8SError
            raise ExceptionType(response.json, error_code=response.status_code)
        
        print type(response)
        try:
            content = response.json
        except ValueError:
            raise PyK8SError('Response was not valid JSON. \
                               Unable to decode.')

        return content

    def request(self, endpoint, method='GET', params=None, version='v1beta2'):
        endpoint_url = '%s/%s/%s' % (self.base_url, version, endpoint)
        content = self._request(endpoint_url, method=method, params=params)

        return content



