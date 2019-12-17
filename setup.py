#!/usr/bin/env python

from setuptools import setup

setup(name='fmlib',
      version='0.1.0',
      description='Fleet Management Library',
      author='Argentina Ortega Sáinz',
      packages=['fmlib', 'fmlib.api', 'fmlib.api.rest', 'fmlib.config',
                'fmlib.db', 'fmlib.exceptions', 'fmlib.interface', 'fmlib.models',
                'fmlib.monitoring', 'fmlib.planning', 'fmlib.requests', 'fmlib.tests',
                'fmlib.tests.fmlib', 'fmlib.integration', 'fmlib.utils'],
      package_dir={'': '.'}
      )
