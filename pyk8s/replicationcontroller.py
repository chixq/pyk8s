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
            'replicas':None,
            'podTemplate':None,
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
                replicas=data.get('replicas', None),
                podTemplate=PodTemplate.newFromDict(data.get('podTemplate', {})),
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
                replicas=data.get('replicas', None),
                podTemplate=PodTemplate.newFromDict(data.get('podTemplate', {})),
                replicaSelector=ReplicaSelector.newFromDict(data.get('replicaSelector', {})),
                manifest=Manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return DesiredState.newFromDict(json_data)
class Replicationcontroller(object):
    def __init__(self,**kwargs):
        params = {
            'id':None,
            'apiVersion':None,
            'desiredState':None,
            'resourceVersion':None,
            'kind':None,
            'labels':None,
            'creationTimestamp':None,
            'uid':None,
            'selfLink':None,
            'namespace':None,
            'currentState':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['desiredState']=self.desiredState.toDict();
        params['labels']=self.labels.toDict();
        params['currentState']=self.currentState.toDict();
        
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
                id=data.get('id', None),
                apiVersion=data.get('apiVersion', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                resourceVersion=data.get('resourceVersion', None),
                kind=data.get('kind', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                creationTimestamp=data.get('creationTimestamp', None),
                uid=data.get('uid', None),
                selfLink=data.get('selfLink', None),
                namespace=data.get('namespace', None),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller(
                id=data.get('id', None),
                apiVersion=data.get('apiVersion', None),
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                resourceVersion=data.get('resourceVersion', None),
                kind=data.get('kind', None),
                labels=Labels.newFromDict(data.get('labels', {})),
                creationTimestamp=data.get('creationTimestamp', None),
                uid=data.get('uid', None),
                selfLink=data.get('selfLink', None),
                namespace=data.get('namespace', None),
                currentState=CurrentState.newFromDict(data.get('currentState', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller.newFromDict(json_data)
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

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Port.newFromDict(json_data)
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

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicaSelector.newFromDict(json_data)
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
class PodTemplate(object):
    def __init__(self,**kwargs):
        params = {
            'desiredState':None,
            'labels':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
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
            return PodTemplate(
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                labels=Labels.newFromDict(data.get('labels', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return PodTemplate(
                desiredState=DesiredState.newFromDict(data.get('desiredState', {})),
                labels=Labels.newFromDict(data.get('labels', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return PodTemplate.newFromDict(json_data)
class Container(object):
    def __init__(self,**kwargs):
        params = {
            'resources':None,
            'capabilities':None,
            'ports':None,
            'name':None,
            'image':None,
            'imagePullPolicy':None,
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
#                resources=Resources.newFromDict(data.get('resources', {})),
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
                ports = [Port.newFromDict(port) for port in (data.get('ports',{}) if (data.get('ports',{}) is not None) else {})],
                name=data.get('name', None),
                image=data.get('image', None),
                imagePullPolicy=data.get('imagePullPolicy', None),
                terminationMessagePath=data.get('terminationMessagePath', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Container(
#                resources=Resources.newFromDict(data.get('resources', {})),
#                capabilities=Capabilities.newFromDict(data.get('capabilities', {})),
                ports = [Port.newFromDict(port) for port in (data.get('ports',{}) if (data.get('ports',{}) is not None) else {})],
                name=data.get('name', None),
                image=data.get('image', None),
                imagePullPolicy=data.get('imagePullPolicy', None),
                terminationMessagePath=data.get('terminationMessagePath', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Container.newFromDict(json_data)
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
class Manifest(object):
    def __init__(self,**kwargs):
        params = {
            'volumes':None,
            'containers':None,
            'dnsPolicy':None,
            'id':None,
            'restartPolicy':None,
            'version':None,
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
                volumes=data.get('volumes', None),
                containers = [Container.newFromDict(container) for container in (data.get('containers',{}) if (data.get('containers',{}) is not None) else {})],
                dnsPolicy=data.get('dnsPolicy', None),
                id=data.get('id', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
                version=data.get('version', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Manifest(
                volumes=data.get('volumes', None),
                containers = [Container.newFromDict(container) for container in (data.get('containers',{}) if (data.get('containers',{}) is not None) else {})],
                dnsPolicy=data.get('dnsPolicy', None),
                id=data.get('id', None),
                restartPolicy=RestartPolicy.newFromDict(data.get('restartPolicy', {})),
                version=data.get('version', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Manifest.newFromDict(json_data)
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

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return CurrentState.newFromDict(json_data)