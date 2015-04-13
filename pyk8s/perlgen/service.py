#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

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

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Selector.newFromDict(json_data)
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

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Labels.newFromDict(json_data)
class Service(object):
    def __init__(self,**kwargs):
        params = {
            'id':None,
            'labels':None,
            'publicIPs':None,
            'kind':None,
            'selfLink':None,
            'apiVersion':None,
            'uid':None,
            'resourceVersion':None,
            'namespace':None,
            'port':None,
            'creationTimestamp':None,
            'selector':None,
            'protocol':None,
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
                id=data.get('id', None),
                labels=Labels.newFromDict(data.get('labels', {})),
#                publicIPs = [PublicIP.newFromDict(publicIP) for publicIP in (data.get('publicIPs',{}) if (data.get('publicIPs',{}) is not None) else {})],
                kind=data.get('kind', None),
                selfLink=data.get('selfLink', None),
                apiVersion=data.get('apiVersion', None),
                uid=data.get('uid', None),
                resourceVersion=data.get('resourceVersion', None),
                namespace=data.get('namespace', None),
                port=data.get('port', None),
                creationTimestamp=data.get('creationTimestamp', None),
                selector=Selector.newFromDict(data.get('selector', {})),
                protocol=data.get('protocol', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Service(
                id=data.get('id', None),
                labels=Labels.newFromDict(data.get('labels', {})),
#                publicIPs = [PublicIP.newFromDict(publicIP) for publicIP in (data.get('publicIPs',{}) if (data.get('publicIPs',{}) is not None) else {})],
                kind=data.get('kind', None),
                selfLink=data.get('selfLink', None),
                apiVersion=data.get('apiVersion', None),
                uid=data.get('uid', None),
                resourceVersion=data.get('resourceVersion', None),
                namespace=data.get('namespace', None),
                port=data.get('port', None),
                creationTimestamp=data.get('creationTimestamp', None),
                selector=Selector.newFromDict(data.get('selector', {})),
                protocol=data.get('protocol', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Service.newFromDict(json_data)