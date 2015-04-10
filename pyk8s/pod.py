#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Pod(object):
    def __init__(self,**kwargs):
        params = {
            'uid':None,
            'currentState':None,
            'generateName':None,
            'apiVersion':None,
            'desiredState':None,
            'id':None,
            'creationTimestamp':None,
            'kind':None,
            'selfLink':None,
            'labels':None,
            'namespace':None,
            'resourceVersion':None,
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
                uid=data.get('uid', None),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
                generateName=data.get('generateName', None),
                apiVersion=data.get('apiVersion', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                id=data.get('id', None),
                creationTimestamp=data.get('creationTimestamp', None),
                kind=data.get('kind', None),
                selfLink=data.get('selfLink', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                namespace=data.get('namespace', None),
                resourceVersion=data.get('resourceVersion', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod(
                uid=data.get('uid', None),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
                generateName=data.get('generateName', None),
                apiVersion=data.get('apiVersion', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                id=data.get('id', None),
                creationTimestamp=data.get('creationTimestamp', None),
                kind=data.get('kind', None),
                selfLink=data.get('selfLink', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                namespace=data.get('namespace', None),
                resourceVersion=data.get('resourceVersion', None),
            )


class Container(object):
    def __init__(self,**kwargs):
        params = {
            'imagePullPolicy':None,
            'capabilities':None,
            'terminationMessagePath':None,
            'resources':None,
            'ports':None,
            'name':None,
            'image':None,
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
                imagePullPolicy=data.get('imagePullPolicy', None),
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
                terminationMessagePath=data.get('terminationMessagePath', None),
#                resources=Resources.newFromDict(data.get('resources', {})),
                ports = [Port.newFromDict(port) for port in data.get('ports',{})],
                name=data.get('name', None),
                image=data.get('image', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Container(
                imagePullPolicy=data.get('imagePullPolicy', None),
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
                terminationMessagePath=data.get('terminationMessagePath', None),
#                resources=Resources.newFromDict(data.get('resources', {})),
                portss = [Port.newFromDict(port) for port in data.get('ports',{})],
                name=data.get('name', None),
                image=data.get('image', None),
            )


class Manifest(object):
    def __init__(self,**kwargs):
        params = {
            'dnsPolicy':None,
            'volumes':None,
            'containers':None,
            'id':None,
            'version':None,
            'restartPolicy':None,
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
                dnsPolicy=data.get('dnsPolicy', None),
                volumes=data.get('volumes', None),
                containers=data.get('containers', None),
                id=data.get('id', None),
                version=data.get('version', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Manifest(
                dnsPolicy=data.get('dnsPolicy', None),
                volumes=data.get('volumes', None),
                containers=data.get('containers', None),
                id=data.get('id', None),
                version=data.get('version', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
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

