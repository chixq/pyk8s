#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Spec(object):
    def __init__(self,**kwargs):
        params = {
            'hard':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['hard']=self.hard.toDict();
        
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
            return Spec(
                hard=Hard.newFromDict(data.get('hard', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Spec(
                hard=Hard.newFromDict(data.get('hard', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Spec.newFromDict(json_data)
class Hard(object):
    def __init__(self,**kwargs):
        params = {
            'services':None,
            'resourcequotas':None,
            'memory':None,
            'pods':None,
            'replicationcontrollers':None,
            'cpu':None,
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
            return Hard(
                services=data.get('services', None),
                resourcequotas=data.get('resourcequotas', None),
                memory=data.get('memory', None),
                pods=data.get('pods', None),
                replicationcontrollers=data.get('replicationcontrollers', None),
                cpu=data.get('cpu', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Hard(
                services=data.get('services', None),
                resourcequotas=data.get('resourcequotas', None),
                memory=data.get('memory', None),
                pods=data.get('pods', None),
                replicationcontrollers=data.get('replicationcontrollers', None),
                cpu=data.get('cpu', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Hard.newFromDict(json_data)
class Resourcequota(object):
    def __init__(self,**kwargs):
        params = {
            'apiVersion':None,
            'id':None,
            'spec':None,
            'kind':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['spec']=self.spec.toDict();
        
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
            return Resourcequota(
                apiVersion=data.get('apiVersion', None),
                id=data.get('id', None),
                spec=Spec.newFromDict(data.get('spec', {})),
                kind=data.get('kind', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Resourcequota(
                apiVersion=data.get('apiVersion', None),
                id=data.get('id', None),
                spec=Spec.newFromDict(data.get('spec', {})),
                kind=data.get('kind', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Resourcequota.newFromDict(json_data)