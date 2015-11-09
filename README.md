Power
=====

Linux python module to access power capabilities of the system.

- Power source type: AC, Battery or UPS
- Battery warning level: no warning (None), less than 22% of battery (Early), less than 10min (Final) 
- AC system status report: status code, time remaining to full/empty whether system is charging or discharging, battery capacity.
- Fault tolerant: if for some reason power capabilities cannot be extracted, falls back to AC
- Support for multiple battries ( stats reported capacity is average of batteries in system with more than one battery)
- Very easy to extend to support new features or new systems
