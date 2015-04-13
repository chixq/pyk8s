#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class RestartPolicy(object):
    def __init__(self,**kwargs):
        params = {
            'always':None,
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
            return RestartPolicy(
#                always=Always.newFromDict(data.get('always', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return RestartPolicy(
#                always=Always.newFromDict(data.get('always', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return RestartPolicy.newFromDict(json_data)
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
class DesiredState(object):
    def __init__(self,**kwargs):
        params = {
            'manifest':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['manifest']=self.manifest.toDict();
        
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
            return DesiredState(
                manifest=Manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return DesiredState(
                manifest=Manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return DesiredState.newFromDict(json_data)
class Port(object):
    def __init__(self,**kwargs):
        params = {
            'containerPort':None,
            'hostPort':None,
            'protocol':None,
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
            return Port(
                containerPort=data.get('containerPort', None),
                hostPort=data.get('hostPort', None),
                protocol=data.get('protocol', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Port(
                containerPort=data.get('containerPort', None),
                hostPort=data.get('hostPort', None),
                protocol=data.get('protocol', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Port.newFromDict(json_data)
class CurrentState(object):
    def __init__(self,**kwargs):
        params = {
            'status':None,
            'manifest':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['manifest']=self.manifest.toDict();
        
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
            return CurrentState(
                status=data.get('status', None),
                manifest=Manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return CurrentState(
                status=data.get('status', None),
                manifest=Manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return CurrentState.newFromDict(json_data)
class Pod(object):
    def __init__(self,**kwargs):
        params = {
            'namespace':None,
            'uid':None,
            'id':None,
            'resourceVersion':None,
            'kind':None,
            'currentState':None,
            'creationTimestamp':None,
            'apiVersion':None,
            'desiredState':None,
            'selfLink':None,
            'generateName':None,
            'labels':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['currentState']=self.currentState.toDict();
        params['desiredState']=self.desiredState.toDict();
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
            return Pod(
                namespace=data.get('namespace', None),
                uid=data.get('uid', None),
                id=data.get('id', None),
                resourceVersion=data.get('resourceVersion', None),
                kind=data.get('kind', None),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
                creationTimestamp=data.get('creationTimestamp', None),
                apiVersion=data.get('apiVersion', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                selfLink=data.get('selfLink', None),
                generateName=data.get('generateName', None),
                labels=Labels.newFromDict(data.get('labels', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod(
                namespace=data.get('namespace', None),
                uid=data.get('uid', None),
                id=data.get('id', None),
                resourceVersion=data.get('resourceVersion', None),
                kind=data.get('kind', None),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
                creationTimestamp=data.get('creationTimestamp', None),
                apiVersion=data.get('apiVersion', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                selfLink=data.get('selfLink', None),
                generateName=data.get('generateName', None),
                labels=Labels.newFromDict(data.get('labels', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Pod.newFromDict(json_data)
class Container(object):
    def __init__(self,**kwargs):
        params = {
            'ports':None,
            'capabilities':None,
            'resources':None,
            'imagePullPolicy':None,
            'image':None,
            'name':None,
            'terminationMessagePath':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        i=0
        for port in self.ports:
            params['ports'][i]=port.toDict();
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
            return Container(
                ports = [Port.newFromDict(port) for port in (data.get('ports',{}) if (data.get('ports',{}) is not None) else {})],
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
#                resources=Resources.newFromDict(data.get('resources', {})),
                imagePullPolicy=data.get('imagePullPolicy', None),
                image=data.get('image', None),
                name=data.get('name', None),
                terminationMessagePath=data.get('terminationMessagePath', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Container(
                ports = [Port.newFromDict(port) for port in (data.get('ports',{}) if (data.get('ports',{}) is not None) else {})],
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
#                resources=Resources.newFromDict(data.get('resources', {})),
                imagePullPolicy=data.get('imagePullPolicy', None),
                image=data.get('image', None),
                name=data.get('name', None),
                terminationMessagePath=data.get('terminationMessagePath', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Container.newFromDict(json_data)
class Manifest(object):
    def __init__(self,**kwargs):
        params = {
            'id':None,
            'containers':None,
            'dnsPolicy':None,
            'version':None,
            'volumes':None,
            'restartPolicy':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        i=0
        for container in self.containers:
            params['containers'][i]=container.toDict();
            i=i+1;
        params['restartPolicy']=self.restartPolicy.toDict();
        
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
            return Manifest(
                id=data.get('id', None),
                containers = [Container.newFromDict(container) for container in (data.get('containers',{}) if (data.get('containers',{}) is not None) else {})],
                dnsPolicy=data.get('dnsPolicy', None),
                version=data.get('version', None),
                volumes=data.get('volumes', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Manifest(
                id=data.get('id', None),
                containers = [Container.newFromDict(container) for container in (data.get('containers',{}) if (data.get('containers',{}) is not None) else {})],
                dnsPolicy=data.get('dnsPolicy', None),
                version=data.get('version', None),
                volumes=data.get('volumes', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Manifest.newFromDict(json_data)