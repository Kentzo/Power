Power
=====
.. image:: https://travis-ci.org/Kentzo/Power.svg?branch=master
    :target: https://travis-ci.org/Kentzo/Power
.. image:: https://codecov.io/gh/Kentzo/Power/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/Kentzo/Power
.. image:: https://img.shields.io/pypi/v/Power.svg
    :target: https://pypi.python.org/pypi/Power
.. image:: https://pyup.io/repos/github/Kentzo/Power/shield.svg
     :target: https://pyup.io/repos/github/Kentzo/Power/
     :alt: Updates

Crossplatform (Windows, Linux, Mac OS X, FreeBSD) python module to access power capabilities of the system.

- Power source type: AC, Battery or UPS
- Battery warning level: no warning (None), less than 22% of battery (Early), less than 10min (Final) 
- Time remaining estimate
- Fault tolerant: if for some reason power capabilities cannot be extracted, falls back to AC
- Support for multiple battries
- Power changes can be observed (Mac OS X only for now)
- Very easy to extand to support new features or new systems



Examples
--------

Until we expand the documentation please have a look in power/tests.py


