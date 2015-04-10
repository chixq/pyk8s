#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

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


class Service(object):
    def __init__(self,**kwargs):
        params = {
            'kind':None,
            'creationTimestamp':None,
            'publicIPs':None,
            'protocol':None,
            'namespace':None,
            'resourceVersion':None,
            'id':None,
            'port':None,
            'labels':None,
            'uid':None,
            'selfLink':None,
            'apiVersion':None,
            'selector':None,
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
                kind=data.get('kind', None),
                creationTimestamp=data.get('creationTimestamp', None),
#                publicIPs = [PublicIP.newFromDict(publicIP) for publicIP in data.get('publicIPs',{})],
                protocol=data.get('protocol', None),
                namespace=data.get('namespace', None),
                resourceVersion=data.get('resourceVersion', None),
                id=data.get('id', None),
                port=data.get('port', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                uid=data.get('uid', None),
                selfLink=data.get('selfLink', None),
                apiVersion=data.get('apiVersion', None),
                selector=Selector.newFromDict(data.get('selector', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Service(
                kind=data.get('kind', None),
                creationTimestamp=data.get('creationTimestamp', None),
#                publicIPss = [PublicIP.newFromDict(publicIP) for publicIP in data.get('publicIPs',{})],
                protocol=data.get('protocol', None),
                namespace=data.get('namespace', None),
                resourceVersion=data.get('resourceVersion', None),
                id=data.get('id', None),
                port=data.get('port', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                uid=data.get('uid', None),
                selfLink=data.get('selfLink', None),
                apiVersion=data.get('apiVersion', None),
                selector=Selector.newFromDict(data.get('selector', {})),
            )

