#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-bostonschema',
    version='0.1',
    description='',
    license='AGPL3',
    author='',
    author_email='',
    url='',
    namespace_packages=['ckanext'],
    packages=['ckanext.bostonschema'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        boston_schema = ckanext.bostonschema.plugins:BostonSchema
    """
)
