Power
=====

Crossplatform (Windows, Linux, Mac OS X, FreeBSD) python module to access power capabilities of the system.

- Power source type: AC, Battery or UPS
- Battery warning level: no warning (None), less than 22% of battery (Early), less than 10min (Final) 
- Time remaining estimate
- Fault tolerant: if for some reason power capabilities cannot be extracted, falls back to AC
- Support for multiple battries
- Power changes can be observed (Mac OS X only for now)
- Very easy to extand to support new features or new systems
