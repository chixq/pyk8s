#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Node_status_condition(object):
    def __init__(self,**kwargs):
        params = {
            'lastProbeTime':None,
            'reason':None,
            'lastTransitionTime':None,
            'status':None,
            'kind':None,
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
            return Node_status_condition(
                lastProbeTime=data.get('lastProbeTime', None),
                reason=data.get('reason', None),
                lastTransitionTime=data.get('lastTransitionTime', None),
                status=data.get('status', None),
                kind=data.get('kind', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Node_status_condition(
                lastProbeTime=data.get('lastProbeTime', None),
                reason=data.get('reason', None),
                lastTransitionTime=data.get('lastTransitionTime', None),
                status=data.get('status', None),
                kind=data.get('kind', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Node_status_condition.newFromDict(json_data)
class Node_status(object):
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
            return Node_status(
                conditions = [Node_status_condition.newFromDict(condition) for condition in (data.get('conditions',{}) if (data.get('conditions',{}) is not None) else {})],
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Node_status(
                conditions = [Node_status_condition.newFromDict(condition) for condition in (data.get('conditions',{}) if (data.get('conditions',{}) is not None) else {})],
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Node_status.newFromDict(json_data)
class Node(object):
    def __init__(self,**kwargs):
        params = {
            'id':None,
            'hostIP':None,
            'uid':None,
            'kind':None,
            'status':None,
            'resourceVersion':None,
            'apiVersion':None,
            'creationTimestamp':None,
            'selfLink':None,
            'resources':None,
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
                hostIP=data.get('hostIP', None),
                uid=data.get('uid', None),
                kind=data.get('kind', None),
                status=Node_status.newFromDict(data.get('status', {})),
                resourceVersion=data.get('resourceVersion', None),
                apiVersion=data.get('apiVersion', None),
                creationTimestamp=data.get('creationTimestamp', None),
                selfLink=data.get('selfLink', None),
#                resources=Node_resources.newFromDict(data.get('resources', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Node(
                id=data.get('id', None),
                hostIP=data.get('hostIP', None),
                uid=data.get('uid', None),
                kind=data.get('kind', None),
                status=Node_status.newFromDict(data.get('status', {})),
                resourceVersion=data.get('resourceVersion', None),
                apiVersion=data.get('apiVersion', None),
                creationTimestamp=data.get('creationTimestamp', None),
                selfLink=data.get('selfLink', None),
#                resources=Node_resources.newFromDict(data.get('resources', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Node.newFromDict(json_data)