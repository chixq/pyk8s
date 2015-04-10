#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

from pyk8s.binding import Binding
class Bindings(object):
    def __init__(self,**kwargs):
        params = {
            'host':None,
            'selfLink':None,
            'uid':None,
            'namespace':None,
            'creationTimestamp':None,
            'kind':None,
            'apiVersion':None,
            'annotations':None,
            'generateName':None,
            'podID':None,
            'id':None,
            'resourceVersion':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        
        return params

    def toJson(self):
        return json.dumps(self.toDict(), sort_keys=True)

    @staticmethod
    def newFromDict(data):
        if data is None:
            data = {}

        if not isinstance(data, dict):
            raise PyK8SError('Type dict required')
        else:
            return Bindings(
                host=data.get('host', None),
                selfLink=data.get('selfLink', None),
                uid=data.get('uid', None),
                namespace=data.get('namespace', None),
                creationTimestamp=data.get('creationTimestamp', None),
                kind=data.get('kind', None),
                apiVersion=data.get('apiVersion', None),
                annotations=data.get('annotations', None),
                generateName=data.get('generateName', None),
                podID=data.get('podID', None),
                id=data.get('id', None),
                resourceVersion=data.get('resourceVersion', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Bindings(
                host=data.get('host', None),
                selfLink=data.get('selfLink', None),
                uid=data.get('uid', None),
                namespace=data.get('namespace', None),
                creationTimestamp=data.get('creationTimestamp', None),
                kind=data.get('kind', None),
                apiVersion=data.get('apiVersion', None),
                annotations=data.get('annotations', None),
                generateName=data.get('generateName', None),
                podID=data.get('podID', None),
                id=data.get('id', None),
                resourceVersion=data.get('resourceVersion', None),
            )

