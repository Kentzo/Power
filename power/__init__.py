# coding=utf-8
"""
Provides checking of current power source, battery warning level, ac status, battery 
time remaining estimate and battery capacity.
Allows you to add observer for power notifications if platform supports it.

Usage:
    from power import PowerManagement, PowerManagementObserver # Automatically imports platform-specific implementation

    class Observer(PowerManagementObserver):
        def on_power_sources_change(self, power_management):
            print("Power sources did change.")

        def on_time_remaining_change(self, power_management):
            print("Time remaining did change.")

    # class Observer(object):
    #     ...
    # PowerManagementObserver.register(Observer)

Another example:
    import power

    p = power.PowerManagement()

    ac_status, time_remaining, bat_capacity = p.get_ac_status()

    print('AC system status      :', ac_status)
    print('Time remaining        :', time_remaining, 'minutes')
    print('Capacity of batteries :', bat_capacity, '\n%')

"""
__version__ = '1.5'

from sys import platform
from power.common import *


try:
    from power.linux import PowerManagement
except RuntimeError as e:
    import warnings
    warnings.warn("Unable to load PowerManagement for {platform}. No-op PowerManagement class is used: {error}".format(error=str(e), platform=platform))
    from power.common import PowerManagementNoop as PowerManagement
