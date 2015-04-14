#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Pod_desiredState(object):
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
            return Pod_desiredState(
                manifest=Pod_desiredState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod_desiredState(
                manifest=Pod_desiredState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Pod_desiredState.newFromDict(json_data)
class Pod_desiredState_manifest_container(object):
    def __init__(self,**kwargs):
        params = {
            'imagePullPolicy':None,
            'terminationMessagePath':None,
            'image':None,
            'capabilities':None,
            'resources':None,
            'ports':None,
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
            return Pod_desiredState_manifest_container(
                imagePullPolicy=data.get('imagePullPolicy', None),
                terminationMessagePath=data.get('terminationMessagePath', None),
                image=data.get('image', None),
#                capabilities=Pod_desiredState_manifest_container_capabilities.newFromDict(data.get('capabilities', {})),
#                resources=Pod_desiredState_manifest_container_resources.newFromDict(data.get('resources', {})),
                ports = [Pod_desiredState_manifest_container_port.newFromDict(port) for port in (data.get('ports',{}) if (data.get('ports',{}) is not None) else {})],
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod_desiredState_manifest_container(
                imagePullPolicy=data.get('imagePullPolicy', None),
                terminationMessagePath=data.get('terminationMessagePath', None),
                image=data.get('image', None),
#                capabilities=Pod_desiredState_manifest_container_capabilities.newFromDict(data.get('capabilities', {})),
#                resources=Pod_desiredState_manifest_container_resources.newFromDict(data.get('resources', {})),
                ports = [Pod_desiredState_manifest_container_port.newFromDict(port) for port in (data.get('ports',{}) if (data.get('ports',{}) is not None) else {})],
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Pod_desiredState_manifest_container.newFromDict(json_data)
class Pod_desiredState_manifest_restartPolicy(object):
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
            return Pod_desiredState_manifest_restartPolicy(
#                always=Pod_desiredState_manifest_restartPolicy_always.newFromDict(data.get('always', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod_desiredState_manifest_restartPolicy(
#                always=Pod_desiredState_manifest_restartPolicy_always.newFromDict(data.get('always', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Pod_desiredState_manifest_restartPolicy.newFromDict(json_data)
class Pod_currentState(object):
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
            return Pod_currentState(
                status=data.get('status', None),
                manifest=Pod_currentState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod_currentState(
                status=data.get('status', None),
                manifest=Pod_currentState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Pod_currentState.newFromDict(json_data)
class Pod_desiredState_manifest(object):
    def __init__(self,**kwargs):
        params = {
            'containers':None,
            'version':None,
            'restartPolicy':None,
            'volumes':None,
            'id':None,
            'dnsPolicy':None,
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
            return Pod_desiredState_manifest(
                containers = [Pod_desiredState_manifest_container.newFromDict(container) for container in (data.get('containers',{}) if (data.get('containers',{}) is not None) else {})],
                version=data.get('version', None),
                restartPolicy=Pod_desiredState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                volumes=data.get('volumes', None),
                id=data.get('id', None),
                dnsPolicy=data.get('dnsPolicy', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod_desiredState_manifest(
                containers = [Pod_desiredState_manifest_container.newFromDict(container) for container in (data.get('containers',{}) if (data.get('containers',{}) is not None) else {})],
                version=data.get('version', None),
                restartPolicy=Pod_desiredState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                volumes=data.get('volumes', None),
                id=data.get('id', None),
                dnsPolicy=data.get('dnsPolicy', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Pod_desiredState_manifest.newFromDict(json_data)
class Pod_currentState_manifest(object):
    def __init__(self,**kwargs):
        params = {
            'id':None,
            'version':None,
            'restartPolicy':None,
            'containers':None,
            'volumes':None,
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
            return Pod_currentState_manifest(
                id=data.get('id', None),
                version=data.get('version', None),
#                restartPolicy=Pod_currentState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                containers=data.get('containers', None),
                volumes=data.get('volumes', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod_currentState_manifest(
                id=data.get('id', None),
                version=data.get('version', None),
#                restartPolicy=Pod_currentState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                containers=data.get('containers', None),
                volumes=data.get('volumes', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Pod_currentState_manifest.newFromDict(json_data)
class Pod_desiredState_manifest_container_port(object):
    def __init__(self,**kwargs):
        params = {
            'hostPort':None,
            'containerPort':None,
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
            return Pod_desiredState_manifest_container_port(
                hostPort=data.get('hostPort', None),
                containerPort=data.get('containerPort', None),
                protocol=data.get('protocol', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod_desiredState_manifest_container_port(
                hostPort=data.get('hostPort', None),
                containerPort=data.get('containerPort', None),
                protocol=data.get('protocol', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Pod_desiredState_manifest_container_port.newFromDict(json_data)
class Pod_labels(object):
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
            return Pod_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Pod_labels.newFromDict(json_data)
class Pod(object):
    def __init__(self,**kwargs):
        params = {
            'id':None,
            'creationTimestamp':None,
            'currentState':None,
            'labels':None,
            'kind':None,
            'apiVersion':None,
            'selfLink':None,
            'namespace':None,
            'desiredState':None,
            'generateName':None,
            'resourceVersion':None,
            'uid':None,
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
            return Pod(
                id=data.get('id', None),
                creationTimestamp=data.get('creationTimestamp', None),
                currentState=Pod_currentState.newFromDict(data.get('currentState', {})),
                labels=Pod_labels.newFromDict(data.get('labels', {})),
                kind=data.get('kind', None),
                apiVersion=data.get('apiVersion', None),
                selfLink=data.get('selfLink', None),
                namespace=data.get('namespace', None),
                desiredState=Pod_desiredState.newFromDict(data.get('desiredState', {})),
                generateName=data.get('generateName', None),
                resourceVersion=data.get('resourceVersion', None),
                uid=data.get('uid', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Pod(
                id=data.get('id', None),
                creationTimestamp=data.get('creationTimestamp', None),
                currentState=Pod_currentState.newFromDict(data.get('currentState', {})),
                labels=Pod_labels.newFromDict(data.get('labels', {})),
                kind=data.get('kind', None),
                apiVersion=data.get('apiVersion', None),
                selfLink=data.get('selfLink', None),
                namespace=data.get('namespace', None),
                desiredState=Pod_desiredState.newFromDict(data.get('desiredState', {})),
                generateName=data.get('generateName', None),
                resourceVersion=data.get('resourceVersion', None),
                uid=data.get('uid', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Pod.newFromDict(json_data)