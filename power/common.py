# coding=utf-8
"""
    Represents common objects and classes across all platforms.

    @group Power Source Type: POWER_TYPE_AC, POWER_TYPE_BATTERY, POWER_TYPE_UPS
    @var POWER_TYPE_AC: The system is connected to the external power source.
    @var POWER_TYPE_BATTERY: The system is connected to the battery.
    @var POWER_TYPE_UPS: The system is connected to UPS.
    @type POWER_TYPE_BATTERY: int
    @type POWER_TYPE_AC: int
    @type POWER_TYPE_UPS: int

    @group Low Battery Warning Levels: LOW_BATTERY_WARNING_NONE, LOW_BATTERY_WARNING_EARLY, LOW_BATTERY_WARNING_FINAL
    @var LOW_BATTERY_WARNING_NONE: The system is connected to the unlimited power source.
    @var LOW_BATTERY_WARNING_EARLY: The battery has dropped below 22% remaining power.
    @var LOW_BATTERY_WARNING_FINAL: The battery can provide no more than 10 minutes of runtime.
    @type LOW_BATTERY_WARNING_EARLY: int
    @type LOW_BATTERY_WARNING_NONE: int
    @type LOW_BATTERY_WARNING_FINAL: int

    @group Special Values For Time Remaining: TIME_REMAINING_UNKNOWN, TIME_REMAINING_UNLIMITED
    @var TIME_REMAINING_UNKNOWN: Indicates the system is connected to a limited power source, but system is still
        calculating a time remaining estimate.
    @var TIME_REMAINING_UNLIMITED: Indicates that the system is connected to an external power source, without time limit.
    @type TIME_REMAINING_UNKNOWN: float
    @type TIME_REMAINING_UNLIMITED: float

    @group Power Adapter Info Dictionary Keys: POWER_ADAPTER_FAMILY_KEY,
        POWER_ADAPTER_ID_KEY,
        POWER_ADAPTER_REVISION_KEY,
        POWER_ADAPTER_SERIAL_NUMBER_KEY,
        POWER_ADAPTER_SOURCE_KEY,
        POWER_ADAPTER_WATTS_KEY,
        POWER_ADAPTER_CURRENT_KEY
    @var POWER_ADAPTER_FAMILY_KEY: Power adapter's family code.
        Value type is int.
    @var POWER_ADAPTER_ID_KEY: Power adapter's ID.
        Value type is int.
    @var POWER_ADAPTER_REVISION_KEY: Power adapter's revision.
        Value type is int.
    @var POWER_ADAPTER_SERIAL_NUMBER_KEY: Power adapter's serial number.
        Value type is int.
    @var POWER_ADAPTER_SOURCE_KEY: Power adapter's source.
        Value type is int.
    @var POWER_ADAPTER_WATTS_KEY: Wattage of the power adapter in units of watts.
        Value type is int.
    @var POWER_ADAPTER_CURRENT_KEY: Current of the power adapter in units of mAmps.
        Value type is int.
    @type POWER_ADAPTER_FAMILY_KEY: str
    @type POWER_ADAPTER_ID_KEY: str
    @type POWER_ADAPTER_REVISION_KEY: str
    @type POWER_ADAPTER_SERIAL_NUMBER_KEY: str
    @type POWER_ADAPTER_SOURCE_KEY: str
    @type POWER_ADAPTER_WATTS_KEY: str
    @type POWER_ADAPTER_CURRENT_KEY: str

    @group Power Source Info Dictionary Keys: POWER_SOURCE_BATTERY_FAILURE_MODES_KEY,
        POWER_SOURCE_BATTERY_HEALTH_CONDITION_KEY,
        POWER_SOURCE_BATTERY_HEALTH_KEY,
        POWER_SOURCE_CURRENT_CAPACITY_KEY,
        POWER_SOURCE_CURRENT_KEY,
        POWER_SOURCE_DESIGN_CAPACITY_KEY,
        POWER_SOURCE_HARDWARE_SERIAL_NUMBER_KEY,
        POWER_SOURCE_IS_CHARGED_KEY,
        POWER_SOURCE_IS_CHARGING_KEY,
        POWER_SOURCE_IS_FINISHING_CHARGE_KEY,
        POWER_SOURCE_IS_PRESENT_KEY,
        POWER_SOURCE_MAX_CAPACITY_KEY,
        POWER_SOURCE_MAX_ERR_KEY,
        POWER_SOURCE_NAME_KEY,
        POWER_SOURCE_TIME_TO_EMPTY_KEY,
        POWER_SOURCE_TIME_TO_FULL_CHARGEKEY,
        POWER_SOURCE_TRANSPORT_TYPE_KEY,
        POWER_SOURCE_VENDOR_DATA_KEY,
        POWER_SOURCE_VOLTAGE_KEY,
        POWER_SOURCE_VOLTAGE_KEY,
        POWER_SOURCE_ID_KEY,
        POWER_SOURCE_STATE_KEY
    @var POWER_SOURCE_BATTERY_FAILURE_MODES_KEY:  A battery may suffer from more than one type of failure simultaneously
        therefore value is list of strings defined in Battery Failure Modes.
    @var POWER_SOURCE_BATTERY_HEALTH_CONDITION_KEY: Broadly describes battery's health.
        Value is one of the Battery Health Condition Values.
    @var POWER_SOURCE_BATTERY_HEALTH_KEY: Battery's health estimate.
        Value is one of the Battery Health Values.
    @var POWER_SOURCE_CURRENT_CAPACITY_KEY: Power Source's capacity usually in units mAh.
        Units are consistent for all reported capcities.
        Value type is int.
    @var POWER_SOURCE_CURRENT_KEY: Power Source's electric current in units of mA.
        Value type is int.
    @var POWER_SOURCE_DESIGN_CAPACITY_KEY: Power Source's design capcity usually in units of mAh.
        Units are consistent for all reported capcities.
        Value type is int.
    @var POWER_SOURCE_HARDWARE_SERIAL_NUMBER_KEY: An unique serial number that identifies Power Source.
        Value type is str.
    @var POWER_SOURCE_IS_CHARGED_KEY:
        A battery must be plugged in to an external power source in order to be fully charged.
        Note that a battery may validly be plugged in, not charging, and <100% charge.
        E.g. A battery with capacity >= 95% and not charging, is defined as charged.
        Valye type is bool.
    @var POWER_SOURCE_IS_CHARGING_KEY: Power Source's current charging state.
        Value type is bool.
    @var POWER_SOURCE_IS_FINISHING_CHARGE_KEY: Indicate whether the Power Source is finishing off its charge.
        Value type is bool.
    @var POWER_SOURCE_IS_PRESENT_KEY: Presense of the Power Source.
        E.g. a portable with the capacity for two batteries but with only one present would show 2 power source dictionaries,
        but POWER_SOURCE_IS_PRESENT_KEY would have the value False in one of them.
        Value type is bool.
    @var POWER_SOURCE_MAX_CAPACITY_KEY: Power Source's maximum or "Full Charge' capcity.
        Units are consistent for all reported capcities.
        Value type is int.
    @var POWER_SOURCE_MAX_ERR_KEY: Power Source's precentage error in capacity reporting.
        Value type is int.
    @var POWER_SOURCE_NAME_KEY: Power Source's name.
        Value type is str.
    @var POWER_SOURCE_TIME_TO_EMPTY_KEY: Power Source's time remaining until empty in units of seconds.
        Value type is int.
        -1 means "still calculating".
    @var POWER_SOURCE_TIME_TO_FULL_CHARGEKEY: Power Source's time remaining until full charged in units of seconds.
        Value type is int.
        -1 means "still calculating".
    @var POWER_SOURCE_TRANSPORT_TYPE_KEY: Power Source's power source data transport type.
        Value is one of the Data Transport Types
    @var POWER_SOURCE_TYPE_KEY: Type of the Power Source.
        Value is one of the Power Source Types.
    @var POWER_SOURCE_VENDOR_DATA_KEY: Arbitrary vendor data
        Value is dict.
    @var POWER_SOURCE_VOLTAGE_KEY: Power Source's electrical voltage in units of mV.
        Value is int.
    @var POWER_SOURCE_ID_KEY: Value uniquely identifying a UPS attached to the system.
        Value type is int.
    @var POWER_SOURCE_STATE_KEY: Curren source of power.
        Value is one of the Power Source States
    @type POWER_SOURCE_BATTERY_FAILURE_MODES_KEY: str
    @type POWER_SOURCE_BATTERY_HEALTH_CONDITION_KEY: str
    @type POWER_SOURCE_BATTERY_HEALTH_KEY: str
    @type POWER_SOURCE_CURRENT_CAPACITY_KEY: str
    @type POWER_SOURCE_CURRENT_KEY: str
    @type POWER_SOURCE_DESIGN_CAPACITY_KEY: str
    @type POWER_SOURCE_HARDWARE_SERIAL_NUMBER_KEY: str
    @type POWER_SOURCE_IS_CHARGED_KEY: str
    @type POWER_SOURCE_IS_CHARGING_KEY: str
    @type POWER_SOURCE_IS_FINISHING_CHARGE_KEY: str
    @type POWER_SOURCE_IS_PRESENT_KEY: str
    @type POWER_SOURCE_MAX_CAPACITY_KEY: str
    @type POWER_SOURCE_MAX_ERR_KEY: str
    @type POWER_SOURCE_NAME_KEY: str
    @type POWER_SOURCE_TIME_TO_EMPTY_KEY: str
    @type POWER_SOURCE_TIME_TO_FULL_CHARGEKEY: str
    @type POWER_SOURCE_TRANSPORT_TYPE_KEY: str
    @type POWER_SOURCE_TYPE_KEY: str
    @type POWER_SOURCE_VENDOR_DATA_KEY: str
    @type POWER_SOURCE_VOLTAGE_KEY: str
    @type POWER_SOURCE_ID_KEY: str
    @type POWER_SOURCE_STATE_KEY: str

    @group Battery Failure Modes: POWER_SOURCE_BATTERY_FAILURE_MODE_CELL_IMBALANCE,
        POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_FET,
        POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_OVER_CURRENT,
        POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_OVER_TEMP,
        POWER_SOURCE_BATTERY_FAILURE_MODE_DATA_FLUSH_FAULT,
        POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_FET,
        POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_OVER_CURRENT
        POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_OVER_TEMP,
        POWER_SOURCE_BATTERY_FAILURE_MODE_EXTERNAL_INPUT,
        POWER_SOURCE_BATTERY_FAILURE_MODE_FUSE_BLOWN,
        POWER_SOURCE_BATTERY_FAILURE_MODE_OPEN_THERMISTOR,
        POWER_SOURCE_BATTERY_FAILURE_MODE_PERIODIC_AFE_COMMS,
        POWER_SOURCE_BATTERY_FAILURE_MODE_PERMANENT_AFE_COMMS,
        POWER_SOURCE_BATTERY_FAILURE_MODE_SAFETY_OVER_VOLTAGE
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_CELL_IMBALANCE: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_FET: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_OVER_CURRENT: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_OVER_TEMP: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_DATA_FLUSH_FAULT: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_FET: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_OVER_CURRENT: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_OVER_TEMP: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_EXTERNAL_INPUT: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_FUSE_BLOWN: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_OPEN_THERMISTOR: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_PERIODIC_AFE_COMMS: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_PERMANENT_AFE_COMMS: str
    @type POWER_SOURCE_BATTERY_FAILURE_MODE_SAFETY_OVER_VOLTAGE: str

    @group Battery Health Condition Values: POWER_SOURCE_BATTERY_HEALTH_VALUE_CHECK_BATTERY,
        POWER_SOURCE_BATTERY_HEALTH_VALUE_PERMANENT_FAILURE
    @var POWER_SOURCE_BATTERY_HEALTH_VALUE_CHECK_BATTERY: This value indicates that the battery should be checked out by a repair service.
    @var POWER_SOURCE_BATTERY_HEALTH_VALUE_PERMANENT_FAILURE: Indicates the battery needs replacement.
    @type POWER_SOURCE_BATTERY_HEALTH_VALUE_CHECK_BATTERY: str
    @type POWER_SOURCE_BATTERY_HEALTH_VALUE_PERMANENT_FAILURE: str

    @group Battery Health Values: POWER_SOURCE_BATTERY_HEALTH_VALUE_FAIR,
        POWER_SOURCE_BATTERY_HEALTH_VALUE_GOOD,
        POWER_SOURCE_BATTERY_HEALTH_VALUE_POOR
    @type POWER_SOURCE_BATTERY_HEALTH_VALUE_FAIR: str
    @type POWER_SOURCE_BATTERY_HEALTH_VALUE_GOOD: str
    @type POWER_SOURCE_BATTERY_HEALTH_VALUE_POOR: str

    @group Data Transport Types:
        POWER_SOURCE_DATA_TRANSPORT_TYPE_USB
        POWER_SOURCE_DATA_TRANSPORT_TYPE_NETWORK
        POWER_SOURCE_DATA_TRANSPORT_TYPE_SERIAL
        POWER_SOURCE_DATA_TRANSPORT_TYPE_INTERNAL
    @var POWER_SOURCE_DATA_TRANSPORT_TYPE_USB: Indicates the power source is an UPS attached over a USB connection.
    @var POWER_SOURCE_DATA_TRANSPORT_TYPE_NETWORK: Indicates the power source is a UPS attached over a network connection (and it may be managing several computers).
    @var POWER_SOURCE_DATA_TRANSPORT_TYPE_SERIAL: Indicates the power source is a UPS attached over a serial connection.
    @var POWER_SOURCE_DATA_TRANSPORT_TYPE_INTERNAL: Indicates the power source is an internal battery.
    @type POWER_SOURCE_DATA_TRANSPORT_TYPE_USB: str
    @type POWER_SOURCE_DATA_TRANSPORT_TYPE_NETWORK: str
    @type POWER_SOURCE_DATA_TRANSPORT_TYPE_SERIAL: str
    @type POWER_SOURCE_DATA_TRANSPORT_TYPE_INTERNAL: str

    @group Power Source Types: POWER_SOURCE_TYPE_UPS, POWER_SOURCE_TYPE_INTERNAL_BATTERY
    @var POWER_SOURCE_TYPE_UPS: Represents a battery residing inside a machine.
    @var POWER_SOURCE_TYPE_INTERNAL_BATTERY: Represents an external attached UPS.
    @type POWER_SOURCE_TYPE_UPS: str
    @type POWER_SOURCE_TYPE_INTERNAL_BATTERY: str

    @group Power Source States:
        POWER_SOURCE_STATE_AC
        POWER_SOURC_STATE_BATTERY
        POWER_SOURCE_STATE_OFFLINE
    @var POWER_SOURCE_STATE_AC: Power source is connected to external or AC power, and is not draining the internal battery.
    @var POWER_SOURC_STATE_BATTERY: Power source is currently using the internal battery.
    @var POWER_SOURCE_STATE_OFFLINE: Power source is off-line or no longer connected.
    @type POWER_SOURCE_STATE_AC: str
    @type POWER_SOURC_STATE_BATTERY: str
    @type POWER_SOURCE_STATE_OFFLINE: str

"""
__author__ = 'kulakov.ilya@gmail.com'

