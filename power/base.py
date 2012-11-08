# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

from abc import ABCMeta, abstractmethod
import weakref


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

    @abstractmethod
    def get_providing_power_source_type(self):
        pass

    @abstractmethod
    def get_low_battery_warning_level(self):
        pass

    @abstractmethod
    def get_time_remaining_estimate(self):
        pass

    @abstractmethod
    def get_external_power_adapter_info(self):
        pass

    @abstractmethod
    def get_power_sources_info(self):
        pass

    @abstractmethod
    def add_observer(self, observer):
        """
        Adds an observer. If observer already registered, subsequent calls are NOT counted.

        You're responsible for removing observer. Otherwise observer may continue receive notifications
        even if PowerManagement object used to register observer is deallocated.
        """
        if not isinstance(observer, PowerManagementObserver):
            raise TypeError("observer MUST conform to power.PowerManagementObserver")
        self._weak_observers.add(weakref.ref(observer))

    @abstractmethod
    def remove_observer(self, observer):
        """
        Removes observer if it was registered. Subsequent calls for already removed observers are ignored.
        """
        self._weak_observers.remove(weakref.ref(observer))

    def remove_all_observers(self):
        """
        Remove all registered observers.
        """
        for weak_observer in self._weak_observers:
            observer = weak_observer()
            if observer:
                self.remove_observer(observer)
        self._weak_observers = set()


class PowerManagementObserver:
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_power_sources_change(self, power_management):
        pass
