#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

from pyk8s.limitRange import LimitRange
class LimitRanges(object):
    def __init__(self,**kwargs):
        params = {
            'items':None,
            'selfLink':None,
            'resourceVersion':None,
            'creationTimestamp':None,
            'kind':None,
            'apiVersion':None,
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
            return LimitRanges(
                items = [LimitRange.newFromDict(item) for item in (data.get('items',{}) if (data.get('items',{}) is not None) else {})],
                selfLink=data.get('selfLink', None),
                resourceVersion=data.get('resourceVersion', None),
                creationTimestamp=data.get('creationTimestamp', None),
                kind=data.get('kind', None),
                apiVersion=data.get('apiVersion', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return LimitRanges(
                items = [LimitRanges.newFromDict(item) for item in (data.get('items',{}) if (data.get('items',{}) is not None) else {})],
                selfLink=data.get('selfLink', None),
                resourceVersion=data.get('resourceVersion', None),
                creationTimestamp=data.get('creationTimestamp', None),
                kind=data.get('kind', None),
                apiVersion=data.get('apiVersion', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return LimitRanges.newFromDict(json_data)