from abc import ABCMeta, abstractmethod
import weakref

__all__ = [
    'POWER_TYPE_AC',
    'POWER_TYPE_BATTERY',
    'POWER_TYPE_UPS',
    'LOW_BATTERY_WARNING_NONE',
    'LOW_BATTERY_WARNING_EARLY',
    'LOW_BATTERY_WARNING_FINAL',
    'TIME_REMAINING_UNKNOWN',
    'TIME_REMAINING_UNLIMITED',
    'POWER_ADAPTER_FAMILY_KEY',
    'POWER_ADAPTER_ID_KEY',
    'POWER_ADAPTER_REVISION_KEY',
    'POWER_ADAPTER_SERIAL_NUMBER_KEY',
    'POWER_ADAPTER_SOURCE_KEY',
    'POWER_ADAPTER_WATTS_KEY',
    'POWER_ADAPTER_CURRENT_KEY',
    'POWER_ADAPTER_EMPTY_DICT',
    'POWER_SOURCE_BATTERY_FAILURE_MODES_KEY',
    'POWER_SOURCE_BATTERY_HEALTH_CONDITION_KEY',
    'POWER_SOURCE_BATTERY_HEALTH_KEY',
    'POWER_SOURCE_CURRENT_CAPACITY_KEY',
    'POWER_SOURCE_CURRENT_KEY',
    'POWER_SOURCE_DESIGN_CAPACITY_KEY',
    'POWER_SOURCE_HARDWARE_SERIAL_NUMBER_KEY',
    'POWER_SOURCE_IS_CHARGED_KEY',
    'POWER_SOURCE_IS_CHARGING_KEY',
    'POWER_SOURCE_IS_FINISHING_CHARGE_KEY',
    'POWER_SOURCE_IS_PRESENT_KEY',
    'POWER_SOURCE_MAX_CAPACITY_KEY',
    'POWER_SOURCE_MAX_ERR_KEY',
    'POWER_SOURCE_NAME_KEY',
    'POWER_SOURCE_TIME_TO_EMPTY_KEY',
    'POWER_SOURCE_TIME_TO_FULL_CHARGEKEY',
    'POWER_SOURCE_TRANSPORT_TYPE_KEY',
    'POWER_SOURCE_TYPE_KEY',
    'POWER_SOURCE_VENDOR_DATA_KEY',
    'POWER_SOURCE_VOLTAGE_KEY',
    'POWER_SOURCE_ID_KEY',
    'POWER_SOURCE_STATE_KEY',
    'POWER_SOURCE_EMPTY_DICT',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_CELL_IMBALANCE',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_FET',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_OVER_CURRENT',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_OVER_TEMP',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_DATA_FLUSH_FAULT',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_FET',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_OVER_CURRENT',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_OVER_TEMP',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_EXTERNAL_INPUT',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_FUSE_BLOWN',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_OPEN_THERMISTOR',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_PERIODIC_AFE_COMMS',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_PERMANENT_AFE_COMMS',
    'POWER_SOURCE_BATTERY_FAILURE_MODE_SAFETY_OVER_VOLTAGE',
    'POWER_SOURCE_BATTERY_HEALTH_CONDITION_VALUE_CHECK_BATTERY',
    'POWER_SOURCE_BATTERY_HEALTH_CONDITION_VALUE_PERMANENT_FAILURE',
    'POWER_SOURCE_BATTERY_HEALTH_VALUE_FAIR',
    'POWER_SOURCE_BATTERY_HEALTH_VALUE_GOOD',
    'POWER_SOURCE_BATTERY_HEALTH_VALUE_POOR',
    'POWER_SOURCE_DATA_TRANSPORT_TYPE_USB',
    'POWER_SOURCE_DATA_TRANSPORT_TYPE_NETWORK',
    'POWER_SOURCE_DATA_TRANSPORT_TYPE_SERIAL',
    'POWER_SOURCE_DATA_TRANSPORT_TYPE_INTERNAL',
    'POWER_SOURCE_TYPE_UPS',
    'POWER_SOURCE_TYPE_INTERNAL_BATTERY',
    'POWER_SOURCE_STATE_AC',
    'POWER_SOURC_STATE_BATTERY',
    'POWER_SOURCE_STATE_OFFLINE',
    'PowerManagementObserver'
    ]


