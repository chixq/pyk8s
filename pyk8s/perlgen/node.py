#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Node(object):
    def __init__(self,**kwargs):
        params = {
            'id':None,
            'creationTimestamp':None,
            'uid':None,
            'hostIP':None,
            'kind':None,
            'selfLink':None,
            'resources':None,
            'apiVersion':None,
            'status':None,
            'resourceVersion':None,
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
                id=data.get('id', None),
                creationTimestamp=data.get('creationTimestamp', None),
                uid=data.get('uid', None),
                hostIP=data.get('hostIP', None),
                kind=data.get('kind', None),
                selfLink=data.get('selfLink', None),
#                resources=Resources.newFromDict(data.get('resources', {})),
                apiVersion=data.get('apiVersion', None),
                status=Status.newFromDict(data.get('status', {})),
                resourceVersion=data.get('resourceVersion', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Node(
                id=data.get('id', None),
                creationTimestamp=data.get('creationTimestamp', None),
                uid=data.get('uid', None),
                hostIP=data.get('hostIP', None),
                kind=data.get('kind', None),
                selfLink=data.get('selfLink', None),
#                resources=Resources.newFromDict(data.get('resources', {})),
                apiVersion=data.get('apiVersion', None),
                status=Status.newFromDict(data.get('status', {})),
                resourceVersion=data.get('resourceVersion', None),
            )


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
                conditions = [Condition.newFromDict(condition) for condition in data.get('conditions',{})],
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Status(
                conditionss = [Condition.newFromDict(condition) for condition in data.get('conditions',{})],
            )


class Condition(object):
    def __init__(self,**kwargs):
        params = {
            'status':None,
            'lastProbeTime':None,
            'kind':None,
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
                status=data.get('status', None),
                lastProbeTime=data.get('lastProbeTime', None),
                kind=data.get('kind', None),
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
                status=data.get('status', None),
                lastProbeTime=data.get('lastProbeTime', None),
                kind=data.get('kind', None),
                reason=data.get('reason', None),
                lastTransitionTime=data.get('lastTransitionTime', None),
            )

