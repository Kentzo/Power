# coding=utf-8
"""
Represents common constants and classes for all platforms.

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

@type STATUS_UNKNOWN: int
@type STATUS_AC: int
@type STATUS_CHARGING: int
@type STATUS_DISCHARGING: int
@type STATUS_FULL: int
@type STATUS_FULL_ONAC: int

"""
__author__ = 'kulakov.ilya@gmail.com'
__maintainer__ = 'oskari.rauta@gmail.com'

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
    'STATUS_UNKNOWN',
    'STATUS_AC',
    'STATUS_CHARGING',
    'STATUS_DISCHARGING',
    'STATUS_FULL',
    'STATUS_FULL_ONAC',
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

STATUS_UNKNOWN = 0

STATUS_AC = 1

STATUS_CHARGING = 2

STATUS_DISCHARGING = 3

STATUS_FULL = 4

STATUS_FULL_ONAC = 5

class PowerManagementBase(object):
    """
    Base class for platform dependent PowerManagement functions.

    @ivar _weak_observers: List of weak reference to added observers
    @note: Platform's implementation may provide additional parameters for initialization
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self._weak_observers = []

    @abstractmethod
    def get_providing_power_source_type(self):
        """
        Returns type of the providing power source.

        @return: Possible values:
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
    def get_ac_status(self):
        """
        Looks through all power sources.

        Returns AC's current status, time remaining in minutes for all power sources either to
        empty or to full, whether system is charging or not and average of capacity on all
        batteries (always 100 on AC only system).

	@return: Special values for status
            - STATUS_UNKNOWN       (0 - on error)
            - STATUS_AC            (1 - AC only system)
            - STATUS_CHARGING      (2)
            - STATUS_DISCHARGING   (3)
            - STATUS_FULL          (4 - batteries are full, system not on AC)
            - STATUS_FULL_ONAC     (5 - batteries are full, system is on AC)

        @rtype: int

        @return: Special values for time remaining
            - TIME_REMAINING_UNKNOWN (-1.0)
            - TIME_REMAINING_UNLIMITED (-2.0)

        @rtype: float

	@return: capacity

        @rtype: float
        """
        pass

    @abstractmethod
    def add_observer(self, observer):
        """
        Adds weak ref to an observer.

        @param observer: Instance of class registered with PowerManagementObserver
        @raise TypeError: If observer is not registered with PowerManagementObserver abstract class
        """
        if not isinstance(observer, PowerManagementObserver):
            raise TypeError("observer MUST conform to power.PowerManagementObserver")
        self._weak_observers.append(weakref.ref(observer))

    @abstractmethod
    def remove_observer(self, observer):
        """
        Removes an observer.

        @param observer: Previously added observer
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
    """
    Base class for PowerManagement observers.
    Do not make assumptions in what thread or event loop these methods are called.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_power_sources_change(self, power_management):
        """
        @param power_management: Instance of PowerManagement posted notification
        """
        pass

    @abstractmethod
    def on_time_remaining_change(self, power_management):
        """
        @param power_management: Instance of PowerManagement posted notification
        """
        pass


class PowerManagementNoop(PowerManagementBase):
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

    def get_ac_status(self):
        """
        @return: Always STATUS_AC, TIME_REMAINING_UNLIMITED, 100
        """
        return STATUS_AC, TIME_REMAINING_UNLIMITED, 100

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