POWER_TYPE_AC = 0

POWER_TYPE_BATTERY = 1

POWER_TYPE_UPS = 2


LOW_BATTERY_WARNING_NONE = 1

LOW_BATTERY_WARNING_EARLY = 2

LOW_BATTERY_WARNING_FINAL = 3


TIME_REMAINING_UNKNOWN = -1.0

TIME_REMAINING_UNLIMITED = -2.0



POWER_ADAPTER_FAMILY_KEY = "Family Code"

POWER_ADAPTER_ID_KEY = "Adapter ID"

POWER_ADAPTER_REVISION_KEY = "AdapterRevision"

POWER_ADAPTER_SERIAL_NUMBER_KEY = "SerialNumber"

POWER_ADAPTER_SOURCE_KEY = "Source"

POWER_ADAPTER_WATTS_KEY = "Watts"

POWER_ADAPTER_CURRENT_KEY = "Current"

POWER_ADAPTER_EMPTY_DICT = {
    POWER_ADAPTER_FAMILY_KEY: None,
    POWER_ADAPTER_ID_KEY: None,
    POWER_ADAPTER_REVISION_KEY: None,
    POWER_ADAPTER_SERIAL_NUMBER_KEY: None,
    POWER_ADAPTER_SOURCE_KEY: None,
    POWER_ADAPTER_WATTS_KEY: None,
    POWER_ADAPTER_CURRENT_KEY:None
}


