#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

from pyk8s.event import Event
class Events(object):
    def __init__(self,**kwargs):
        params = {
            'items':None,
            'creationTimestamp':None,
            'apiVersion':None,
            'resourceVersion':None,
            'kind':None,
            'selfLink':None,
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
            return Events(
                items = [Event.newFromDict(event) for event in data.get('items',{})],
                creationTimestamp=data.get('creationTimestamp', None),
                apiVersion=data.get('apiVersion', None),
                resourceVersion=data.get('resourceVersion', None),
                kind=data.get('kind', None),
                selfLink=data.get('selfLink', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Events(
                itemss = [Events.newFromDict(events) for events in data.get('items',{})],
                creationTimestamp=data.get('creationTimestamp', None),
                apiVersion=data.get('apiVersion', None),
                resourceVersion=data.get('resourceVersion', None),
                kind=data.get('kind', None),
                selfLink=data.get('selfLink', None),
            )

