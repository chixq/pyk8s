#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class LimitRange(object):
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
            return LimitRange(
                spec=LimitRange_spec.newFromDict(data.get('spec', {})),
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
        return LimitRange(
                spec=LimitRange_spec.newFromDict(data.get('spec', {})),
                id=data.get('id', None),
                apiVersion=data.get('apiVersion', None),
                kind=data.get('kind', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return LimitRange.newFromDict(json_data)
class LimitRange_spec_limit_min(object):
    def __init__(self,**kwargs):
        params = {
            'memory':None,
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
            return LimitRange_spec_limit_min(
                memory=data.get('memory', None),
                cpu=data.get('cpu', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return LimitRange_spec_limit_min(
                memory=data.get('memory', None),
                cpu=data.get('cpu', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return LimitRange_spec_limit_min.newFromDict(json_data)
class LimitRange_spec_limit_max(object):
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
            return LimitRange_spec_limit_max(
                cpu=data.get('cpu', None),
                memory=data.get('memory', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return LimitRange_spec_limit_max(
                cpu=data.get('cpu', None),
                memory=data.get('memory', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return LimitRange_spec_limit_max.newFromDict(json_data)
class LimitRange_spec(object):
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
            return LimitRange_spec(
                limits = [LimitRange_spec_limit.newFromDict(limit) for limit in (data.get('limits',{}) if (data.get('limits',{}) is not None) else {})],
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return LimitRange_spec(
                limits = [LimitRange_spec_limit.newFromDict(limit) for limit in (data.get('limits',{}) if (data.get('limits',{}) is not None) else {})],
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return LimitRange_spec.newFromDict(json_data)
class LimitRange_spec_limit(object):
    def __init__(self,**kwargs):
        params = {
            'min':None,
            'type':None,
            'max':None,
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
            return LimitRange_spec_limit(
                min=LimitRange_spec_limit_min.newFromDict(data.get('min', {})),
                type=data.get('type', None),
                max=LimitRange_spec_limit_max.newFromDict(data.get('max', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return LimitRange_spec_limit(
                min=LimitRange_spec_limit_min.newFromDict(data.get('min', {})),
                type=data.get('type', None),
                max=LimitRange_spec_limit_max.newFromDict(data.get('max', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return LimitRange_spec_limit.newFromDict(json_data)