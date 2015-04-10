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


class Resourcequota(object):
    def __init__(self,**kwargs):
        params = {
            'spec':None,
            'id':None,
            'kind':None,
            'apiVersion':None,
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
                spec=Spec.newFromDict(data.get('spec', {})),
                id=data.get('id', None),
                kind=data.get('kind', None),
                apiVersion=data.get('apiVersion', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Resourcequota(
                spec=Spec.newFromDict(data.get('spec', {})),
                id=data.get('id', None),
                kind=data.get('kind', None),
                apiVersion=data.get('apiVersion', None),
            )


class Hard(object):
    def __init__(self,**kwargs):
        params = {
            'pods':None,
            'replicationcontrollers':None,
            'cpu':None,
            'memory':None,
            'services':None,
            'resourcequotas':None,
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
                pods=data.get('pods', None),
                replicationcontrollers=data.get('replicationcontrollers', None),
                cpu=data.get('cpu', None),
                memory=data.get('memory', None),
                services=data.get('services', None),
                resourcequotas=data.get('resourcequotas', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Hard(
                pods=data.get('pods', None),
                replicationcontrollers=data.get('replicationcontrollers', None),
                cpu=data.get('cpu', None),
                memory=data.get('memory', None),
                services=data.get('services', None),
                resourcequotas=data.get('resourcequotas', None),
            )

