#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Service_labels(object):
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
            return Service_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Service_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Service_labels.newFromDict(json_data)
class Service(object):
    def __init__(self,**kwargs):
        params = {
            'resourceVersion':None,
            'publicIPs':None,
            'selector':None,
            'protocol':None,
            'labels':None,
            'kind':None,
            'port':None,
            'selfLink':None,
            'id':None,
            'namespace':None,
            'uid':None,
            'creationTimestamp':None,
            'apiVersion':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['selector']=self.selector.toDict();
        params['labels']=self.labels.toDict();
        
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
                resourceVersion=data.get('resourceVersion', None),
#                publicIPs = [Service_publicIP.newFromDict(publicIP) for publicIP in (data.get('publicIPs',{}) if (data.get('publicIPs',{}) is not None) else {})],
                selector=Service_selector.newFromDict(data.get('selector', {})),
                protocol=data.get('protocol', None),
                labels=Service_labels.newFromDict(data.get('labels', {})),
                kind=data.get('kind', None),
                port=data.get('port', None),
                selfLink=data.get('selfLink', None),
                id=data.get('id', None),
                namespace=data.get('namespace', None),
                uid=data.get('uid', None),
                creationTimestamp=data.get('creationTimestamp', None),
                apiVersion=data.get('apiVersion', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Service(
                resourceVersion=data.get('resourceVersion', None),
#                publicIPs = [Service_publicIP.newFromDict(publicIP) for publicIP in (data.get('publicIPs',{}) if (data.get('publicIPs',{}) is not None) else {})],
                selector=Service_selector.newFromDict(data.get('selector', {})),
                protocol=data.get('protocol', None),
                labels=Service_labels.newFromDict(data.get('labels', {})),
                kind=data.get('kind', None),
                port=data.get('port', None),
                selfLink=data.get('selfLink', None),
                id=data.get('id', None),
                namespace=data.get('namespace', None),
                uid=data.get('uid', None),
                creationTimestamp=data.get('creationTimestamp', None),
                apiVersion=data.get('apiVersion', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Service.newFromDict(json_data)
class Service_selector(object):
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
            return Service_selector(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Service_selector(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Service_selector.newFromDict(json_data)