# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:28:57 2020

@author: ggund
"""


from setuptools import setup

setup(
    # Needed to silence warnings
    name='Superalias_package',
    url='https://github.com/ggund99/Superalias_package1',
    author='ggund99',
    author_email='gaurav.gund@gartner.com',
    # Needed to actually package something
    packages=['superalias_package'],
    # Needed for dependencies
    #install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    license='MIT',
    description='Functions to do task in SuperAlias Tool',
    # We will also need a readme eventually (there will be a warning)
    #long_description=open('README.rst').read(),
    # if there are any scripts
   # scripts=['scripts/hello.py'],
)
