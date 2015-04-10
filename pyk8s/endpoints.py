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

#-------------------pods--------------------------------------------
    def getPods(self):
        response = self.get('pods')
        return Pods.newFromDict(response)
    
    def postPods(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        
        response = self.post('pods',params)
        return response
    
    def addPods(self,ob):
        if not isinstance(ob,Pods):
            raise PyK8SError('Type Pods required')
        
        response = self.postPods(ob.toDict())
        return response

#-------------------pod--------------------------------------------
    def getPod(self,name):
        response = self.get('pods/'+name)
        return Pod.newFromDict(response)
    
    def postPod(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        
        response = self.post('pods/'+name,params)
        return response
    
    def addPod(self,name,ob):
        if not isinstance(ob,Pod):
            raise PyK8SError('Type Pod required')
        
        response = self.postPods(name,ob.toDict())
        return response

#-------------------nodes--------------------------------------------    
    def getNodes(self):
        response = self.get('nodes')
        return Nodes.newFromDict(response)
    
    def postNodes(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        
        response = self.post('nodes',params)
        return response
    
    def addNodes(self,ob):
        if not isinstance(ob,Nodes):
            raise PyK8SError('Type Nodes required')
        
        response = self.postNodes(ob.toDict())
        return response
    
#-------------------node--------------------------------------------    
    def getNode(self,name):
        response = self.get('nodes/'+name)
        return Node.newFromDict(response)
    
    def postNode(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        
        response = self.post('nodes/'+name,params)
        return response
    
    def addNode(self,name,ob):
        if not isinstance(ob,Nodes):
            raise PyK8SError('Type Node required')
        
        response = self.postNode(name,ob.toDict())
        return response
        
    
#-------------------services--------------------------------------------    
    def getServices(self):
        response = self.get('services')
        return Services.newFromDict(response)

    def postServices(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        
        response = self.post('services',params)
        return response
    
    def addServices(self,ob):
        if not isinstance(ob,Services):
            raise PyK8SError('Type Services required')
        
        response = self.postServices(ob.toDict())
        return response

#-------------------service--------------------------------------------    
    def getService(self,name):
        response = self.get('services/'+name)
        return Service.newFromDict(response)
    
    def postService(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        
        response = self.post('services/'+name,params)
        return response
    
    def addService(self,name,ob):
        if not isinstance(ob,Service):
            raise PyK8SError('Type Service required')
        
        response = self.postService(name,ob.toDict())
        return response
#     def getBindings(self):
#         response = self.get('services')
#         return Services.newFromDict(response)
#-------------------events--------------------------------------------
    def getEvents(self):
        response=self.get('events')
        return Events.newFromDict(response)
    
    def postEvents(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        
        response = self.post('events',params)
        return response
    
    def addEvents(self,ob):
        if not isinstance(ob,Events):
            raise PyK8SError('Type Events required')
        
        response = self.postEvents(ob.toDict())
        return response
#-------------------event--------------------------------------------    
    def getEvent(self,name):
        response=self.get('events'+name)
        return Event.newFromDict(response)
    
    def postEvent(self,name,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        
        response = self.post('events/'+name,params)
        return response
    
    def addEvent(self,name,ob):
        if not isinstance(ob,Event):
            raise PyK8SError('Type Event required')
        
        response = self.postEvent(name,ob.toDict())
        return response
#-------------------limitranges--------------------------------------------    
    def getLimitranges(self):
        response=self.get('limitranges')
        return Limitranges.newFromDict(response)
    
    def postLimitranges(self,params):
        if not isinstance(params,dict):
            raise PyK8SError('Type dict required')
        
        response = self.post('limitranges',params)
        return response
    
    def addLimitranges(self,ob):
        if not isinstance(ob,Limitranges):
            raise PyK8SError('Type Limitranges required')
        
        response = self.postLimitranges(ob.toDict())
        return response
#-------------------limitrange--------------------------------------------    
    def getLimitrange(self,name):
        response=self.get('limitranges'+name)
        return Limitrange.newFromDict(response)
    
#-------------------replicationcontrollers--------------------------------------------
    def getReplicationcontrollers(self):
        response=self.get('replicationcontrollers')
        return Replicationcontrollers.newFromDict(response)
    
#-------------------replicationcontroller--------------------------------------------    
    def getReplicationcontroller(self,name):
        response=self.get('replicationcontrollers'+name)
        return Replicationcontroller.newFromDict(response)
    
#-------------------resourcequotas--------------------------------------------    
    def getResourcequotas(self):
        response=self.get('resourcequotas')
        return Resourcequotas.newFromDict(response)
   
#-------------------resourcequota--------------------------------------------    
    def getResourcequota(self,name):
        response=self.get('resourcequotas'+name)
        return Resourcequota.newFromDict(response)    
    