POWER_SOURCE_BATTERY_FAILURE_MODES_KEY = "Battery Failure Modes"

POWER_SOURCE_BATTERY_HEALTH_CONDITION_KEY = "Battery Health Condition"

POWER_SOURCE_BATTERY_HEALTH_KEY = "Battery Health"

POWER_SOURCE_CURRENT_CAPACITY_KEY = "Current Capacity"

POWER_SOURCE_CURRENT_KEY = "Current"

POWER_SOURCE_DESIGN_CAPACITY_KEY = "Design Capacity"

POWER_SOURCE_HARDWARE_SERIAL_NUMBER_KEY = "Hardware Serial Number"

POWER_SOURCE_IS_CHARGED_KEY = "Is Charged"

POWER_SOURCE_IS_CHARGING_KEY = "Is Charging"

POWER_SOURCE_IS_FINISHING_CHARGE_KEY = "Is Finishing Charge"

POWER_SOURCE_IS_PRESENT_KEY = "Is Present"

POWER_SOURCE_MAX_CAPACITY_KEY = "Max Capacity"

POWER_SOURCE_MAX_ERR_KEY = "MaxErr"

POWER_SOURCE_NAME_KEY = "Name"

POWER_SOURCE_TIME_TO_EMPTY_KEY = "Time to Empty"

