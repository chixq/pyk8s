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
            'apiVersion':None,
            'namespace':None,
            'resourceVersion':None,
            'name':None,
            'uid':None,
            'fieldPath':None,
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
            return InvolvedObject(
                apiVersion=data.get('apiVersion', None),
                namespace=data.get('namespace', None),
                resourceVersion=data.get('resourceVersion', None),
                name=data.get('name', None),
                uid=data.get('uid', None),
                fieldPath=data.get('fieldPath', None),
                kind=data.get('kind', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return InvolvedObject(
                apiVersion=data.get('apiVersion', None),
                namespace=data.get('namespace', None),
                resourceVersion=data.get('resourceVersion', None),
                name=data.get('name', None),
                uid=data.get('uid', None),
                fieldPath=data.get('fieldPath', None),
                kind=data.get('kind', None),
            )


class Event(object):
    def __init__(self,**kwargs):
        params = {
            'kind':None,
            'creationTimestamp':None,
            'source':None,
            'reason':None,
            'uid':None,
            'resourceVersion':None,
            'id':None,
            'involvedObject':None,
            'host':None,
            'message':None,
            'namespace':None,
            'apiVersion':None,
            'lastTimestamp':None,
            'annotations':None,
            'firstTimestamp':None,
            'count':None,
            'timestamp':None,
            'generateName':None,
            'status':None,
            'selfLink':None,
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
                kind=data.get('kind', None),
                creationTimestamp=data.get('creationTimestamp', None),
                source=data.get('source', None),
                reason=data.get('reason', None),
                uid=data.get('uid', None),
                resourceVersion=data.get('resourceVersion', None),
                id=data.get('id', None),
                involvedObject=InvolvedObject.newFromDict(data.get('involvedObject', {})),
                host=data.get('host', None),
                message=data.get('message', None),
                namespace=data.get('namespace', None),
                apiVersion=data.get('apiVersion', None),
                lastTimestamp=data.get('lastTimestamp', None),
                annotations=data.get('annotations', None),
                firstTimestamp=data.get('firstTimestamp', None),
                count=data.get('count', None),
                timestamp=data.get('timestamp', None),
                generateName=data.get('generateName', None),
                status=data.get('status', None),
                selfLink=data.get('selfLink', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Event(
                kind=data.get('kind', None),
                creationTimestamp=data.get('creationTimestamp', None),
                source=data.get('source', None),
                reason=data.get('reason', None),
                uid=data.get('uid', None),
                resourceVersion=data.get('resourceVersion', None),
                id=data.get('id', None),
                involvedObject=InvolvedObject.newFromDict(data.get('involvedObject', {})),
                host=data.get('host', None),
                message=data.get('message', None),
                namespace=data.get('namespace', None),
                apiVersion=data.get('apiVersion', None),
                lastTimestamp=data.get('lastTimestamp', None),
                annotations=data.get('annotations', None),
                firstTimestamp=data.get('firstTimestamp', None),
                count=data.get('count', None),
                timestamp=data.get('timestamp', None),
                generateName=data.get('generateName', None),
                status=data.get('status', None),
                selfLink=data.get('selfLink', None),
            )

