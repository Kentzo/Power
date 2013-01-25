#!/usr/bin/env python
# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

from setuptools import setup
from sys import platform


REQUIREMENTS = []


if platform.startswith('darwin'):
    REQUIREMENTS.append('pyobjc >= 2.5')


setup(
    name="Power",
    version="1.1",
    description="Cross-platform system power status information.",
    author="Ilya Kulakov",
    author_email="kulakov.ilya@gmail.com",
    url="https://github.com/Kentzo/Power",
    platforms=["Mac OS X 10.6+", "Windows XP+", "Linux 2.6+"],
    packages=['power'],
    classifiers=[
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Power (UPS)',
        'Topic :: System :: Hardware',
        'Topic :: System :: Monitoring'
    ],
    install_requires=REQUIREMENTS
)
