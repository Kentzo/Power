# coding=utf-8
"""
    Imports Power Management functions of Windows Vista and higher into Python.
    Refer to http://msdn.microsoft.com/en-us/library/windows/desktop/aa373163(v=vs.85).aspx
    for the most recent documentation.
"""
__author__ = 'kulakov.ilya@gmail.com'

from ctypes import Structure, wintypes, POINTER, windll, GetLastError, WinError, pointer, WINFUNCTYPE
import base
import weakref


# GetSystemPowerStatus
# Returns brief description of current system power status.
# Windows XP+
# REQUIRED.
GetSystemPowerStatus = None
try:
    GetSystemPowerStatus = windll.kernel32.GetSystemPowerStatus

    class SYSTEM_POWER_STATUS(Structure):
        _fields_ = [
            ('ACLineStatus', wintypes.c_ubyte),
            ('BatteryFlag', wintypes.c_ubyte),
            ('BatteryLifePercent', wintypes.c_ubyte),
            ('Reserved1', wintypes.c_ubyte),
            ('BatteryLifeTime', wintypes.DWORD),
            ('BatteryFullLifeTime', wintypes.DWORD)
            ]

    GetSystemPowerStatus.argtypes = [POINTER(SYSTEM_POWER_STATUS)]
    GetSystemPowerStatus.restype = wintypes.BOOL
except AttributeError as e:
    raise RuntimeError("Unable to load GetSystemPowerStatus."
                       "The system does not provide it (Win XP is required) or kernel32.dll is damaged.")


# PowerSettingRegisterNotification/PowerSettingUnregisterNotification
# Allows to register callback for power setting notitifacations
# Windows 7+
# NOT REQUIRED
PowerSettingRegisterNotification = None
PowerSettingUnregisterNotification = None
DEVICE_NOTIFY_CALLBACK_ROUTINE = None
GUID_ACDC_POWER_SOURCE = None
GUID_BATTERY_PERCENTAGE_REMAINING = None
try:
    PowerSettingRegisterNotification = windll.powrprof.PowerSettingRegisterNotification
    PowerSettingUnregisterNotification = windll.powrprof.PowerSettingUnregisterNotification

    # See pyglet.com (http://code.google.com/p/pyglet/source/browse/pyglet/com.py)
    class GUID(Structure):
        _fields_ = [
            ('Data1', wintypes.c_long),
            ('Data2', wintypes.c_short),
            ('Data3', wintypes.c_short),
            ('Data4', wintypes.c_byte * 8)
        ]

        def __init__(self, l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
            self.Data1 = l
            self.Data2 = w1
            self.Data3 = w2
            self.Data4[:] = (b1, b2, b3, b4, b5, b6, b7, b8)

    PowerSettingRegisterNotification.argtypes = [POINTER(GUID), wintypes.DWORD, wintypes.HANDLE, POINTER(wintypes.LPVOID)]
    PowerSettingRegisterNotification.restype = wintypes.DWORD
    PowerSettingUnregisterNotification.argtypes = [POINTER(wintypes.LPVOID)]
    PowerSettingUnregisterNotification.restype = wintypes.DWORD

    DEVICE_NOTIFY_CALLBACK_ROUTINE = WINFUNCTYPE(wintypes.ULONG, wintypes.LPVOID, wintypes.ULONG, wintypes.LPVOID)
    # GUID values are found in WinNT.h of Window 7 SDK
    GUID_ACDC_POWER_SOURCE = GUID(0x5D3E9A59, 0xE9D5, 0x4B00, 0xA6, 0xBD, 0xFF, 0x34, 0xFF, 0x51, 0x65, 0x48)
    GUID_BATTERY_PERCENTAGE_REMAINING = GUID(0xA7AD8041, 0xB45A, 0x4CAE, 0x87, 0xA3, 0xEE, 0xCB, 0xB4, 0x68, 0xA9, 0xE1)
except AttributeError as e:
    PowerSettingRegisterNotification = None
    PowerSettingUnregisterNotification = None
    DEVICE_NOTIFY_CALLBACK_ROUTINE = None
    GUID_ACDC_POWER_SOURCE = None
    GUID_BATTERY_PERCENTAGE_REMAINING = None
    raise RuntimeWarning("Unable to load PowerSettingRegisterNotification/PowerSettingUnregisterNotification."
                         "The system does not provide them (Win 7 is required) or powrprof.dll is damaged."
                         "You will add_observer/remove_observer are noop.")


POWER_TYPE_MAP = {
    0: base.POWER_TYPE_BATTERY,
    1: base.POWER_TYPE_AC,
    255: base.POWER_TYPE_AC
}


class PowerManagement(base.PowerManagementBase):
    def __init__(self):
        super(PowerManagement, self).__init__()

        weak_self = weakref.ref(self)

        def on_acdc_power_source_change(context, type, setting):
            weak_self()
            pass

        def on_battery_percentage_remaining_change(context, type, setting):
            weak_self()
            pass

        self.on_acdc_power_source_change = DEVICE_NOTIFY_CALLBACK_ROUTINE(on_acdc_power_source_change)
        self.on_battery_percentage_remaining_change = DEVICE_NOTIFY_CALLBACK_ROUTINE(on_battery_percentage_remaining_change)

    def get_providing_power_source_type(self):
        power_status = SYSTEM_POWER_STATUS()
        if not GetSystemPowerStatus(pointer(power_status)):
            raise WinError()
        return POWER_TYPE_MAP[power_status.ACLineStatus]

    def get_low_battery_warning_level(self):
        power_status = SYSTEM_POWER_STATUS()
        if not GetSystemPowerStatus(pointer(power_status)):
            raise WinError()

        if POWER_TYPE_MAP[power_status.ACLineStatus] == base.POWER_TYPE_AC:
            return base.LOW_BATTERY_WARNING_NONE
        else:
            if power_status.BatteryLifeTime != -1 and power_status.BatteryLifeTime <= 600:
                return base.LOW_BATTERY_WARNING_FINAL
            elif power_status.BatteryLifePercent <= 22:
                return base.LOW_BATTERY_WARNING_EARLY
            else:
                return base.LOW_BATTERY_WARNING_NONE

    def get_time_remaining_estimate(self):
        power_status = SYSTEM_POWER_STATUS()
        if not GetSystemPowerStatus(pointer(power_status)):
            raise WinError()

        if POWER_TYPE_MAP[power_status.ACLineStatus] == base.POWER_TYPE_AC:
            return base.TIME_REMAINING_UNLIMITED
        elif power_status.BatteryLifeTime == -1:
            return base.TIME_REMAINING_UNKNOWN
        else:
            return float(power_status.BatteryLifeTime) / 60

    def get_external_power_adapter_info(self):
        pass

    def get_power_sources_info(self):
        pass

    def add_observer(self, observer):
        if not PowerSettingRegisterNotification:
            return
        super(PowerManagement, self).add_observer(observer)
        if len(self._weak_observers) == 1:
            PowerSettingRegisterNotification(pointer(), )

    def remove_observer(self, observer):
        if not PowerSettingUnregisterNotification:
            return
        if len(self._weak_observers) == 0:
            PowerSettingUnregisterNotification()