POWER_SOURCE_TIME_TO_FULL_CHARGEKEY = "Time to Full Charge"

POWER_SOURCE_TRANSPORT_TYPE_KEY = "Transport Type"

POWER_SOURCE_TYPE_KEY = "Type"

POWER_SOURCE_VENDOR_DATA_KEY = "Vendor Specific Data"

POWER_SOURCE_VOLTAGE_KEY = "Voltage"

POWER_SOURCE_ID_KEY = "Power Source ID"

POWER_SOURCE_STATE_KEY = "Power Source State"

POWER_SOURCE_EMPTY_DICT = {
    POWER_SOURCE_BATTERY_FAILURE_MODES_KEY: None,
    POWER_SOURCE_BATTERY_HEALTH_CONDITION_KEY: None,
    POWER_SOURCE_BATTERY_HEALTH_KEY: None,
    POWER_SOURCE_CURRENT_CAPACITY_KEY: None,
    POWER_SOURCE_CURRENT_KEY: None,
    POWER_SOURCE_DESIGN_CAPACITY_KEY: None,
    POWER_SOURCE_HARDWARE_SERIAL_NUMBER_KEY: None,
    POWER_SOURCE_IS_CHARGED_KEY: None,
    POWER_SOURCE_IS_CHARGING_KEY: None,
    POWER_SOURCE_IS_FINISHING_CHARGE_KEY: None,
    POWER_SOURCE_IS_PRESENT_KEY: None,
    POWER_SOURCE_MAX_CAPACITY_KEY: None,
    POWER_SOURCE_MAX_ERR_KEY: None,
    POWER_SOURCE_NAME_KEY: None,
    POWER_SOURCE_TIME_TO_EMPTY_KEY: None,
    POWER_SOURCE_TIME_TO_FULL_CHARGEKEY: None,
    POWER_SOURCE_TRANSPORT_TYPE_KEY: None,
    POWER_SOURCE_TYPE_KEY: None,
    POWER_SOURCE_VENDOR_DATA_KEY: None,
    POWER_SOURCE_VOLTAGE_KEY: None,
    POWER_SOURCE_ID_KEY: None,
    POWER_SOURCE_STATE_KEY: None
}


