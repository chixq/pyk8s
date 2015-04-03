#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PyK8SError(Exception):

    def __init__(self, msg, error_code=None, retry_after=None):
        self.error_code = error_code
        if error_code in K8S_HTTP_STATUS_CODE:
            msg = 'Kubernetes API returns %s (%s), %s' % (error_code, K8S_HTTP_STATUS_CODE[error_code][0], msg)

        super(PyK8SError, self).__init__(msg)

    @property
    def msg(self):
        return self.args[0]

class PyK8SAuthError(PyK8SError):
    pass

class PyK8SResourceLimitedError(PyK8SError):

    def __init__(self):
        msg = 'Not enough resource offers'
        super(PyK8SResourceLimitedError, self).__init__(msg)




# Refer to https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/api-conventions.md#http-status-codes
K8S_HTTP_STATUS_CODE = {
    200: ('OK', 'Request completed successfully!'),
    201: ('Created', 'Rquest to create kind completed successfully.'),
    204: ('NoContent', 'Rquest completed successfully, and the response contains no body.'),

    307: ('TemporaryRedirect','Address for the requested resource has changed.'),
    400: ('Bad Request', 'Requested is invalid. Do not retry. Fix the request'),
    401: ('Unauthorized', 'Authentication credentials were missing \
          or incorrect.'),
    403: ('Forbidden', 'The request is understood, but it has been \
          refused. An accompanying error message will explain why. \
          This code is used when requests are being denied due to \
          update limits.'),
    404: ('Not Found', 'The URI requested is invalid or the resource \
          requested does not exists.'),
    405: ('MethodNotAllowed', 'Action the client attempted to perform on the resource was not supported by the code.'),
    409: ('Conflict', ' either the resource the client attempted to create already exists or\
          the requested update operation cannot be completed due to a conflict.'),
    422: ('UnprocessableEntity', 'Requested create or update operation cannot be completed \
          due to invalid data provided as part of the request.'),
    429: ('Too Many Requests', 'Either the client rate limit has been exceeded or \
          the server has received more requests then it can process.'),
    500: ('Internal Server Error', 'Kubernetes API server internal Error'),
    502: ('Bad Gateway', 'Kubernetes  API server is down or being upgraded.'),
    503: ('Service Unavailable', 'Kubernetes API server are up, but overloaded \
          with requests. Try again later.'),
    504: ('Gateway Timeout', 'Kubernetes API server are up, but the request \
          couldn\'t be serviced during given timeout.'),
}
