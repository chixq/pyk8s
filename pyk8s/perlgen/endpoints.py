#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyk8s.exceptions import PyK8SError
from pyk8s.pods import Pods
from pyk8s.nodes import Nodes
from pyk8s.services import Services
from pyk8s.events import Events
from pyk8s.limitranges import Limitranges
from pyk8s.replicationcontrollers import Replicationcontrollers
from pyk8s.resourcequotas import Resourcequotas
from pyk8s.pod import Pod
from pyk8s.node import Node
from pyk8s.service import Service
from pyk8s.event import Event
from pyk8s.limitrange import Limitrange
from pyk8s.replicationcontroller import Replicationcontroller
from pyk8s.resourcequota import Resourcequota
from pyk8s.bindings import Bindings

class EndpointMixin(object):
    #-------bindings-----
    def getBindings(self):
        response = self.get('bindings')
        return Bindings.newFromDict(response)

    #-------event-----
    def getEvent(self,name):
        response = self.get('events/'+name)
        return Event.newFromDict(response)

    def postEvent(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('events/',params)

    def addEvent(self,ob):
        if not isinstance(ob,Event):
            raise PyK8SError('Type Event required')
        return self.postEvent(ob.toDict())

    def addEventFromFile(self,filename):
        ob=Event.newFromJsonFile(filename)
        return self.postEvent(ob.toDict())

    #-------events-----
    def getEvents(self):
        response = self.get('events')
        return Events.newFromDict(response)

    #-------limitRange-----
    def getLimitRange(self,name):
        response = self.get('limitRanges/'+name)
        return LimitRange.newFromDict(response)

    def postLimitRange(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('limitRanges/',params)

    def addLimitRange(self,ob):
        if not isinstance(ob,LimitRange):
            raise PyK8SError('Type LimitRange required')
        return self.postLimitRange(ob.toDict())

    def addLimitRangeFromFile(self,filename):
        ob=LimitRange.newFromJsonFile(filename)
        return self.postLimitRange(ob.toDict())

    #-------limitRanges-----
    def getLimitRanges(self):
        response = self.get('limitRanges')
        return LimitRanges.newFromDict(response)

    #-------node-----
    def getNode(self,name):
        response = self.get('nodes/'+name)
        return Node.newFromDict(response)

    def postNode(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('nodes/',params)

    def addNode(self,ob):
        if not isinstance(ob,Node):
            raise PyK8SError('Type Node required')
        return self.postNode(ob.toDict())

    def addNodeFromFile(self,filename):
        ob=Node.newFromJsonFile(filename)
        return self.postNode(ob.toDict())

    #-------nodes-----
    def getNodes(self):
        response = self.get('nodes')
        return Nodes.newFromDict(response)

    #-------pod-----
    def getPod(self,name):
        response = self.get('pods/'+name)
        return Pod.newFromDict(response)

    def postPod(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('pods/',params)

    def addPod(self,ob):
        if not isinstance(ob,Pod):
            raise PyK8SError('Type Pod required')
        return self.postPod(ob.toDict())

    def addPodFromFile(self,filename):
        ob=Pod.newFromJsonFile(filename)
        return self.postPod(ob.toDict())

    #-------pods-----
    def getPods(self):
        response = self.get('pods')
        return Pods.newFromDict(response)

    #-------replicationController-----
    def getReplicationController(self,name):
        response = self.get('replicationControllers/'+name)
        return ReplicationController.newFromDict(response)

    def postReplicationController(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('replicationControllers/',params)

    def addReplicationController(self,ob):
        if not isinstance(ob,ReplicationController):
            raise PyK8SError('Type ReplicationController required')
        return self.postReplicationController(ob.toDict())

    def addReplicationControllerFromFile(self,filename):
        ob=ReplicationController.newFromJsonFile(filename)
        return self.postReplicationController(ob.toDict())

    #-------replicationControllers-----
    def getReplicationControllers(self):
        response = self.get('replicationControllers')
        return ReplicationControllers.newFromDict(response)

    #-------resourceQuota-----
    def getResourceQuota(self,name):
        response = self.get('resourceQuotas/'+name)
        return ResourceQuota.newFromDict(response)

    def postResourceQuota(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('resourceQuotas/',params)

    def addResourceQuota(self,ob):
        if not isinstance(ob,ResourceQuota):
            raise PyK8SError('Type ResourceQuota required')
        return self.postResourceQuota(ob.toDict())

    def addResourceQuotaFromFile(self,filename):
        ob=ResourceQuota.newFromJsonFile(filename)
        return self.postResourceQuota(ob.toDict())

    #-------resourceQuotas-----
    def getResourceQuotas(self):
        response = self.get('resourceQuotas')
        return ResourceQuotas.newFromDict(response)

    #-------service-----
    def getService(self,name):
        response = self.get('services/'+name)
        return Service.newFromDict(response)

    def postService(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('services/',params)

    def addService(self,ob):
        if not isinstance(ob,Service):
            raise PyK8SError('Type Service required')
        return self.postService(ob.toDict())

    def addServiceFromFile(self,filename):
        ob=Service.newFromJsonFile(filename)
        return self.postService(ob.toDict())

    #-------services-----
    def getServices(self):
        response = self.get('services')
        return Services.newFromDict(response)