POWER_SOURCE_BATTERY_FAILURE_MODE_CELL_IMBALANCE = "Cell Imbalance"

POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_FET = "Charge FET"

POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_OVER_CURRENT = "Charge Over-Current"

POWER_SOURCE_BATTERY_FAILURE_MODE_CHARGE_OVER_TEMP = "Charge Over-Temperature"

POWER_SOURCE_BATTERY_FAILURE_MODE_DATA_FLUSH_FAULT = "Data Flush Fault"

POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_FET = "Discharge FET"

POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_OVER_CURRENT = "Discharge Over-Current"

POWER_SOURCE_BATTERY_FAILURE_MODE_DISCHARGE_OVER_TEMP = "Discharge Over-Temperature"

POWER_SOURCE_BATTERY_FAILURE_MODE_EXTERNAL_INPUT = "Externally Indicated Failure"

POWER_SOURCE_BATTERY_FAILURE_MODE_FUSE_BLOWN = "Fuse Blown"

POWER_SOURCE_BATTERY_FAILURE_MODE_OPEN_THERMISTOR = "Open Thermistor"

POWER_SOURCE_BATTERY_FAILURE_MODE_PERIODIC_AFE_COMMS = "Periodic AFE Comms"

POWER_SOURCE_BATTERY_FAILURE_MODE_PERMANENT_AFE_COMMS = "Permanent AFE Comms"

