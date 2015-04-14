#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Event_involvedObject(object):
    def __init__(self,**kwargs):
        params = {
            'namespace':None,
            'uid':None,
            'apiVersion':None,
            'resourceVersion':None,
            'kind':None,
            'fieldPath':None,
            'name':None,
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
            return Event_involvedObject(
                namespace=data.get('namespace', None),
                uid=data.get('uid', None),
                apiVersion=data.get('apiVersion', None),
                resourceVersion=data.get('resourceVersion', None),
                kind=data.get('kind', None),
                fieldPath=data.get('fieldPath', None),
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Event_involvedObject(
                namespace=data.get('namespace', None),
                uid=data.get('uid', None),
                apiVersion=data.get('apiVersion', None),
                resourceVersion=data.get('resourceVersion', None),
                kind=data.get('kind', None),
                fieldPath=data.get('fieldPath', None),
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Event_involvedObject.newFromDict(json_data)
class Event(object):
    def __init__(self,**kwargs):
        params = {
            'lastTimestamp':None,
            'annotations':None,
            'selfLink':None,
            'message':None,
            'source':None,
            'namespace':None,
            'generateName':None,
            'kind':None,
            'host':None,
            'firstTimestamp':None,
            'id':None,
            'timestamp':None,
            'uid':None,
            'reason':None,
            'apiVersion':None,
            'status':None,
            'resourceVersion':None,
            'creationTimestamp':None,
            'involvedObject':None,
            'count':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['involvedObject']=self.involvedObject.toDict();
        
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
            return Event(
                lastTimestamp=data.get('lastTimestamp', None),
                annotations=data.get('annotations', None),
                selfLink=data.get('selfLink', None),
                message=data.get('message', None),
                source=data.get('source', None),
                namespace=data.get('namespace', None),
                generateName=data.get('generateName', None),
                kind=data.get('kind', None),
                host=data.get('host', None),
                firstTimestamp=data.get('firstTimestamp', None),
                id=data.get('id', None),
                timestamp=data.get('timestamp', None),
                uid=data.get('uid', None),
                reason=data.get('reason', None),
                apiVersion=data.get('apiVersion', None),
                status=data.get('status', None),
                resourceVersion=data.get('resourceVersion', None),
                creationTimestamp=data.get('creationTimestamp', None),
                involvedObject=Event_involvedObject.newFromDict(data.get('involvedObject', {})),
                count=data.get('count', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Event(
                lastTimestamp=data.get('lastTimestamp', None),
                annotations=data.get('annotations', None),
                selfLink=data.get('selfLink', None),
                message=data.get('message', None),
                source=data.get('source', None),
                namespace=data.get('namespace', None),
                generateName=data.get('generateName', None),
                kind=data.get('kind', None),
                host=data.get('host', None),
                firstTimestamp=data.get('firstTimestamp', None),
                id=data.get('id', None),
                timestamp=data.get('timestamp', None),
                uid=data.get('uid', None),
                reason=data.get('reason', None),
                apiVersion=data.get('apiVersion', None),
                status=data.get('status', None),
                resourceVersion=data.get('resourceVersion', None),
                creationTimestamp=data.get('creationTimestamp', None),
                involvedObject=Event_involvedObject.newFromDict(data.get('involvedObject', {})),
                count=data.get('count', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Event.newFromDict(json_data)