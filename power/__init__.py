# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

from common import *
from sys import platform


if platform.startswith('darwin'):
    from darwin import PowerManagement
elif platform.startswith('win32'):
    from win32 import PowerManagement
elif platform.startswith('linux'):
    from linux import PowerManagement
else:
    from common import PowerManagementBase
    import warnings
    class PowerManagement(PowerManagementBase):
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

    warnings.warn("{platform} is not supported. No-op PowerManagement class is used.".format(platform=platform))