POWER_SOURCE_BATTERY_FAILURE_MODE_SAFETY_OVER_VOLTAGE = "Safety Over-Voltage"


POWER_SOURCE_BATTERY_HEALTH_CONDITION_VALUE_CHECK_BATTERY = "Check Battery"

POWER_SOURCE_BATTERY_HEALTH_CONDITION_VALUE_PERMANENT_FAILURE = "Permanent Battery Failure"


POWER_SOURCE_BATTERY_HEALTH_VALUE_FAIR = "Fair"

POWER_SOURCE_BATTERY_HEALTH_VALUE_GOOD = "Good"

POWER_SOURCE_BATTERY_HEALTH_VALUE_POOR = "Poor"


POWER_SOURCE_DATA_TRANSPORT_TYPE_USB = "USB"

POWER_SOURCE_DATA_TRANSPORT_TYPE_NETWORK = "Ethernet"

POWER_SOURCE_DATA_TRANSPORT_TYPE_SERIAL = "Serial"

POWER_SOURCE_DATA_TRANSPORT_TYPE_INTERNAL = "Internal"


POWER_SOURCE_TYPE_UPS = "UPS"

POWER_SOURCE_TYPE_INTERNAL_BATTERY = "Internal Battery"


POWER_SOURCE_STATE_AC = "AC Power"

POWER_SOURC_STATE_BATTERY = "Battery Power"

POWER_SOURCE_STATE_OFFLINE = "Offline"


