#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

# from pyk8s.binding import Binding
class Bindings(object):
    def __init__(self,**kwargs):
        params = {
            'apiVersion':None,
            'uid':None,
            'host':None,
            'creationTimestamp':None,
            'kind':None,
            'podID':None,
            'resourceVersion':None,
            'annotations':None,
            'namespace':None,
            'selfLink':None,
            'id':None,
            'generateName':None,
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
                apiVersion=data.get('apiVersion', None),
                uid=data.get('uid', None),
                host=data.get('host', None),
                creationTimestamp=data.get('creationTimestamp', None),
                kind=data.get('kind', None),
                podID=data.get('podID', None),
                resourceVersion=data.get('resourceVersion', None),
                annotations=data.get('annotations', None),
                namespace=data.get('namespace', None),
                selfLink=data.get('selfLink', None),
                id=data.get('id', None),
                generateName=data.get('generateName', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Bindings(
                apiVersion=data.get('apiVersion', None),
                uid=data.get('uid', None),
                host=data.get('host', None),
                creationTimestamp=data.get('creationTimestamp', None),
                kind=data.get('kind', None),
                podID=data.get('podID', None),
                resourceVersion=data.get('resourceVersion', None),
                annotations=data.get('annotations', None),
                namespace=data.get('namespace', None),
                selfLink=data.get('selfLink', None),
                id=data.get('id', None),
                generateName=data.get('generateName', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Bindings.newFromDict(json_data)