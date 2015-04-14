#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class ReplicationController_desiredState(object):
    def __init__(self,**kwargs):
        params = {
            'replicas':None,
            'replicaSelector':None,
            'podTemplate':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['replicaSelector']=self.replicaSelector.toDict();
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
            return ReplicationController_desiredState(
                replicas=data.get('replicas', None),
                replicaSelector=ReplicationController_desiredState_replicaSelector.newFromDict(data.get('replicaSelector', {})),
                podTemplate=ReplicationController_desiredState_podTemplate.newFromDict(data.get('podTemplate', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_desiredState(
                replicas=data.get('replicas', None),
                replicaSelector=ReplicationController_desiredState_replicaSelector.newFromDict(data.get('replicaSelector', {})),
                podTemplate=ReplicationController_desiredState_podTemplate.newFromDict(data.get('podTemplate', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_desiredState.newFromDict(json_data)
class ReplicationController_currentState_podTemplate_desiredState(object):
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
            return ReplicationController_currentState_podTemplate_desiredState(
                manifest=ReplicationController_currentState_podTemplate_desiredState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_currentState_podTemplate_desiredState(
                manifest=ReplicationController_currentState_podTemplate_desiredState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_currentState_podTemplate_desiredState.newFromDict(json_data)
class ReplicationController_desiredState_podTemplate_desiredState_manifest(object):
    def __init__(self,**kwargs):
        params = {
            'restartPolicy':None,
            'dnsPolicy':None,
            'id':None,
            'version':None,
            'containers':None,
            'volumes':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['restartPolicy']=self.restartPolicy.toDict();
        i=0
        for container in self.containers:
            params['containers'][i]=container.toDict();
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
            return ReplicationController_desiredState_podTemplate_desiredState_manifest(
                restartPolicy=ReplicationController_desiredState_podTemplate_desiredState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                dnsPolicy=data.get('dnsPolicy', None),
                id=data.get('id', None),
                version=data.get('version', None),
                containers = [ReplicationController_desiredState_podTemplate_desiredState_manifest_container.newFromDict(container) for container in (data.get('containers',{}) if (data.get('containers',{}) is not None) else {})],
                volumes=data.get('volumes', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_desiredState_podTemplate_desiredState_manifest(
                restartPolicy=ReplicationController_desiredState_podTemplate_desiredState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                dnsPolicy=data.get('dnsPolicy', None),
                id=data.get('id', None),
                version=data.get('version', None),
                containers = [ReplicationController_desiredState_podTemplate_desiredState_manifest_container.newFromDict(container) for container in (data.get('containers',{}) if (data.get('containers',{}) is not None) else {})],
                volumes=data.get('volumes', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_desiredState_podTemplate_desiredState_manifest.newFromDict(json_data)
class ReplicationController_desiredState_podTemplate_desiredState_manifest_restartPolicy(object):
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
            return ReplicationController_desiredState_podTemplate_desiredState_manifest_restartPolicy(
#                always=ReplicationController_desiredState_podTemplate_desiredState_manifest_restartPolicy_always.newFromDict(data.get('always', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_desiredState_podTemplate_desiredState_manifest_restartPolicy(
#                always=ReplicationController_desiredState_podTemplate_desiredState_manifest_restartPolicy_always.newFromDict(data.get('always', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_desiredState_podTemplate_desiredState_manifest_restartPolicy.newFromDict(json_data)
class ReplicationController_desiredState_podTemplate_desiredState_manifest_container_port(object):
    def __init__(self,**kwargs):
        params = {
            'containerPort':None,
            'protocol':None,
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
            return ReplicationController_desiredState_podTemplate_desiredState_manifest_container_port(
                containerPort=data.get('containerPort', None),
                protocol=data.get('protocol', None),
                hostPort=data.get('hostPort', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_desiredState_podTemplate_desiredState_manifest_container_port(
                containerPort=data.get('containerPort', None),
                protocol=data.get('protocol', None),
                hostPort=data.get('hostPort', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_desiredState_podTemplate_desiredState_manifest_container_port.newFromDict(json_data)
class ReplicationController_currentState_podTemplate_desiredState_manifest(object):
    def __init__(self,**kwargs):
        params = {
            'id':None,
            'restartPolicy':None,
            'containers':None,
            'volumes':None,
            'version':None,
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
            return ReplicationController_currentState_podTemplate_desiredState_manifest(
                id=data.get('id', None),
#                restartPolicy=ReplicationController_currentState_podTemplate_desiredState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                containers=data.get('containers', None),
                volumes=data.get('volumes', None),
                version=data.get('version', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_currentState_podTemplate_desiredState_manifest(
                id=data.get('id', None),
#                restartPolicy=ReplicationController_currentState_podTemplate_desiredState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                containers=data.get('containers', None),
                volumes=data.get('volumes', None),
                version=data.get('version', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_currentState_podTemplate_desiredState_manifest.newFromDict(json_data)
class ReplicationController_desiredState_podTemplate(object):
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
            return ReplicationController_desiredState_podTemplate(
                labels=ReplicationController_desiredState_podTemplate_labels.newFromDict(data.get('labels', {})),
                desiredState=ReplicationController_desiredState_podTemplate_desiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_desiredState_podTemplate(
                labels=ReplicationController_desiredState_podTemplate_labels.newFromDict(data.get('labels', {})),
                desiredState=ReplicationController_desiredState_podTemplate_desiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_desiredState_podTemplate.newFromDict(json_data)
class ReplicationController_desiredState_podTemplate_labels(object):
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
            return ReplicationController_desiredState_podTemplate_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_desiredState_podTemplate_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_desiredState_podTemplate_labels.newFromDict(json_data)
class ReplicationController_labels(object):
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
            return ReplicationController_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_labels.newFromDict(json_data)
class ReplicationController_desiredState_replicaSelector(object):
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
            return ReplicationController_desiredState_replicaSelector(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_desiredState_replicaSelector(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_desiredState_replicaSelector.newFromDict(json_data)
class ReplicationController_currentState_podTemplate(object):
    def __init__(self,**kwargs):
        params = {
            'desiredState':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
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
            return ReplicationController_currentState_podTemplate(
                desiredState=ReplicationController_currentState_podTemplate_desiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_currentState_podTemplate(
                desiredState=ReplicationController_currentState_podTemplate_desiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_currentState_podTemplate.newFromDict(json_data)
class ReplicationController_currentState(object):
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
            return ReplicationController_currentState(
                replicas=data.get('replicas', None),
                podTemplate=ReplicationController_currentState_podTemplate.newFromDict(data.get('podTemplate', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_currentState(
                replicas=data.get('replicas', None),
                podTemplate=ReplicationController_currentState_podTemplate.newFromDict(data.get('podTemplate', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_currentState.newFromDict(json_data)
class ReplicationController_desiredState_podTemplate_desiredState(object):
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
            return ReplicationController_desiredState_podTemplate_desiredState(
                manifest=ReplicationController_desiredState_podTemplate_desiredState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_desiredState_podTemplate_desiredState(
                manifest=ReplicationController_desiredState_podTemplate_desiredState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_desiredState_podTemplate_desiredState.newFromDict(json_data)
class ReplicationController(object):
    def __init__(self,**kwargs):
        params = {
            'apiVersion':None,
            'selfLink':None,
            'uid':None,
            'desiredState':None,
            'creationTimestamp':None,
            'id':None,
            'resourceVersion':None,
            'namespace':None,
            'currentState':None,
            'kind':None,
            'labels':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
        params['desiredState']=self.desiredState.toDict();
        params['currentState']=self.currentState.toDict();
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
            return ReplicationController(
                apiVersion=data.get('apiVersion', None),
                selfLink=data.get('selfLink', None),
                uid=data.get('uid', None),
                desiredState=ReplicationController_desiredState.newFromDict(data.get('desiredState', {})),
                creationTimestamp=data.get('creationTimestamp', None),
                id=data.get('id', None),
                resourceVersion=data.get('resourceVersion', None),
                namespace=data.get('namespace', None),
                currentState=ReplicationController_currentState.newFromDict(data.get('currentState', {})),
                kind=data.get('kind', None),
                labels=ReplicationController_labels.newFromDict(data.get('labels', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController(
                apiVersion=data.get('apiVersion', None),
                selfLink=data.get('selfLink', None),
                uid=data.get('uid', None),
                desiredState=ReplicationController_desiredState.newFromDict(data.get('desiredState', {})),
                creationTimestamp=data.get('creationTimestamp', None),
                id=data.get('id', None),
                resourceVersion=data.get('resourceVersion', None),
                namespace=data.get('namespace', None),
                currentState=ReplicationController_currentState.newFromDict(data.get('currentState', {})),
                kind=data.get('kind', None),
                labels=ReplicationController_labels.newFromDict(data.get('labels', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController.newFromDict(json_data)
class ReplicationController_desiredState_podTemplate_desiredState_manifest_container(object):
    def __init__(self,**kwargs):
        params = {
            'ports':None,
            'terminationMessagePath':None,
            'image':None,
            'capabilities':None,
            'name':None,
            'resources':None,
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
            return ReplicationController_desiredState_podTemplate_desiredState_manifest_container(
                ports = [ReplicationController_desiredState_podTemplate_desiredState_manifest_container_port.newFromDict(port) for port in (data.get('ports',{}) if (data.get('ports',{}) is not None) else {})],
                terminationMessagePath=data.get('terminationMessagePath', None),
                image=data.get('image', None),
#                capabilities=ReplicationController_desiredState_podTemplate_desiredState_manifest_container_capabilities.newFromDict(data.get('capabilities', {})),
                name=data.get('name', None),
#                resources=ReplicationController_desiredState_podTemplate_desiredState_manifest_container_resources.newFromDict(data.get('resources', {})),
                imagePullPolicy=data.get('imagePullPolicy', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return ReplicationController_desiredState_podTemplate_desiredState_manifest_container(
                ports = [ReplicationController_desiredState_podTemplate_desiredState_manifest_container_port.newFromDict(port) for port in (data.get('ports',{}) if (data.get('ports',{}) is not None) else {})],
                terminationMessagePath=data.get('terminationMessagePath', None),
                image=data.get('image', None),
#                capabilities=ReplicationController_desiredState_podTemplate_desiredState_manifest_container_capabilities.newFromDict(data.get('capabilities', {})),
                name=data.get('name', None),
#                resources=ReplicationController_desiredState_podTemplate_desiredState_manifest_container_resources.newFromDict(data.get('resources', {})),
                imagePullPolicy=data.get('imagePullPolicy', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return ReplicationController_desiredState_podTemplate_desiredState_manifest_container.newFromDict(json_data)