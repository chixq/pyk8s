from setuptools import  setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()
setup(
    name='PyK8S',
    version='1.0',
    description='Python API Wrapper of Google Kubernetes',
    long_description=long_description,
    url='https://github.com/chixq/pyk8s',
    keywords='kubernetes k8s api',
    license='MIT',
    packages='pyk8s',
    install_requires=['request', 'response'],
)
