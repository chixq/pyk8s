#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class InvolvedObject(object):
    def __init__(self,**kwargs):
        params = {
            'name':None,
            'apiVersion':None,
            'uid':None,
            'fieldPath':None,
            'namespace':None,
            'kind':None,
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
            return InvolvedObject(
                name=data.get('name', None),
                apiVersion=data.get('apiVersion', None),
                uid=data.get('uid', None),
                fieldPath=data.get('fieldPath', None),
                namespace=data.get('namespace', None),
                kind=data.get('kind', None),
                resourceVersion=data.get('resourceVersion', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return InvolvedObject(
                name=data.get('name', None),
                apiVersion=data.get('apiVersion', None),
                uid=data.get('uid', None),
                fieldPath=data.get('fieldPath', None),
                namespace=data.get('namespace', None),
                kind=data.get('kind', None),
                resourceVersion=data.get('resourceVersion', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return InvolvedObject.newFromDict(json_data)
class Event(object):
    def __init__(self,**kwargs):
        params = {
            'count':None,
            'kind':None,
            'status':None,
            'involvedObject':None,
            'host':None,
            'id':None,
            'source':None,
            'lastTimestamp':None,
            'apiVersion':None,
            'generateName':None,
            'creationTimestamp':None,
            'selfLink':None,
            'resourceVersion':None,
            'namespace':None,
            'annotations':None,
            'message':None,
            'timestamp':None,
            'uid':None,
            'reason':None,
            'firstTimestamp':None,
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
                count=data.get('count', None),
                kind=data.get('kind', None),
                status=data.get('status', None),
                involvedObject=InvolvedObject.newFromDict(data.get('involvedObject', {})),
                host=data.get('host', None),
                id=data.get('id', None),
                source=data.get('source', None),
                lastTimestamp=data.get('lastTimestamp', None),
                apiVersion=data.get('apiVersion', None),
                generateName=data.get('generateName', None),
                creationTimestamp=data.get('creationTimestamp', None),
                selfLink=data.get('selfLink', None),
                resourceVersion=data.get('resourceVersion', None),
                namespace=data.get('namespace', None),
                annotations=data.get('annotations', None),
                message=data.get('message', None),
                timestamp=data.get('timestamp', None),
                uid=data.get('uid', None),
                reason=data.get('reason', None),
                firstTimestamp=data.get('firstTimestamp', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Event(
                count=data.get('count', None),
                kind=data.get('kind', None),
                status=data.get('status', None),
                involvedObject=InvolvedObject.newFromDict(data.get('involvedObject', {})),
                host=data.get('host', None),
                id=data.get('id', None),
                source=data.get('source', None),
                lastTimestamp=data.get('lastTimestamp', None),
                apiVersion=data.get('apiVersion', None),
                generateName=data.get('generateName', None),
                creationTimestamp=data.get('creationTimestamp', None),
                selfLink=data.get('selfLink', None),
                resourceVersion=data.get('resourceVersion', None),
                namespace=data.get('namespace', None),
                annotations=data.get('annotations', None),
                message=data.get('message', None),
                timestamp=data.get('timestamp', None),
                uid=data.get('uid', None),
                reason=data.get('reason', None),
                firstTimestamp=data.get('firstTimestamp', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Event.newFromDict(json_data)