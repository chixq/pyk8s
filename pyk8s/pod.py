#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson as json
except ImportError:
    import json

from pyk8s.exceptions import PyK8SError


class TypeMeta(object):
    def __init__(self, **kwargs):
        params = {
            'id': None,
            'uid': None,
            'createTimeStamp': None,
            'selfLink': None,
            'resourceVersion': None,
            'namespace': None,
            'annotations': None,
            'apiVersion': None
        }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))


    def toDict(self):
        return self.__dict__

    def toJson(self):
        return json.dumps(self.toDict(), sort_keys=True)

    @staticmethod
    def newFromDict(data):
        if not isinstance(data, dict):
            raise PyK8SError('Type dict required')
        else:
            return TypeMeta(id=data.get('id', None),
                            uid=data.get('uid', None),
                            createTimeStamp=data.get('createTimeStamp', None),
                            selfLink=data.get('selfLink', None),
                            resourceVersion=data.get('resourceVersion', None),
                            namespace=data.get('namespace', None),
                            annotation=data.get('annotation', None),
                            apiVersion=data.get('apiVersion', None))


    @staticmethod
    def newFromJson(jsonStr):
        try:
            data = json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is valid,' + str(ex))

        return TypeMeta(id=data.get('id', None),
                        uid=data.get('uid', None),
                        createTimeStamp=data.get('createTimeStamp', None),
                        selfLink=data.get('selfLink', None),
                        resourceVersion=data.get('resourceVersion', None),
                        namespace=data.get('namespace', None),
                        annotation=data.get('annotation', None),
                        apiVersion=data.get('apiVersion', None))





class Port(object):
    def __init__(self, **kwargs):
        params = {
            'hostPort': None,
            'containerPort': None,
            'protocolPort': None
        }

        for (attribute, default_params) in params.iteritems():
            setattr(attribute, kwargs.get(attribute, default_params))

    def toDict(self):
        return self.__dict__

    def toJson(self):
        return json.dumps(self.toDict(), sort_keys=True)

    @staticmethod
    def newFromDict(data):
        if not isinstance(data, dict):
            raise PyK8SError('Type dict required')
        else:
            return Port(
                hostPort=data.get('hostPort', None),
                containerPort=data.get('containerPort', None),
                protocol=data.get('protocol', None)
            )


class LivenessProbe(object):
    def __init__(self, **kwargs):
        params = {
            'httpGet': None,
            'initialDelaySeconds': None,
            'timeoutSeconds': None
        }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        return self.__dict__

    def toJson(self):
        return json.dumps(self.toDict(), sort_keys=True)

    @staticmethod
    def newFromDict(data):
        if not isinstance(data, dict):
            raise PyK8SError('Type dict required')
        else:
            return LivenessProbe(
                httpGet=data.get('httpGet', None),
                initialDelaySeconds=data.get('initialDelaySeconds', None),
                timeoutSeconds=data.get('timeoutSeconds', None)
            )


