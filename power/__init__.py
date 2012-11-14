# coding=utf-8
"""
Provides crossplatform checking of current power source, battery warning level and battery time remaining estimate.
Allows you to add observer for power notifications if platform supports it.

Usage:
    from power import PowerManagement, PowerManagementObserver # Automatically imports platform-specific implementation

    class Observer(PowerManagementObserver):
        def on_power_sources_change(self, power_management):
            print "Power sources did change."

        def on_time_remaining_change(self, power_management):
            print "Time remaining did change."

    # class Observer(object):
    #     ...
    # PowerManagementObserver.register(Observer)
"""
__author__ = 'kulakov.ilya@gmail.com'

from common import *
from sys import platform
import warnings
import common


class PowerManagementNoop(common.PowerManagementBase):
    """
    No-op subclass of PowerManagement.
    It operates like AC is always attached and power sources are never changed.
    """
    def get_providing_power_source_type(self):
        """
        @return: Always POWER_TYPE_AC
        """
        return POWER_TYPE_AC

    def get_low_battery_warning_level(self):
        """
        @return: Always LOW_BATTERY_WARNING_NONE
        """
        return LOW_BATTERY_WARNING_NONE

    def get_time_remaining_estimate(self):
        """
        @return: Always TIME_REMAINING_UNLIMITED
        """
        return TIME_REMAINING_UNLIMITED

    def add_observer(self, observer):
        """
        Does nothing.
        """
        pass

    def remove_observer(self, observer):
        """
        Does nothing.
        """
        pass

    def remove_all_observers(self):
        """
        Does nothing.
        """
        pass


try:
    if platform.startswith('darwin'):
        from darwin import PowerManagement
    elif platform.startswith('win32'):
        from win32 import PowerManagement
    elif platform.startswith('linux'):
        from linux import PowerManagement
    else:
        raise RuntimeError("{platform} is not supported.".format(platform=platform))
except RuntimeError as e:
    warnings.warn("Unable to load PowerManagement for {platform}. No-op PowerManagement class is used: {error}".format(error=str(e), platform=platform))
    from . import PowerManagementNoop as PowerManagement
