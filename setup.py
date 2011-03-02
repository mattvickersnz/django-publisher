#!/usr/bin/env python

# ...

from distutils.core import setup

setup(name='Django Publisher',
      version='0.1',
      description='Django Publisher: Adds publication status and date to any model.',
      author='mattgeeknz',
      author_email='code@matt.geek.nz',
      maintainer='mattgeeknz',
      maintainer_email='code@matt.geek.nz',
      url='https://github.com/mattgeeknz/django-publisher/',
      packages=['publisher'],
      long_description="Simple encapsulation of publication state that can be applied to any Django model.",
      license="MIT License",
      platforms=["any"],
     )
