#!/usr/bin/env python
# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

from setuptools import setup
from sys import platform


REQUIREMENTS = []


if platform.startswith('darwin'):
    REQUIREMENTS.append('pyobjc >= 2.5')


setup(
    name="power",
    version="1.2",
    description="Cross-platform system power status information.",
    long_description="Library that allows you get current power source type (AC, Battery or UPS), warning level (none, <22%, <10min) and remaining minutes. You can also observe changes of power source and remaining time.",
    author="Ilya Kulakov",
    author_email="kulakov.ilya@gmail.com",
    url="https://github.com/Kentzo/Power",
    platforms=["Mac OS X 10.6+", "Windows XP+", "Linux 2.6+", "FreeBSD"],
    packages=['power'],
    license="MIT License",
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Power (UPS)',
    ],
    install_requires=REQUIREMENTS
)
