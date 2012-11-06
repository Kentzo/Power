# coding=utf-8
"""
    This module import Power Sources functionality of IOKit into Python.
    Refer to /System/Library/Frameworks/IOKit.framework/Headers/ps/IOPowerSources.h
    and /System/Library/Frameworks/IOKit.framework/Headers/ps/IOPSKeys.h for the most recent documentation.

"""
__author__ = 'kulakov.ilya@gmail.com'

import objc as _objc
import os


def IOPSCopyExternalPowerAdapterDetails():
    pass


def IOPSCopyPowerSourcesInfo():
    pass


def IOPSCopyPowerSourcesList(blob):
    pass


def IOPSGetBatteryWarningLevel():
    pass


def IOPSGetPowerSourceDescription(blob, ps):
    pass


def IOPSGetProvidingPowerSourceType(snapshot):
    pass


def IOPSGetTimeRemainingEstimate():
    pass


def IOPSNotificationCreateRunLoopSource(callback, context):
    pass


kIOPSACPowerValue = None


kIOPSBatteryFailureModesKey = None


kIOPSBatteryHealthConditionKey = None


kIOPSBatteryHealthKey = None


kIOPSBatteryPowerValue = None


kIOPSCheckBatteryValue = None


kIOPSCommandDelayedRemovePowerKey = None


kIOPSCommandEnableAudibleAlarmKey = None


kIOPSCommandStartupDelayKey = None


kIOPSCurrentCapacityKey = None


kIOPSCurrentKey = None


kIOPSDeadWarnLevelKey = None


kIOPSDesignCapacityKey = None


kIOPSDynamicStorePath = None


kIOPSFailureCellImbalance = None


kIOPSFailureChargeFET = None


kIOPSFailureChargeOverCurrent = None


kIOPSFailureChargeOverTemp = None


kIOPSFailureDataFlushFault = None


kIOPSFailureDischargeFET = None


kIOPSFailureDischargeOverCurrent = None


kIOPSFailureDischargeOverTemp = None


kIOPSFailureExternalInput = None


kIOPSFailureFuseBlown = None


kIOPSFailureOpenThermistor = None


kIOPSFailurePeriodicAFEComms = None


kIOPSFailurePermanentAFEComms = None


kIOPSFailureSafetyOverVoltage = None


kIOPSFairValue = None


kIOPSGoodValue = None


kIOPSHardwareSerialNumberKey = None


kIOPSHealthConfidenceKey = None


kIOPSInternalBatteryType = None


kIOPSInternalType = None


kIOPSIsChargedKey = None


kIOPSIsChargingKey = None


kIOPSIsFinishingChargeKey = None


kIOPSIsPresentKey = None


kIOPSLowWarnLevelKey = None


kIOPSMaxCapacityKey = None


kIOPSMaxErrKey = None


kIOPSNameKey = None


kIOPSNetworkTransportType = None


kIOPSNotifyLowBattery = None


kIOPSOffLineValue = None


kIOPSPermanentFailureValue = None


kIOPSPoorValue = None


kIOPSPowerAdapterCurrentKey = None


kIOPSPowerAdapterFamilyKey = None


kIOPSPowerAdapterIDKey = None


kIOPSPowerAdapterRevisionKey = None


kIOPSPowerAdapterSerialNumberKey = None


kIOPSPowerAdapterSourceKey = None


kIOPSPowerAdapterWattsKey = None


kIOPSPowerSourceIDKey = None


kIOPSPowerSourceStateKey = None


kIOPSSerialTransportType = None


kIOPSTimeRemainingNotificationKey = None


kIOPSTimeToEmptyKey = None


kIOPSTimeToFullChargeKey = None


kIOPSTransportTypeKey = None


kIOPSTypeKey = None


kIOPSUPSManagementClaimed = None


kIOPSUPSType = None


kIOPSUSBTransportType = None


kIOPSVendorDataKey = None


kIOPSVoltageKey = None


kIOPSLowBatteryWarningEarly = None


kIOPSLowBatteryWarningFinal = None


kIOPSLowBatteryWarningNone = None


kIOPSTimeRemainingUnknown = None


kIOPSTimeRemainingUnlimited = None


bridgesupport_path = os.path.join(os.path.dirname(__file__), "IOPowerSources.bridgesupport")
bridgesupport = open(bridgesupport_path)
_objc.parseBridgeSupport(bridgesupport.read(),
    globals(),
    _objc.pathForFramework("/System/Library/Frameworks/IOKit.framework"))
