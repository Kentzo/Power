# coding=utf-8
"""
    Imports Power Management functions of Windows Vista and higher into Python.
    Refer to http://msdn.microsoft.com/en-us/library/windows/desktop/aa373163(v=vs.85).aspx
    for the most recent documentation.
"""
__author__ = 'kulakov.ilya@gmail.com'

from ctypes import Structure, wintypes, POINTER, windll, GetLastError, WinError

class SYSTEM_BATTERY_STATE(Structure):
    _fields_ = [
        ("AcOnLine", wintypes.BOOLEAN),
        ("BatteryPresent", wintypes.BOOLEAN),
        ("Charging", wintypes.BOOLEAN),
        ("Discharging", wintypes.BOOLEAN),
        ("Spare1", wintypes.BOOLEAN * 4),
        ("MaxCapacity", wintypes.DWORD),
        ("RemainingCapacity", wintypes.DWORD),
        ("Rate", wintypes.DWORD),
        ("EstimatedTime", wintypes.DWORD),
        ("DefaultAlert1", wintypes.DWORD),
        ("DefaultAlert2", wintypes.DWORD)
    ]

PSYSTEM_BATTERY_STATE = POINTER(SYSTEM_BATTERY_STATE)


class SYSTEM_POWER_STATUS(Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
        ('BatteryFullLifeTime', wintypes.DWORD),
        ]

LPSYSTEM_POWER_STATUS = POINTER(SYSTEM_POWER_STATUS)


SystemBatteryState = 5


GetSystemPowerStatus = windll.kernel32.GetSystemPowerStatus
GetSystemPowerStatus.argtypes = (LPSYSTEM_POWER_STATUS)
GetSystemPowerStatus.restype = wintypes.BOOL


CallNtPowerInformation = windll.powrprof.CallNtPowerInformation
CallNtPowerInformation.argtypes = (wintypes.c_int, wintypes.LPVOID, wintypes.ULONG, wintypes.LPVOID, wintypes.ULONG)
CallNtPowerInformation = wintypes.LONG
