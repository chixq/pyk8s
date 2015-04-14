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
        self.pyk8s = PyK8S(base_url="http://54.159.167.112:8888/api", user_id="", user_password="", client_args=client_args)

    @unittest.skipIf(skipTest, '')
    def testGetPods(self):
        pod_list = self.pyk8s.getPods()
        self.assertGreater(len(pod_list.toDict()), 1)
        
#     @unittest.skipIf(skipTest, '')
#     def testGetPod(self):
#         pod = self.pyk8s.getPod('nginxcontroller-pw5ua')
#         print pod.toDict()
#         self.assertGreater(len(pod.toDict()), 1)
        
    @unittest.skipIf(skipTest, '')   
    def testaddPodFromFile(self):
        self.pyk8s.addPodFromFile("/home/renhuiyang/2015/pyk8s/test/pod.json")
        
    @unittest.skipIf(skipTest, '')
    def testGetNodes(self):
        node_list = self.pyk8s.getNodes()
        self.assertGreater(len(node_list.toDict()), 1)
        
    @unittest.skipIf(skipTest, '')   
    def testGetNode(self):
        node = self.pyk8s.getNode('ip-10-35-177-40.ec2.internal')
        self.assertGreater(len(node.toDict()), 1)
        
    @unittest.skipIf(skipTest, '')
    def testGetServices(self):
        Services_list = self.pyk8s.getServices()
        self.assertGreater(len(Services_list.toDict()), 1)
        
    @unittest.skipIf(skipTest, '')
    def testGetService(self):
        Service = self.pyk8s.getService('k8sm-scheduler')
        self.assertGreater(len(Service.toDict()), 1)
        
    @unittest.skipIf(skipTest, '')   
    def testaddReplicationcontrollerFromFile(self):
        self.pyk8s.addReplicationControllerFromFile("/home/renhuiyang/2015/pyk8s/test/controll.json")
        
#     @unittest.skipIf(skipTest, '')   
#     def testaddServiceFromFile(self):
#         self.pyk8s.addServiceFromFile("/home/renhuiyang/2015/pyk8s/test/service.json")
        
if __name__ == '__main__':
   unittest.main()