#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

from pyk8s.replicationcontroller import Replicationcontroller
class Replicationcontrollers(object):
    def __init__(self,**kwargs):
        params = {
            'apiVersion':None,
            'selfLink':None,
            'resourceVersion':None,
            'items':None,
            'kind':None,
            'creationTimestamp':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        i=0
        for item in self.items:
            params['items'][i]=item.toDict();
            i=i+1;
        
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
            return Replicationcontrollers(
                apiVersion=data.get('apiVersion', None),
                selfLink=data.get('selfLink', None),
                resourceVersion=data.get('resourceVersion', None),
                items = [Replicationcontroller.newFromDict(item) for item in (data.get('items',{}) if (data.get('items',{}) is not None) else {})],
                kind=data.get('kind', None),
                creationTimestamp=data.get('creationTimestamp', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontrollers(
                apiVersion=data.get('apiVersion', None),
                selfLink=data.get('selfLink', None),
                resourceVersion=data.get('resourceVersion', None),
                items = [Replicationcontrollers.newFromDict(item) for item in (data.get('items',{}) if (data.get('items',{}) is not None) else {})],
                kind=data.get('kind', None),
                creationTimestamp=data.get('creationTimestamp', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontrollers.newFromDict(json_data)