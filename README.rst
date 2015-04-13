PyK8S
=====

PyK8S is the API wrapper of Google Kubernetes.

Release Note
------------
v1.0 support Kubernetes 0.14

Installation
------------

```
pip install pyk8s
```

Basic Usages
------------

```
pyk8s = PyK8S(base_url="http://54.249.185.104:8888/api", user_id="", user_password="", client_args=client_args)
pod_list = pyk8s.getPods()
```

