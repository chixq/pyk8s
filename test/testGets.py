#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from pyk8s.api import PyK8S

skipTest=False

class GetsTest(unittest.TestCase):
    def setUp(self):
        print 'Test GET Method...'
        client_args = {
            'headers': {
                'User-Agent': 'PyK8S Test'
            },
            'allow_redirects': False
        }
        self.pyk8s = PyK8S(base_url="http://54.249.185.104:8888/api", user_id="", user_password="", client_args=client_args)

    @unittest.skipIf(skipTest, '')
    def testGetPods(self):
        pod_list = self.pyk8s.getPods()
        self.assertGreater(len(pod_list), 1)
