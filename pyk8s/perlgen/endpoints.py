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

    #-------limitrange-----
    def getLimitrange(self,name):
        response = self.get('limitranges/'+name)
        return Limitrange.newFromDict(response)

    def postLimitrange(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('limitranges/',params)

    def addLimitrange(self,ob):
        if not isinstance(ob,Limitrange):
            raise PyK8SError('Type Limitrange required')
        return self.postLimitrange(ob.toDict())

    def addLimitrangeFromFile(self,filename):
        ob=Limitrange.newFromJsonFile(filename)
        return self.postLimitrange(ob.toDict())

    #-------limitranges-----
    def getLimitranges(self):
        response = self.get('limitranges')
        return Limitranges.newFromDict(response)

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

    #-------replicationcontroller-----
    def getReplicationcontroller(self,name):
        response = self.get('replicationcontrollers/'+name)
        return Replicationcontroller.newFromDict(response)

    def postReplicationcontroller(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('replicationcontrollers/',params)

    def addReplicationcontroller(self,ob):
        if not isinstance(ob,Replicationcontroller):
            raise PyK8SError('Type Replicationcontroller required')
        return self.postReplicationcontroller(ob.toDict())

    def addReplicationcontrollerFromFile(self,filename):
        ob=Replicationcontroller.newFromJsonFile(filename)
        return self.postReplicationcontroller(ob.toDict())

    #-------replicationcontrollers-----
    def getReplicationcontrollers(self):
        response = self.get('replicationcontrollers')
        return Replicationcontrollers.newFromDict(response)

    #-------resourcequota-----
    def getResourcequota(self,name):
        response = self.get('resourcequotas/'+name)
        return Resourcequota.newFromDict(response)

    def postResourcequota(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        return self.post('resourcequotas/',params)

    def addResourcequota(self,ob):
        if not isinstance(ob,Resourcequota):
            raise PyK8SError('Type Resourcequota required')
        return self.postResourcequota(ob.toDict())

    def addResourcequotaFromFile(self,filename):
        ob=Resourcequota.newFromJsonFile(filename)
        return self.postResourcequota(ob.toDict())

    #-------resourcequotas-----
    def getResourcequotas(self):
        response = self.get('resourcequotas')
        return Resourcequotas.newFromDict(response)

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

