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
            'kind':None,
            'resourceVersion':None,
            'name':None,
            'fieldPath':None,
            'uid':None,
            'apiVersion':None,
            'namespace':None,
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
                kind=data.get('kind', None),
                resourceVersion=data.get('resourceVersion', None),
                name=data.get('name', None),
                fieldPath=data.get('fieldPath', None),
                uid=data.get('uid', None),
                apiVersion=data.get('apiVersion', None),
                namespace=data.get('namespace', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return InvolvedObject(
                kind=data.get('kind', None),
                resourceVersion=data.get('resourceVersion', None),
                name=data.get('name', None),
                fieldPath=data.get('fieldPath', None),
                uid=data.get('uid', None),
                apiVersion=data.get('apiVersion', None),
                namespace=data.get('namespace', None),
            )


class Event(object):
    def __init__(self,**kwargs):
        params = {
            'selfLink':None,
            'apiVersion':None,
            'generateName':None,
            'reason':None,
            'source':None,
            'lastTimestamp':None,
            'creationTimestamp':None,
            'resourceVersion':None,
            'annotations':None,
            'namespace':None,
            'id':None,
            'firstTimestamp':None,
            'involvedObject':None,
            'status':None,
            'message':None,
            'uid':None,
            'timestamp':None,
            'count':None,
            'kind':None,
            'host':None,
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
                selfLink=data.get('selfLink', None),
                apiVersion=data.get('apiVersion', None),
                generateName=data.get('generateName', None),
                reason=data.get('reason', None),
                source=data.get('source', None),
                lastTimestamp=data.get('lastTimestamp', None),
                creationTimestamp=data.get('creationTimestamp', None),
                resourceVersion=data.get('resourceVersion', None),
                annotations=data.get('annotations', None),
                namespace=data.get('namespace', None),
                id=data.get('id', None),
                firstTimestamp=data.get('firstTimestamp', None),
                involvedObject=InvolvedObject.newFromDict(data.get('involvedObject', {})),
                status=data.get('status', None),
                message=data.get('message', None),
                uid=data.get('uid', None),
                timestamp=data.get('timestamp', None),
                count=data.get('count', None),
                kind=data.get('kind', None),
                host=data.get('host', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Event(
                selfLink=data.get('selfLink', None),
                apiVersion=data.get('apiVersion', None),
                generateName=data.get('generateName', None),
                reason=data.get('reason', None),
                source=data.get('source', None),
                lastTimestamp=data.get('lastTimestamp', None),
                creationTimestamp=data.get('creationTimestamp', None),
                resourceVersion=data.get('resourceVersion', None),
                annotations=data.get('annotations', None),
                namespace=data.get('namespace', None),
                id=data.get('id', None),
                firstTimestamp=data.get('firstTimestamp', None),
                involvedObject=InvolvedObject.newFromDict(data.get('involvedObject', {})),
                status=data.get('status', None),
                message=data.get('message', None),
                uid=data.get('uid', None),
                timestamp=data.get('timestamp', None),
                count=data.get('count', None),
                kind=data.get('kind', None),
                host=data.get('host', None),
            )

