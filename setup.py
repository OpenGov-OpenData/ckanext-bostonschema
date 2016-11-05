#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-bostontheme',
    version='0.1',
    description='',
    license='AGPL3',
    author='',
    author_email='',
    url='',
    namespace_packages=['ckanext'],
    packages=['ckanext.bostontheme'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        boston_theme = ckanext.bostontheme.plugins:CustomTheme
    """
)
