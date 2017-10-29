#!/usr/bin/env python
# coding=utf-8
import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


REQUIREMENTS = []

if sys.platform.startswith('darwin'):
    REQUIREMENTS.append('pyobjc-core >= 2.5')


TEST_REQUIREMENTS = [
    'pytest',
    'pytest-cov',
]


with open(os.path.join(os.path.dirname(__file__), 'power', 'version.py')) as f:
    VERSION = None
    code = compile(f.read(), 'version.py', 'exec')
    exec(code)
    assert VERSION


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name="power",
    version=VERSION,
    description="Cross-platform system power status information.",
    long_description="Library that allows you get current power source type (AC, Battery or UPS), "
                     "warning level (none, <22%, <10min) and remaining minutes. "
                     "You can also observe changes of power source and remaining time.",
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Power (UPS)',
    ],
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    extras_require={
        'tests': TEST_REQUIREMENTS
    },
    cmdclass={'test': PyTest}
)
