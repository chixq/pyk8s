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
            'kind':None,
            'spec':None,
            'id':None,
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
                kind=data.get('kind', None),
                spec=Resourcequota_spec.newFromDict(data.get('spec', {})),
                id=data.get('id', None),
                apiVersion=data.get('apiVersion', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Resourcequota(
                kind=data.get('kind', None),
                spec=Resourcequota_spec.newFromDict(data.get('spec', {})),
                id=data.get('id', None),
                apiVersion=data.get('apiVersion', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Resourcequota.newFromDict(json_data)
class Resourcequota_spec(object):
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
            return Resourcequota_spec(
                hard=Resourcequota_spec_hard.newFromDict(data.get('hard', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Resourcequota_spec(
                hard=Resourcequota_spec_hard.newFromDict(data.get('hard', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Resourcequota_spec.newFromDict(json_data)
class Resourcequota_spec_hard(object):
    def __init__(self,**kwargs):
        params = {
            'services':None,
            'resourcequotas':None,
            'replicationcontrollers':None,
            'cpu':None,
            'pods':None,
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
            return Resourcequota_spec_hard(
                services=data.get('services', None),
                resourcequotas=data.get('resourcequotas', None),
                replicationcontrollers=data.get('replicationcontrollers', None),
                cpu=data.get('cpu', None),
                pods=data.get('pods', None),
                memory=data.get('memory', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Resourcequota_spec_hard(
                services=data.get('services', None),
                resourcequotas=data.get('resourcequotas', None),
                replicationcontrollers=data.get('replicationcontrollers', None),
                cpu=data.get('cpu', None),
                pods=data.get('pods', None),
                memory=data.get('memory', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Resourcequota_spec_hard.newFromDict(json_data)