class PowerManagementBase(object):
    """
    Base class for platform dependent PowerManagement functions.

    @ivar _weak_observers: List of weak reference to added observers.
    @note: Platform's implementation may provide additional parameters for initialization.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self._weak_observers = []

    @abstractmethod
    def get_providing_power_source_type(self):
        """
        @return: Returns type of the providing power source.
            Possible values:
                - POWER_TYPE_AC
                - POWER_TYPE_BATTERY
                - POWER_TYPE_UPS
        @rtype: int
        """
        pass

    @abstractmethod
    def get_low_battery_warning_level(self):
        """
        Returns the system battery warning level.
        @return: Possible values:
            - LOW_BATTERY_WARNING_NONE
            - LOW_BATTERY_WARNING_EARLY
            - LOW_BATTERY_WARNING_FINAL
        @rtype: int
        """
        pass

    @abstractmethod
    def get_time_remaining_estimate(self):
        """
        Returns the estimated seconds remaining until all power sources (battery and/or UPS) are empty.
        @return: Special values:
            - TIME_REMAINING_UNKNOWN
            - TIME_REMAINING_UNLIMITED
        @rtype: float
        """
        pass

    @abstractmethod
    def get_external_power_adapter_info(self):
        """
        Returns description of the external power source or None of no external power source present.
        @return: All of the following keys are guaranteed to be present. However value of any key may be None.
            - POWER_ADAPTER_FAMILY_KEY
            - POWER_ADAPTER_ID_KEY
            - POWER_ADAPTER_REVISION_KEY
            - POWER_ADAPTER_SERIAL_NUMBER_KEY
            - POWER_ADAPTER_SOURCE_KEY
            - POWER_ADAPTER_WATTS_KEY
            - POWER_ADAPTER_CURRENT_KEY
        @rtype: dict or None
        """
        pass

    @abstractmethod
    def get_power_sources_info(self):
        """
        Returns list of dictionary descriptions of attached batteries or None if no batteries are attached.
        @return All of the following keys are guaranteed to be present. However value of any key may be None.
            - POWER_SOURCE_BATTERY_FAILURE_MODES_KEY
            - POWER_SOURCE_BATTERY_HEALTH_CONDITION_KEY
            - POWER_SOURCE_BATTERY_HEALTH_KEY
            - POWER_SOURCE_CURRENT_CAPACITY_KEY
            - POWER_SOURCE_CURRENT_KEY
            - POWER_SOURCE_DESIGN_CAPACITY_KEY
            - POWER_SOURCE_HARDWARE_SERIAL_NUMBER_KEY
            - POWER_SOURCE_IS_CHARGED_KEY
            - POWER_SOURCE_IS_CHARGING_KEY
            - POWER_SOURCE_IS_FINISHING_CHARGE_KEY
            - POWER_SOURCE_IS_PRESENT_KEY
            - POWER_SOURCE_MAX_CAPACITY_KEY
            - POWER_SOURCE_MAX_ERR_KEY
            - POWER_SOURCE_NAME_KEY
            - POWER_SOURCE_TIME_TO_EMPTY_KEY
            - POWER_SOURCE_TIME_TO_FULL_CHARGEKEY
            - POWER_SOURCE_TRANSPORT_TYPE_KEY
            - POWER_SOURCE_TYPE_KEY
            - POWER_SOURCE_VENDOR_DATA_KEY
            - POWER_SOURCE_VOLTAGE_KEY
            - POWER_SOURCE_ID_KEY
            - POWER_SOURCE_STATE_KEY
        @rtype: list or None.
        """
        pass

    @abstractmethod
    def add_observer(self, observer):
        """
        Adds an observer.

        @raise TypeError: If observer is not registered with PowerManagementObserver abstract class.
        """
        if not isinstance(observer, PowerManagementObserver):
            raise TypeError("observer MUST conform to power.PowerManagementObserver")
        self._weak_observers.append(weakref.ref(observer))

    @abstractmethod
    def remove_observer(self, observer):
        """
        Removes observer an observer.
        """
        self._weak_observers.remove(weakref.ref(observer))

    def remove_all_observers(self):
        """
        Removes all registered observers.
        """
        for weak_observer in self._weak_observers:
            observer = weak_observer()
            if observer:
                self.remove_observer(observer)


class PowerManagementObserver:
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_power_sources_change(self, power_management):
        pass

    @abstractmethod
    def on_time_remaining_change(self, power_management):
        pass
