#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class DesiredState(object):
    def __init__(self,**kwargs):
        params = {
            'manifest':None,
            'replicas':None,
            'podTemplate':None,
            'replicaSelector':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['manifest']=self.manifest.toDict();
        params['podTemplate']=self.podTemplate.toDict();
        params['replicaSelector']=self.replicaSelector.toDict();
        
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
                replicas=data.get('replicas', None),
                podTemplate=PodTemplate.newFromDict(data.get('podTemplate', {})),
                replicaSelector=ReplicaSelector.newFromDict(data.get('replicaSelector', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return DesiredState(
                manifest=Manifest.newFromDict(data.get('manifest', {})),
                replicas=data.get('replicas', None),
                podTemplate=PodTemplate.newFromDict(data.get('podTemplate', {})),
                replicaSelector=ReplicaSelector.newFromDict(data.get('replicaSelector', {})),
            )


class Container(object):
    def __init__(self,**kwargs):
        params = {
            'name':None,
            'resources':None,
            'terminationMessagePath':None,
            'imagePullPolicy':None,
            'capabilities':None,
            'image':None,
            'ports':None,
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
                name=data.get('name', None),
#                resources=Resources.newFromDict(data.get('resources', {})),
                terminationMessagePath=data.get('terminationMessagePath', None),
                imagePullPolicy=data.get('imagePullPolicy', None),
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
                image=data.get('image', None),
                ports = [Port.newFromDict(port) for port in data.get('ports',{})],
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Container(
                name=data.get('name', None),
#                resources=Resources.newFromDict(data.get('resources', {})),
                terminationMessagePath=data.get('terminationMessagePath', None),
                imagePullPolicy=data.get('imagePullPolicy', None),
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
                image=data.get('image', None),
                portss = [Port.newFromDict(port) for port in data.get('ports',{})],
            )


class Manifest(object):
    def __init__(self,**kwargs):
        params = {
            'id':None,
            'dnsPolicy':None,
            'restartPolicy':None,
            'version':None,
            'volumes':None,
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
                id=data.get('id', None),
                dnsPolicy=data.get('dnsPolicy', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
                version=data.get('version', None),
                volumes=data.get('volumes', None),
                containers=data.get('containers', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Manifest(
                id=data.get('id', None),
                dnsPolicy=data.get('dnsPolicy', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
                version=data.get('version', None),
                volumes=data.get('volumes', None),
                containers=data.get('containers', None),
            )


class Replicationcontroller(object):
    def __init__(self,**kwargs):
        params = {
            'uid':None,
            'resourceVersion':None,
            'namespace':None,
            'labels':None,
            'creationTimestamp':None,
            'id':None,
            'selfLink':None,
            'currentState':None,
            'apiVersion':None,
            'desiredState':None,
            'kind':None,
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
            return Replicationcontroller(
                uid=data.get('uid', None),
                resourceVersion=data.get('resourceVersion', None),
                namespace=data.get('namespace', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                creationTimestamp=data.get('creationTimestamp', None),
                id=data.get('id', None),
                selfLink=data.get('selfLink', None),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
                apiVersion=data.get('apiVersion', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                kind=data.get('kind', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller(
                uid=data.get('uid', None),
                resourceVersion=data.get('resourceVersion', None),
                namespace=data.get('namespace', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                creationTimestamp=data.get('creationTimestamp', None),
                id=data.get('id', None),
                selfLink=data.get('selfLink', None),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
                apiVersion=data.get('apiVersion', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                kind=data.get('kind', None),
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

