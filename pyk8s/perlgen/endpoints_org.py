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
