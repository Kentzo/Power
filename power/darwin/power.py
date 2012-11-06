# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

from . import IOPowerSources
from .. import LOW_BATTERY_WARNING_NONE, LOW_BATTERY_WARNING_EARLY, LOW_BATTERY_WARNING_FINAL
from .. import POWER_TYPE_AC, POWER_TYPE_BATTERY, POWER_TYPE_UPS


POWER_TYPE_MAP = {
    IOPowerSources.kIOPMACPowerKey : POWER_TYPE_AC,
    IOPowerSources.kIOPMBatteryPowerKey : POWER_TYPE_BATTERY,
    IOPowerSources.kIOPMUPSPowerKey : POWER_TYPE_UPS
}

def get_providing_power_type():
    providing_source = IOPowerSources.IOPSCopyPowerSourcesInfo()
    power_type = IOPowerSources.IOPSGetProvidingPowerSourceType(providing_source)
    return POWER_TYPE_MAP[power_type]


WARNING_LEVEL_MAP = {
    IOPowerSources.kIOPSLowBatteryWarningNone : LOW_BATTERY_WARNING_NONE,
    IOPowerSources.kIOPSLowBatteryWarningEarly : LOW_BATTERY_WARNING_EARLY,
    IOPowerSources.kIOPSLowBatteryWarningFinal : LOW_BATTERY_WARNING_FINAL
}

def get_low_battery_warning_level():
    warning_level = IOPowerSources.IOPSGetBatteryWarningLevel()
    return WARNING_LEVEL_MAP[warning_level]


def get_time_remaining_estimate():
    return int(IOPowerSources.IOPSGetTimeRemainingEstimate())
