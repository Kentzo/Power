# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'


LOW_BATTERY_WARNING_NONE = 1

LOW_BATTERY_WARNING_EARLY = 2

LOW_BATTERY_WARNING_FINAL = 3


TIME_REMAINING_UNKNOWN = -1

TIME_REMAINING_UNLIMITED = -2


POWER_TYPE_AC = 0

POWER_TYPE_BATTERY = 1

POWER_TYPE_UPS = 2


def get_providing_power_source_type():
    pass

def get_low_battery_warning_level():
    pass

def get_time_remaining_estimate():
    pass


from sys import platform

if platform.startswith('darwin'):
    import darwin
    get_providing_power_source_type = darwin.power.get_providing_power_source_type
    get_low_battery_warning_level = darwin.power.get_low_battery_warning_level
    get_time_remaining_estimate = darwin.power.get_time_remaining_estimate
elif platform.startswith('win32'):
    import win32
    get_providing_power_source_type = win32.power.get_providing_power_source_type
    get_low_battery_warning_level = win32.power.get_low_battery_warning_level
    get_time_remaining_estimate = darwin.power.get_time_remaining_estimate
else:
    raise NotImplementedError("%s is not supported. If you believe it should be supported, check the %s".format(platform, __file__))
