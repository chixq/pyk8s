#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

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


class Limit(object):
    def __init__(self,**kwargs):
        params = {
            'min':None,
            'max':None,
            'type':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['min']=self.min.toDict();
        params['max']=self.max.toDict();
        
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
                min=Min.newFromDict(data.get('min', {})),
                max=Max.newFromDict(data.get('max', {})),
                type=data.get('type', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Limit(
                min=Min.newFromDict(data.get('min', {})),
                max=Max.newFromDict(data.get('max', {})),
                type=data.get('type', None),
            )


class Limitrange(object):
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
            return Limitrange(
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
        return Limitrange(
                apiVersion=data.get('apiVersion', None),
                spec=Spec.newFromDict(data.get('spec', {})),
                kind=data.get('kind', None),
                id=data.get('id', None),
            )

