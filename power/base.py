# coding=utf-8
from abc import ABCMeta, abstractmethod, abstractproperty
import weakref

__author__ = 'kulakov.ilya@gmail.com'


LOW_BATTERY_WARNING_NONE = 1

LOW_BATTERY_WARNING_EARLY = 2

LOW_BATTERY_WARNING_FINAL = 3


TIME_REMAINING_UNKNOWN = -1

TIME_REMAINING_UNLIMITED = -2


POWER_TYPE_AC = 0

POWER_TYPE_BATTERY = 1

POWER_TYPE_UPS = 2


#POWER_SOURCE_BATTERY_FAILURE_MODES_KEY = "Battery Failure Modes"
#
#POWER_SOURCE_BATTERY_HEALTH_CONDITION_KEY = "Battery Health Condition"
#
#kIOPSBatteryHealthKey = "Battery Health"
#
#kIOPSCurrentCapacityKey = "Current Capacity"
#
#kIOPSCurrentKey = "Current"
#
#kIOPSDesignCapacityKey = "Design Capacity"
#
#kIOPSHardwareSerialNumberKey = "Hardware Serial Number"
#
#kIOPSHealthConfidenceKey = "HealthConfidence"
#
#kIOPSIsChargedKey "Is Charged"
#
#kIOPSIsChargingKey "Is Charging"
#
#kIOPSIsFinishingChargeKey "Is Finishing Charge"
#
#kIOPSIsPresentKey "Is Present"
#
#kIOPSLowWarnLevelKey "Low Warn Level"
#
#kIOPSMaxCapacityKey "Max Capacity"
#
#kIOPSMaxErrKey "MaxErr"
#
#kIOPSNameKey "Name"
#
#kIOPSPowerAdapterFamilyKey "FamilyCode"
#
#kIOPSPowerAdapterIDKey "AdapterID"
#
#kIOPSPowerAdapterRevisionKey "AdapterRevision"
#
#kIOPSPowerAdapterSerialNumberKey "SerialNumber"
#
#kIOPSPowerAdapterSourceKey "Source"
#
#kIOPSPowerAdapterWattsKey "Watts"
#
#kIOPSPowerSourceIDKey "Power Source ID"
#
#kIOPSPowerSourceStateKey "Power Source State"
#
#kIOPSSerialTransportType "Serial"
#
#kIOPSTimeToEmptyKey "Time to Empty"
#
#kIOPSTimeToFullChargeKey "Time to Full Charge"
#
#kIOPSTransportTypeKey "Transport Type"
#
#kIOPSTypeKey "Type"
#
#kIOPSVendorDataKey "Vendor Specific Data"
#
#kIOPSVoltageKey "Voltage"


class PowerManagementBase(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._weak_observers = set()

    @abstractproperty
    def providing_power_source_type(self):
        pass

    @abstractproperty
    def low_battery_warning_level(self):
        pass

    @abstractproperty
    def time_remaining_estimate(self):
        pass

    @abstractmethod
    def get_external_power_adapter_info(self):
        pass

    @abstractmethod
    def get_power_sources_info(self):
        pass

    @abstractmethod
    def add_observer(self, observer):
        if not isinstance(observer, PowerManagementObserver):
            raise TypeError("observer MUST conform to power.PowerManagementObserver")
        self._weak_observers.add(weakref.ref(observer))

    @abstractmethod
    def remove_observer(self, observer):
        self._weak_observers.remove(weakref.ref(observer))


class PowerManagementObserver:
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_power_sources_change(self, power_management):
        pass
