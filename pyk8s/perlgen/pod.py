#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Container(object):
    def __init__(self,**kwargs):
        params = {
            'capabilities':None,
            'imagePullPolicy':None,
            'image':None,
            'ports':None,
            'resources':None,
            'terminationMessagePath':None,
            'name':None,
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
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
                imagePullPolicy=data.get('imagePullPolicy', None),
                image=data.get('image', None),
                ports = [Port.newFromDict(port) for port in data.get('ports',{})],
#                resources=Resources.newFromDict(data.get('resources', {})),
                terminationMessagePath=data.get('terminationMessagePath', None),
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Container(
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
                imagePullPolicy=data.get('imagePullPolicy', None),
                image=data.get('image', None),
                portss = [Port.newFromDict(port) for port in data.get('ports',{})],
#                resources=Resources.newFromDict(data.get('resources', {})),
                terminationMessagePath=data.get('terminationMessagePath', None),
                name=data.get('name', None),
            )


class Port(object):
    def __init__(self,**kwargs):
        params = {
            'hostPort':None,
            'protocol':None,
            'containerPort':None,
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
                hostPort=data.get('hostPort', None),
                protocol=data.get('protocol', None),
                containerPort=data.get('containerPort', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Port(
                hostPort=data.get('hostPort', None),
                protocol=data.get('protocol', None),
                containerPort=data.get('containerPort', None),
            )


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


class CurrentState(object):
    def __init__(self,**kwargs):
        params = {
            'manifest':None,
            'status':None,
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
                manifest=Manifest.newFromDict(data.get('manifest', {})),
                status=data.get('status', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return CurrentState(
                manifest=Manifest.newFromDict(data.get('manifest', {})),
                status=data.get('status', None),
            )


class Pod(object):
    def __init__(self,**kwargs):
        params = {
            'resourceVersion':None,
            'id':None,
            'creationTimestamp':None,
            'namespace':None,
            'uid':None,
            'generateName':None,
            'apiVersion':None,
            'labels':None,
            'currentState':None,
            'kind':None,
            'selfLink':None,
            'desiredState':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['labels']=self.labels.toDict();
        params['currentState']=self.currentState.toDict();
        params['desiredState']=self.desiredState.toDict();
        
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
                resourceVersion=data.get('resourceVersion', None),
                id=data.get('id', None),
                creationTimestamp=data.get('creationTimestamp', None),
                namespace=data.get('namespace', None),
                uid=data.get('uid', None),
                generateName=data.get('generateName', None),
                apiVersion=data.get('apiVersion', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
                kind=data.get('kind', None),
                selfLink=data.get('selfLink', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod(
                resourceVersion=data.get('resourceVersion', None),
                id=data.get('id', None),
                creationTimestamp=data.get('creationTimestamp', None),
                namespace=data.get('namespace', None),
                uid=data.get('uid', None),
                generateName=data.get('generateName', None),
                apiVersion=data.get('apiVersion', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
                kind=data.get('kind', None),
                selfLink=data.get('selfLink', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
            )


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


class Manifest(object):
    def __init__(self,**kwargs):
        params = {
            'containers':None,
            'restartPolicy':None,
            'version':None,
            'dnsPolicy':None,
            'volumes':None,
            'id':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
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
                containers=data.get('containers', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
                version=data.get('version', None),
                dnsPolicy=data.get('dnsPolicy', None),
                volumes=data.get('volumes', None),
                id=data.get('id', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Manifest(
                containers=data.get('containers', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
                version=data.get('version', None),
                dnsPolicy=data.get('dnsPolicy', None),
                volumes=data.get('volumes', None),
                id=data.get('id', None),
            )


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

