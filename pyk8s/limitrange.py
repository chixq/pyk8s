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
                limits = [Limit.newFromDict(limit) for limit in (data.get('limits',{}) if (data.get('limits',{}) is not None) else {})],
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Spec(
                limits = [Limit.newFromDict(limit) for limit in (data.get('limits',{}) if (data.get('limits',{}) is not None) else {})],
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Spec.newFromDict(json_data)
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

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Min.newFromDict(json_data)
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

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Max.newFromDict(json_data)
class Limit(object):
    def __init__(self,**kwargs):
        params = {
            'max':None,
            'type':None,
            'min':None,
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
                type=data.get('type', None),
                min=Min.newFromDict(data.get('min', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Limit(
                max=Max.newFromDict(data.get('max', {})),
                type=data.get('type', None),
                min=Min.newFromDict(data.get('min', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Limit.newFromDict(json_data)
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

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Limitrange.newFromDict(json_data)