class Container(object):
    def __init__(self, **kwargs):
        params = {
            'name': None,
            'image': None,
            'ports': None,
            'resources': None,
            'livenessProbe': None,
            'terminationMessagePath': None,
            'imagePullPolicy': None,
            'capability': None
        }

        for (attribute, default_value) in params.iteritems():
            setattr(attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        return self.__dict__

    def toJson(self):
        return json.dumps(self.toDict(), sort_keys=True)

    @staticmethod
    def newFromDict(data):
        if isinstance(data, dict):
            raise PyK8SError('Type dict required')
        else:
            ports = [Port.newFromDict(port) for port in data.get('ports', {})]
            livenessProbe = [LivenessProbe.newFromDict(livenessProbe) for livenessProbe in data['livenessProbe']]
            return Container(
                name=data.get('name', None),
                image=data.get('image', None),
                ports=ports,
                resources=data.get('resources', None),
                livenessProbe=livenessProbe,
                terminationMessagePath=data.get('terminationMessagePath', None),
                imagePullPolicy=data.get('imagePullPolicy', None),
                capabilities=data.get('capabilities', None)
            )


class Manifest(object):
    def __init__(self, **kwargs):
        params = {
            'version': None,
            'id': None,
            'volumes': None,
            'containers': None,
            'restartPolicy': None,
            'dnsPolicy': None
        }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        return self.__dict__

    def toJson(self):
        return json.dumps(self.toDict(), sort_keys=True)

    @staticmethod
    def newFromDict(data):
        if isinstance(data, dict):
            raise PyK8SError('Type dict required')
        else:
            containers = [Container.newFromDict(container) for container in data.get('containers', {})]
            return Manifest(
                version=data.get('version', None),
                id=data.get('id', None),
                volumes=data.get('volumes', None),
                containers=containers,
                restartPolicy=data.get('restartPolicy', None),
                dnsPolicy=data.get('dnsPolicy', None)
            )


class PodState(object):
    def __init__(self, **kwargs):
        params = {
            'manifest': None,
            'status': None,
            'Condition': None,
            'host': None,
            'hostIP': None,
            'podIP': None,
            'info': None
        }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))

    def toDict(self):
        return self.__dict__

    def toJson(self):
        return json.dumps(self.toDict(), sort_keys=True)

    @staticmethod
    def newFromDict(data):

        if isinstance(data, dict):
            raise PyK8SError('Type dict required')
        else:
            manifest = Manifest.newFromDict(data.get('manifest', {}))
            return PodState(
                manifest=manifest,
                status=data.get('status', None),
                Condition=data.get('Condition', None),
                host=data.get('host', None),
                podIP=data.get('podIP', None),
                info=data.get('info', {}),
            )

class Pod(TypeMeta):
    def __init__(self, **kwargs):
        params = {
            'label': None,
            'desiredState': None,
            'currentState': None
        }
        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))
        super(Pod, self).__init__(**kwargs)

    @staticmethod
    def newFromDict(data):
        if not isinstance(data, dict):
            raise PyK8SError('Type dict required')
        else:
            return Pod(lable=data.get('label', None),
                       desiredState=data.get('desiredState', None),
                       currentState=data.get('desiredState', None))

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data = json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))

        return Pod(lable=data.get('label', None),
                   desiredState=data.get('desiredState', None),
                   currentState=data.get('desiredState', None))


class PodList(TypeMeta):

    def __init__(self, **kwargs):
        params = {
            'items': None
        }

        for (attribute, default_value) in params.iteritems():
            setattr(self, attribute, kwargs.get(attribute, default_value))
        super(PodList, self).__init__(**kwargs)

    @staticmethod
    def newFromDict(data):
        if not isinstance(data, dict):
            raise PyK8SError('Type dict required')
        else:
            pods = [Pod.newFromDict(pod) for pod in data.get('items', {})]
            return PodList(
                kind='PodList',
                createTimestamp=data.get('createTimestamp', None),
                selfLink=data.get('selfLink', None),
                resourceVersion=data.get('resourceVersion', None),
                apiVersion=data.get('apiVersion', None),
                items=pods
            )

    @staticmethod
    def newFromJson(jsonStr):
        try:
            data = json.loads(jsonStr)
        except ValueError as ex:
            raise PyK8SError('Input json is not valid, ' + str(ex))

        pods = [Pod.newFromDict(pod) for pod in data.get('items', {})]
        return PodList(
            kind='PodList',
            createTimestamp=data.get('createTimestamp', None),
            selfLink=data.get('selfLink', None),
            resourceVersion=data.get('resourceVersion', None),
            apiVersion=data.get('apiVersion', None),
            items=pods
        )


if __name__ == '__main__':
    typeMeta = TypeMeta(id=1)
    print typeMeta.id

    pod = Pod(id=1, label=1, desiredState=2)
    print pod.toDict()
