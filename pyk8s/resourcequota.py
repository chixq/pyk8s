#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Resourcequota(object):
    def __init__(self,**kwargs):
        params = {
            'apiVersion':None,
            'spec':None,
            'kind':None,
            'id':None,
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
                spec=Spec.newFromDict(data.get('spec', {})),
                kind=data.get('kind', None),
                id=data.get('id', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Resourcequota(
                apiVersion=data.get('apiVersion', None),
                spec=Spec.newFromDict(data.get('spec', {})),
                kind=data.get('kind', None),
                id=data.get('id', None),
            )


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


class Hard(object):
    def __init__(self,**kwargs):
        params = {
            'memory':None,
            'resourcequotas':None,
            'services':None,
            'pods':None,
            'cpu':None,
            'replicationcontrollers':None,
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
                memory=data.get('memory', None),
                resourcequotas=data.get('resourcequotas', None),
                services=data.get('services', None),
                pods=data.get('pods', None),
                cpu=data.get('cpu', None),
                replicationcontrollers=data.get('replicationcontrollers', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Hard(
                memory=data.get('memory', None),
                resourcequotas=data.get('resourcequotas', None),
                services=data.get('services', None),
                pods=data.get('pods', None),
                cpu=data.get('cpu', None),
                replicationcontrollers=data.get('replicationcontrollers', None),
            )

