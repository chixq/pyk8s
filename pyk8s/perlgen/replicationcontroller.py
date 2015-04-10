#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

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
            'dnsPolicy':None,
            'version':None,
            'volumes':None,
            'restartPolicy':None,
            'id':None,
            'containers':None,
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
                version=data.get('version', None),
                volumes=data.get('volumes', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
                id=data.get('id', None),
                containers=data.get('containers', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Manifest(
                dnsPolicy=data.get('dnsPolicy', None),
                version=data.get('version', None),
                volumes=data.get('volumes', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
                id=data.get('id', None),
                containers=data.get('containers', None),
            )


class CurrentState(object):
    def __init__(self,**kwargs):
        params = {
            'replicas':None,
            'podTemplate':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['podTemplate']=self.podTemplate.toDict();
        
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
                replicas=data.get('replicas', None),
                podTemplate=PodTemplate.newFromDict(data.get('podTemplate', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return CurrentState(
                replicas=data.get('replicas', None),
                podTemplate=PodTemplate.newFromDict(data.get('podTemplate', {})),
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


class ReplicaSelector(object):
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
            return ReplicaSelector(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicaSelector(
                name=data.get('name', None),
            )


class PodTemplate(object):
    def __init__(self,**kwargs):
        params = {
            'labels':None,
            'desiredState':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['labels']=self.labels.toDict();
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
            return PodTemplate(
                labels=Labels.newFromDict(data.get('labels', {})),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return PodTemplate(
                labels=Labels.newFromDict(data.get('labels', {})),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
            )


class DesiredState(object):
    def __init__(self,**kwargs):
        params = {
            'podTemplate':None,
            'replicas':None,
            'replicaSelector':None,
            'manifest':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['podTemplate']=self.podTemplate.toDict();
        params['replicaSelector']=self.replicaSelector.toDict();
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
                podTemplate=PodTemplate.newFromDict(data.get('podTemplate', {})),
                replicas=data.get('replicas', None),
                replicaSelector=ReplicaSelector.newFromDict(data.get('replicaSelector', {})),
                manifest=Manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return DesiredState(
                podTemplate=PodTemplate.newFromDict(data.get('podTemplate', {})),
                replicas=data.get('replicas', None),
                replicaSelector=ReplicaSelector.newFromDict(data.get('replicaSelector', {})),
                manifest=Manifest.newFromDict(data.get('manifest', {})),
            )


class Replicationcontroller(object):
    def __init__(self,**kwargs):
        params = {
            'selfLink':None,
            'currentState':None,
            'id':None,
            'uid':None,
            'labels':None,
            'creationTimestamp':None,
            'desiredState':None,
            'kind':None,
            'apiVersion':None,
            'resourceVersion':None,
            'namespace':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['currentState']=self.currentState.toDict();
        params['labels']=self.labels.toDict();
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
            return Replicationcontroller(
                selfLink=data.get('selfLink', None),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
                id=data.get('id', None),
                uid=data.get('uid', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                creationTimestamp=data.get('creationTimestamp', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                kind=data.get('kind', None),
                apiVersion=data.get('apiVersion', None),
                resourceVersion=data.get('resourceVersion', None),
                namespace=data.get('namespace', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller(
                selfLink=data.get('selfLink', None),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
                id=data.get('id', None),
                uid=data.get('uid', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                creationTimestamp=data.get('creationTimestamp', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                kind=data.get('kind', None),
                apiVersion=data.get('apiVersion', None),
                resourceVersion=data.get('resourceVersion', None),
                namespace=data.get('namespace', None),
            )


class Port(object):
    def __init__(self,**kwargs):
        params = {
            'protocol':None,
            'containerPort':None,
            'hostPort':None,
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
                protocol=data.get('protocol', None),
                containerPort=data.get('containerPort', None),
                hostPort=data.get('hostPort', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Port(
                protocol=data.get('protocol', None),
                containerPort=data.get('containerPort', None),
                hostPort=data.get('hostPort', None),
            )


class Container(object):
    def __init__(self,**kwargs):
        params = {
            'terminationMessagePath':None,
            'resources':None,
            'image':None,
            'capabilities':None,
            'name':None,
            'ports':None,
            'imagePullPolicy':None,
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
                terminationMessagePath=data.get('terminationMessagePath', None),
#                resources=Resources.newFromDict(data.get('resources', {})),
                image=data.get('image', None),
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
                name=data.get('name', None),
                ports = [Port.newFromDict(port) for port in data.get('ports',{})],
                imagePullPolicy=data.get('imagePullPolicy', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Container(
                terminationMessagePath=data.get('terminationMessagePath', None),
#                resources=Resources.newFromDict(data.get('resources', {})),
                image=data.get('image', None),
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
                name=data.get('name', None),
                portss = [Port.newFromDict(port) for port in data.get('ports',{})],
                imagePullPolicy=data.get('imagePullPolicy', None),
            )

