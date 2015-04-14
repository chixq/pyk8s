#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyk8s.exceptions import PyK8SError
from pyk8s.pods import Pods
from pyk8s.nodes import Nodes
from pyk8s.services import Services
from pyk8s.events import Events
from pyk8s.limitRanges import LimitRanges
from pyk8s.replicationControllers import ReplicationControllers
from pyk8s.resourceQuotas import ResourceQuotas
from pyk8s.pod import Pod
from pyk8s.node import Node
from pyk8s.service import Service
from pyk8s.event import Event
from pyk8s.limitRange import LimitRange
from pyk8s.replicationController import ReplicationController
from pyk8s.resourceQuota import ResourceQuota
from pyk8s.bindings import Bindings

class EndpointMixin(object):
