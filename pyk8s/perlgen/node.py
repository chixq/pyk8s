#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Condition(object):
    def __init__(self,**kwargs):
        params = {
            'kind':None,
            'lastProbeTime':None,
            'status':None,
            'reason':None,
            'lastTransitionTime':None,
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
            return Condition(
                kind=data.get('kind', None),
                lastProbeTime=data.get('lastProbeTime', None),
                status=data.get('status', None),
                reason=data.get('reason', None),
                lastTransitionTime=data.get('lastTransitionTime', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Condition(
                kind=data.get('kind', None),
                lastProbeTime=data.get('lastProbeTime', None),
                status=data.get('status', None),
                reason=data.get('reason', None),
                lastTransitionTime=data.get('lastTransitionTime', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Condition.newFromDict(json_data)
class Status(object):
    def __init__(self,**kwargs):
        params = {
            'conditions':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        i=0
        for condition in self.conditions:
            params['conditions'][i]=condition.toDict();
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
            return Status(
                conditions = [Condition.newFromDict(condition) for condition in (data.get('conditions',{}) if (data.get('conditions',{}) is not None) else {})],
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Status(
                conditions = [Condition.newFromDict(condition) for condition in (data.get('conditions',{}) if (data.get('conditions',{}) is not None) else {})],
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Status.newFromDict(json_data)
class Node(object):
    def __init__(self,**kwargs):
        params = {
            'resourceVersion':None,
            'creationTimestamp':None,
            'status':None,
            'hostIP':None,
            'selfLink':None,
            'apiVersion':None,
            'resources':None,
            'uid':None,
            'id':None,
            'kind':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['status']=self.status.toDict();
        
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
            return Node(
                resourceVersion=data.get('resourceVersion', None),
                creationTimestamp=data.get('creationTimestamp', None),
                status=Status.newFromDict(data.get('status', {})),
                hostIP=data.get('hostIP', None),
                selfLink=data.get('selfLink', None),
                apiVersion=data.get('apiVersion', None),
#                resources=Resources.newFromDict(data.get('resources', {})),
                uid=data.get('uid', None),
                id=data.get('id', None),
                kind=data.get('kind', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Node(
                resourceVersion=data.get('resourceVersion', None),
                creationTimestamp=data.get('creationTimestamp', None),
                status=Status.newFromDict(data.get('status', {})),
                hostIP=data.get('hostIP', None),
                selfLink=data.get('selfLink', None),
                apiVersion=data.get('apiVersion', None),
#                resources=Resources.newFromDict(data.get('resources', {})),
                uid=data.get('uid', None),
                id=data.get('id', None),
                kind=data.get('kind', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Node.newFromDict(json_data)