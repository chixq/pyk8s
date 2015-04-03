#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyk8s.pod import PodList


class EndpointMixin(object):

    def getPods(self):
        response = self.get('pods')
        return PodList.newFromDict(response)

