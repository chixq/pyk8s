#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Service(object):
    def __init__(self,**kwargs):
        params = {
            'selfLink':None,
            'labels':None,
            'resourceVersion':None,
            'uid':None,
            'publicIPs':None,
            'port':None,
            'kind':None,
            'namespace':None,
            'id':None,
            'creationTimestamp':None,
            'protocol':None,
            'selector':None,
            'apiVersion':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['labels']=self.labels.toDict();
        params['selector']=self.selector.toDict();
        
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
            return Service(
                selfLink=data.get('selfLink', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                resourceVersion=data.get('resourceVersion', None),
                uid=data.get('uid', None),
#                publicIPs = [PublicIP.newFromDict(publicIP) for publicIP in data.get('publicIPs',{})],
                port=data.get('port', None),
                kind=data.get('kind', None),
                namespace=data.get('namespace', None),
                id=data.get('id', None),
                creationTimestamp=data.get('creationTimestamp', None),
                protocol=data.get('protocol', None),
                selector=Selector.newFromDict(data.get('selector', {})),
                apiVersion=data.get('apiVersion', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Service(
                selfLink=data.get('selfLink', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                resourceVersion=data.get('resourceVersion', None),
                uid=data.get('uid', None),
#                publicIPss = [PublicIP.newFromDict(publicIP) for publicIP in data.get('publicIPs',{})],
                port=data.get('port', None),
                kind=data.get('kind', None),
                namespace=data.get('namespace', None),
                id=data.get('id', None),
                creationTimestamp=data.get('creationTimestamp', None),
                protocol=data.get('protocol', None),
                selector=Selector.newFromDict(data.get('selector', {})),
                apiVersion=data.get('apiVersion', None),
            )


class Selector(object):
    def __init__(self,**kwargs):
        params = {
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
            return Selector(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Selector(
                name=data.get('name', None),
            )


class Labels(object):
    def __init__(self,**kwargs):
        params = {
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
            return Labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Labels(
                name=data.get('name', None),
            )

