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

class EndpointMixin(object):
    #-------bindings-----
    def getBindings(self):
        response = self.get('bindings')
        return Bindings.newFromDict(response)

    def postBindings(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('bindings',params)

    def addBindings(self,ob):
        if not isinstance(ob,Bindings):
            raise PyK8SError('Type Bindings required')
        return self.postBindings(ob.toDict())

    #-------event-----
    def getEvent(self,name):
        response = self.get('events/'+name)
        return Event.newFromDict(response)

    def postEvent(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('events/'+name,params)

    def addEvent(self,name,ob):
        if not isinstance(ob,Event):
            raise PyK8SError('Type Event required')
        return self.postEvent(name,ob.toDict())

    #-------events-----
    def getEvents(self):
        response = self.get('events')
        return Events.newFromDict(response)

    def postEvents(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('events',params)

    def addEvents(self,ob):
        if not isinstance(ob,Events):
            raise PyK8SError('Type Events required')
        return self.postEvents(ob.toDict())

    #-------limitrange-----
    def getLimitrange(self,name):
        response = self.get('limitranges/'+name)
        return Limitrange.newFromDict(response)

    def postLimitrange(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('limitranges/'+name,params)

    def addLimitrange(self,name,ob):
        if not isinstance(ob,Limitrange):
            raise PyK8SError('Type Limitrange required')
        return self.postLimitrange(name,ob.toDict())

    #-------limitranges-----
    def getLimitranges(self):
        response = self.get('limitranges')
        return Limitranges.newFromDict(response)

    def postLimitranges(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('limitranges',params)

    def addLimitranges(self,ob):
        if not isinstance(ob,Limitranges):
            raise PyK8SError('Type Limitranges required')
        return self.postLimitranges(ob.toDict())

    #-------node-----
    def getNode(self,name):
        response = self.get('nodes/'+name)
        return Node.newFromDict(response)

    def postNode(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('nodes/'+name,params)

    def addNode(self,name,ob):
        if not isinstance(ob,Node):
            raise PyK8SError('Type Node required')
        return self.postNode(name,ob.toDict())

    #-------nodes-----
    def getNodes(self):
        response = self.get('nodes')
        return Nodes.newFromDict(response)

    def postNodes(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('nodes',params)

    def addNodes(self,ob):
        if not isinstance(ob,Nodes):
            raise PyK8SError('Type Nodes required')
        return self.postNodes(ob.toDict())

    #-------pod-----
    def getPod(self,name):
        response = self.get('pods/'+name)
        return Pod.newFromDict(response)

    def postPod(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('pods/'+name,params)

    def addPod(self,name,ob):
        if not isinstance(ob,Pod):
            raise PyK8SError('Type Pod required')
        return self.postPod(name,ob.toDict())

    #-------pods-----
    def getPods(self):
        response = self.get('pods')
        return Pods.newFromDict(response)

    def postPods(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('pods',params)

    def addPods(self,ob):
        if not isinstance(ob,Pods):
            raise PyK8SError('Type Pods required')
        return self.postPods(ob.toDict())

    #-------replicationcontroller-----
    def getReplicationcontroller(self,name):
        response = self.get('replicationcontrollers/'+name)
        return Replicationcontroller.newFromDict(response)

    def postReplicationcontroller(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('replicationcontrollers/'+name,params)

    def addReplicationcontroller(self,name,ob):
        if not isinstance(ob,Replicationcontroller):
            raise PyK8SError('Type Replicationcontroller required')
        return self.postReplicationcontroller(name,ob.toDict())

    #-------replicationcontrollers-----
    def getReplicationcontrollers(self):
        response = self.get('replicationcontrollers')
        return Replicationcontrollers.newFromDict(response)

    def postReplicationcontrollers(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('replicationcontrollers',params)

    def addReplicationcontrollers(self,ob):
        if not isinstance(ob,Replicationcontrollers):
            raise PyK8SError('Type Replicationcontrollers required')
        return self.postReplicationcontrollers(ob.toDict())

    #-------resourcequota-----
    def getResourcequota(self,name):
        response = self.get('resourcequotas/'+name)
        return Resourcequota.newFromDict(response)

    def postResourcequota(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('resourcequotas/'+name,params)

    def addResourcequota(self,name,ob):
        if not isinstance(ob,Resourcequota):
            raise PyK8SError('Type Resourcequota required')
        return self.postResourcequota(name,ob.toDict())

    #-------resourcequotas-----
    def getResourcequotas(self):
        response = self.get('resourcequotas')
        return Resourcequotas.newFromDict(response)

    def postResourcequotas(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('resourcequotas',params)

    def addResourcequotas(self,ob):
        if not isinstance(ob,Resourcequotas):
            raise PyK8SError('Type Resourcequotas required')
        return self.postResourcequotas(ob.toDict())

    #-------service-----
    def getService(self,name):
        response = self.get('services/'+name)
        return Service.newFromDict(response)

    def postService(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('services/'+name,params)

    def addService(self,name,ob):
        if not isinstance(ob,Service):
            raise PyK8SError('Type Service required')
        return self.postService(name,ob.toDict())

    #-------services-----
    def getServices(self):
        response = self.get('services')
        return Services.newFromDict(response)

    def postServices(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('services',params)

    def addServices(self,ob):
        if not isinstance(ob,Services):
            raise PyK8SError('Type Services required')
        return self.postServices(ob.toDict())

