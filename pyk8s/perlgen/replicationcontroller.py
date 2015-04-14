#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json
import copy
from pyk8s.exceptions import PyK8SError

class Replicationcontroller(object):
    def __init__(self,**kwargs):
        params = {
            'creationTimestamp':None,
            'selfLink':None,
            'apiVersion':None,
            'id':None,
            'kind':None,
            'currentState':None,
            'labels':None,
            'uid':None,
            'namespace':None,
            'resourceVersion':None,
            'desiredState':None,
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
                creationTimestamp=data.get('creationTimestamp', None),
                selfLink=data.get('selfLink', None),
                apiVersion=data.get('apiVersion', None),
                id=data.get('id', None),
                kind=data.get('kind', None),
                currentState=Replicationcontroller_currentState.newFromDict(data.get('currentState', {})),
                labels=Replicationcontroller_labels.newFromDict(data.get('labels', {})),
                uid=data.get('uid', None),
                namespace=data.get('namespace', None),
                resourceVersion=data.get('resourceVersion', None),
                desiredState=Replicationcontroller_desiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller(
                creationTimestamp=data.get('creationTimestamp', None),
                selfLink=data.get('selfLink', None),
                apiVersion=data.get('apiVersion', None),
                id=data.get('id', None),
                kind=data.get('kind', None),
                currentState=Replicationcontroller_currentState.newFromDict(data.get('currentState', {})),
                labels=Replicationcontroller_labels.newFromDict(data.get('labels', {})),
                uid=data.get('uid', None),
                namespace=data.get('namespace', None),
                resourceVersion=data.get('resourceVersion', None),
                desiredState=Replicationcontroller_desiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller.newFromDict(json_data)
class Replicationcontroller_currentState_podTemplate(object):
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
            return Replicationcontroller_currentState_podTemplate(
                desiredState=Replicationcontroller_currentState_podTemplate_desiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_currentState_podTemplate(
                desiredState=Replicationcontroller_currentState_podTemplate_desiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_currentState_podTemplate.newFromDict(json_data)
class Replicationcontroller_currentState_podTemplate_desiredState(object):
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
            return Replicationcontroller_currentState_podTemplate_desiredState(
                manifest=Replicationcontroller_currentState_podTemplate_desiredState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_currentState_podTemplate_desiredState(
                manifest=Replicationcontroller_currentState_podTemplate_desiredState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_currentState_podTemplate_desiredState.newFromDict(json_data)
class Replicationcontroller_desiredState_podTemplate_desiredState_manifest_restartPolicy(object):
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
            return Replicationcontroller_desiredState_podTemplate_desiredState_manifest_restartPolicy(
#                always=Replicationcontroller_desiredState_podTemplate_desiredState_manifest_restartPolicy_always.newFromDict(data.get('always', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_desiredState_podTemplate_desiredState_manifest_restartPolicy(
#                always=Replicationcontroller_desiredState_podTemplate_desiredState_manifest_restartPolicy_always.newFromDict(data.get('always', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_desiredState_podTemplate_desiredState_manifest_restartPolicy.newFromDict(json_data)
class Replicationcontroller_desiredState_replicaSelector(object):
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
            return Replicationcontroller_desiredState_replicaSelector(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_desiredState_replicaSelector(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_desiredState_replicaSelector.newFromDict(json_data)
class Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container(object):
    def __init__(self,**kwargs):
        params = {
            'capabilities':None,
            'image':None,
            'terminationMessagePath':None,
            'resources':None,
            'name':None,
            'imagePullPolicy':None,
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
            return Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container(
#                capabilities=Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container_capabilities.newFromDict(data.get('capabilities', {})),
                image=data.get('image', None),
                terminationMessagePath=data.get('terminationMessagePath', None),
#                resources=Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container_resources.newFromDict(data.get('resources', {})),
                name=data.get('name', None),
                imagePullPolicy=data.get('imagePullPolicy', None),
                ports = [Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container_port.newFromDict(port) for port in (data.get('ports',{}) if (data.get('ports',{}) is not None) else {})],
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container(
#                capabilities=Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container_capabilities.newFromDict(data.get('capabilities', {})),
                image=data.get('image', None),
                terminationMessagePath=data.get('terminationMessagePath', None),
#                resources=Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container_resources.newFromDict(data.get('resources', {})),
                name=data.get('name', None),
                imagePullPolicy=data.get('imagePullPolicy', None),
                ports = [Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container_port.newFromDict(port) for port in (data.get('ports',{}) if (data.get('ports',{}) is not None) else {})],
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container.newFromDict(json_data)
class Replicationcontroller_desiredState_podTemplate_labels(object):
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
            return Replicationcontroller_desiredState_podTemplate_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_desiredState_podTemplate_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_desiredState_podTemplate_labels.newFromDict(json_data)
class Replicationcontroller_desiredState(object):
    def __init__(self,**kwargs):
        params = {
            'replicas':None,
            'podTemplate':None,
            'replicaSelector':None,
         }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        params =copy.deepcopy(self.__dict__)
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
            return Replicationcontroller_desiredState(
                replicas=data.get('replicas', None),
                podTemplate=Replicationcontroller_desiredState_podTemplate.newFromDict(data.get('podTemplate', {})),
                replicaSelector=Replicationcontroller_desiredState_replicaSelector.newFromDict(data.get('replicaSelector', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_desiredState(
                replicas=data.get('replicas', None),
                podTemplate=Replicationcontroller_desiredState_podTemplate.newFromDict(data.get('podTemplate', {})),
                replicaSelector=Replicationcontroller_desiredState_replicaSelector.newFromDict(data.get('replicaSelector', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_desiredState.newFromDict(json_data)
class Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container_port(object):
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
            return Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container_port(
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
        return Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container_port(
                hostPort=data.get('hostPort', None),
                containerPort=data.get('containerPort', None),
                protocol=data.get('protocol', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container_port.newFromDict(json_data)
class Replicationcontroller_desiredState_podTemplate(object):
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
            return Replicationcontroller_desiredState_podTemplate(
                labels=Replicationcontroller_desiredState_podTemplate_labels.newFromDict(data.get('labels', {})),
                desiredState=Replicationcontroller_desiredState_podTemplate_desiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_desiredState_podTemplate(
                labels=Replicationcontroller_desiredState_podTemplate_labels.newFromDict(data.get('labels', {})),
                desiredState=Replicationcontroller_desiredState_podTemplate_desiredState.newFromDict(data.get('desiredState', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_desiredState_podTemplate.newFromDict(json_data)
class Replicationcontroller_currentState_podTemplate_desiredState_manifest(object):
    def __init__(self,**kwargs):
        params = {
            'restartPolicy':None,
            'id':None,
            'version':None,
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
            return Replicationcontroller_currentState_podTemplate_desiredState_manifest(
#                restartPolicy=Replicationcontroller_currentState_podTemplate_desiredState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                id=data.get('id', None),
                version=data.get('version', None),
                containers=data.get('containers', None),
                volumes=data.get('volumes', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_currentState_podTemplate_desiredState_manifest(
#                restartPolicy=Replicationcontroller_currentState_podTemplate_desiredState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                id=data.get('id', None),
                version=data.get('version', None),
                containers=data.get('containers', None),
                volumes=data.get('volumes', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_currentState_podTemplate_desiredState_manifest.newFromDict(json_data)
class Replicationcontroller_desiredState_podTemplate_desiredState(object):
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
            return Replicationcontroller_desiredState_podTemplate_desiredState(
                manifest=Replicationcontroller_desiredState_podTemplate_desiredState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_desiredState_podTemplate_desiredState(
                manifest=Replicationcontroller_desiredState_podTemplate_desiredState_manifest.newFromDict(data.get('manifest', {})),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_desiredState_podTemplate_desiredState.newFromDict(json_data)
class Replicationcontroller_currentState(object):
    def __init__(self,**kwargs):
        params = {
            'podTemplate':None,
            'replicas':None,
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
            return Replicationcontroller_currentState(
                podTemplate=Replicationcontroller_currentState_podTemplate.newFromDict(data.get('podTemplate', {})),
                replicas=data.get('replicas', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_currentState(
                podTemplate=Replicationcontroller_currentState_podTemplate.newFromDict(data.get('podTemplate', {})),
                replicas=data.get('replicas', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_currentState.newFromDict(json_data)
class Replicationcontroller_labels(object):
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
            return Replicationcontroller_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_labels(
                name=data.get('name', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_labels.newFromDict(json_data)
class Replicationcontroller_desiredState_podTemplate_desiredState_manifest(object):
    def __init__(self,**kwargs):
        params = {
            'volumes':None,
            'dnsPolicy':None,
            'containers':None,
            'restartPolicy':None,
            'id':None,
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
            return Replicationcontroller_desiredState_podTemplate_desiredState_manifest(
                volumes=data.get('volumes', None),
                dnsPolicy=data.get('dnsPolicy', None),
                containers = [Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container.newFromDict(container) for container in (data.get('containers',{}) if (data.get('containers',{}) is not None) else {})],
                restartPolicy=Replicationcontroller_desiredState_podTemplate_desiredState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                id=data.get('id', None),
                version=data.get('version', None),
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data=json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))
        return Replicationcontroller_desiredState_podTemplate_desiredState_manifest(
                volumes=data.get('volumes', None),
                dnsPolicy=data.get('dnsPolicy', None),
                containers = [Replicationcontroller_desiredState_podTemplate_desiredState_manifest_container.newFromDict(container) for container in (data.get('containers',{}) if (data.get('containers',{}) is not None) else {})],
                restartPolicy=Replicationcontroller_desiredState_podTemplate_desiredState_manifest_restartPolicy.newFromDict(data.get('restartPolicy', {})),
                id=data.get('id', None),
                version=data.get('version', None),
            )

    @staticmethod
    def newFromJsonFile(jsonfile):
        with open(jsonfile) as json_file:
            json_data = json.load(json_file)
        return Replicationcontroller_desiredState_podTemplate_desiredState_manifest.newFromDict(json_data)