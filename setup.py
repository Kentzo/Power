#!/usr/bin/env python
# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name="Power",
    version="1.0",
    description="Cross-platform system power status information.",
    author="Ilya Kulakov",
    author_email="kulakov.ilya@gmail.com",
    url="https://github.com/Kentzo/Power",
    platforms=["Mac OS X 10.6+", "Windows XP+", "Linux 2.6+"],
    packages=['power'],
    classifiers=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: System :: Power (UPS)',
        'Topic :: System :: Hardware',
        'Topic :: System :: Monitoring'
    ]
)
