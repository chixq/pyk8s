#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Limit(object):
    def __init__(self,**kwargs):
        params = {
            'max':None,
            'min':None,
            'type':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['max']=self.max.toDict();
        params['min']=self.min.toDict();
        
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
            return Limit(
                max=Max.newFromDict(data.get('max', {})),
                min=Min.newFromDict(data.get('min', {})),
                type=data.get('type', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Limit(
                max=Max.newFromDict(data.get('max', {})),
                min=Min.newFromDict(data.get('min', {})),
                type=data.get('type', None),
            )


class Max(object):
    def __init__(self,**kwargs):
        params = {
            'cpu':None,
            'memory':None,
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
            return Max(
                cpu=data.get('cpu', None),
                memory=data.get('memory', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Max(
                cpu=data.get('cpu', None),
                memory=data.get('memory', None),
            )


class Spec(object):
    def __init__(self,**kwargs):
        params = {
            'limits':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        i=0
        for limit in self.limits:
            params['limits'][i]=limit.toDict();
            i=i+1;
        
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
                limits = [Limit.newFromDict(limit) for limit in data.get('limits',{})],
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Spec(
                limitss = [Limit.newFromDict(limit) for limit in data.get('limits',{})],
            )


class Limitrange(object):
    def __init__(self,**kwargs):
        params = {
            'spec':None,
            'id':None,
            'apiVersion':None,
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
            return Limitrange(
                spec=Spec.newFromDict(data.get('spec', {})),
                id=data.get('id', None),
                apiVersion=data.get('apiVersion', None),
                kind=data.get('kind', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Limitrange(
                spec=Spec.newFromDict(data.get('spec', {})),
                id=data.get('id', None),
                apiVersion=data.get('apiVersion', None),
                kind=data.get('kind', None),
            )


class Min(object):
    def __init__(self,**kwargs):
        params = {
            'cpu':None,
            'memory':None,
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
            return Min(
                cpu=data.get('cpu', None),
                memory=data.get('memory', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Min(
                cpu=data.get('cpu', None),
                memory=data.get('memory', None),
            )

