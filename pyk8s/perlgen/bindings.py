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
            'podID':None,
            'resourceVersion':None,
            'selfLink':None,
            'host':None,
            'generateName':None,
            'namespace':None,
            'creationTimestamp':None,
            'uid':None,
            'annotations':None,
            'kind':None,
            'id':None,
            'apiVersion':None,
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
                podID=data.get('podID', None),
                resourceVersion=data.get('resourceVersion', None),
                selfLink=data.get('selfLink', None),
                host=data.get('host', None),
                generateName=data.get('generateName', None),
                namespace=data.get('namespace', None),
                creationTimestamp=data.get('creationTimestamp', None),
                uid=data.get('uid', None),
                annotations=data.get('annotations', None),
                kind=data.get('kind', None),
                id=data.get('id', None),
                apiVersion=data.get('apiVersion', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Bindings(
                podID=data.get('podID', None),
                resourceVersion=data.get('resourceVersion', None),
                selfLink=data.get('selfLink', None),
                host=data.get('host', None),
                generateName=data.get('generateName', None),
                namespace=data.get('namespace', None),
                creationTimestamp=data.get('creationTimestamp', None),
                uid=data.get('uid', None),
                annotations=data.get('annotations', None),
                kind=data.get('kind', None),
                id=data.get('id', None),
                apiVersion=data.get('apiVersion', None),
            )

