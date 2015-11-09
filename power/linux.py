# coding=utf-8
"""
Implements PowerManagement functions using /sys/class/power_supply/*
See doc/linux for platform-specific details.

"""
__author__ = 'kulakov.ilya@gmail.com'
__maintainer__ = 'oskari.rauta@gmail.com'

import os
import warnings
from power import common


POWER_SUPPLY_PATH = '/sys/class/power_supply'


if not os.access(POWER_SUPPLY_PATH, os.R_OK):
    raise RuntimeError("Unable to read {path}.".format(path=POWER_SUPPLY_PATH))


class PowerManagement(common.PowerManagementBase):
    @staticmethod
    def power_source_type(supply_path):
        """
        @param supply_path: Path to power supply
        @return: One of common.POWER_TYPE_*
        @raise: Runtime error if type of power source is not supported
        """
        with open(os.path.join(supply_path, 'type'), 'r') as type_file:
            type = type_file.readline().strip()
            if type == 'Mains':
                return common.POWER_TYPE_AC
            elif type == 'UPS':
                return common.POWER_TYPE_UPS
            elif type == 'Battery':
                return common.POWER_TYPE_BATTERY
            else:
                raise RuntimeError("Type of {path} ({type}) is not supported".format(path=supply_path, type=type))

    @staticmethod
    def is_ac_online(supply_path):
        """
        @param supply_path: Path to power supply
        @return: True if ac is online. Otherwise False
        """
        with open(os.path.join(supply_path, 'online'), 'r') as online_file:
            return online_file.readline().strip() == '1'

    @staticmethod
    def is_battery_present(supply_path):
        """
        @param supply_path: Path to power supply
        @return: True if battery is present. Otherwise False
        """
        with open(os.path.join(supply_path, 'present'), 'r') as present_file:
            return present_file.readline().strip() == '1'

    @staticmethod
    def is_battery_full(supply_path):
        """
            @param supply_path: Path to power supply
            @return: True if battery is full. Otherwise False
            """
        with open(os.path.join(supply_path, 'status'), 'r') as status_file:
            return status_file.readline().strip() == 'Full'
    
    @staticmethod
    def is_battery_discharging(supply_path):
        """
        @param supply_path: Path to power supply
        @return: True if battery is discharging. Otherwise False
        """
        with open(os.path.join(supply_path, 'status'), 'r') as status_file:
            return status_file.readline().strip() == 'Discharging'

    @staticmethod
    def is_battery_charging(supply_path):
        """
            @param supply_path: Path to power supply
            @return: True if battery is charging. Otherwise False
            """
        with open(os.path.join(supply_path, 'status'), 'r') as status_file:
            return status_file.readline().strip() == 'Charging'

    @staticmethod
    def get_battery_state(supply_path):
        """
        @param supply_path: Path to power supply
        @return: Tuple (energy_full, energy_now, power_now, capacity)
        """
        
        energy_now_filename = 'charge_now'
        power_now_filename = 'current_now'
        energy_full_filename = 'charge_full'
        
        if not os.path.isfile(os.path.join(supply_path, energy_now_filename)) or not os.path.isfile(os.path.join(supply_path, power_now_filename)) or not os.path.isfile(os.path.join(supply_path, energy_full_filename)):

            if os.path.isfile(os.path.join(supply_path, 'energy_now')) and os.path.isfile(os.path.join(supply_path, 'power_now')) and os.path.isfile(os.path.join(supply_path, 'energy_full')):
                energy_now_filename = 'energy_now'
                power_now_filename = 'power_now'
                energy_full_filename = 'energy_full'
            elif os.path.isfile(os.path.join(supply_path, 'energy_now')) and os.path.isfile(os.path.join(supply_path, 'current_now')) and os.path.isfile(os.path.join(supply_path, 'energy_full')):
                energy_now_filename = 'energy_now'
                power_now_filename = 'current_now'
                energy_full_filename = 'energy_full'
        
        with open(os.path.join(supply_path, energy_now_filename), 'r') as energy_now_file:
            with open(os.path.join(supply_path, power_now_filename), 'r') as power_now_file:
                with open(os.path.join(supply_path, energy_full_filename), 'r') as energy_full_file:
                    with open(os.path.join(supply_path, 'capacity'), 'r') as capacity_file:
                        energy_now = float(energy_now_file.readline().strip())
                        power_now = float(power_now_file.readline().strip())
                        energy_full = float(energy_full_file.readline().strip())
                        capacity = float(capacity_file.readline().strip())
                        return energy_full, energy_now, power_now, capacity

    def get_providing_power_source_type(self):
        """
        Looks through all power supplies in POWER_SUPPLY_PATH.
        If there is an AC adapter online returns POWER_TYPE_AC.
        If there is a discharging battery, returns POWER_TYPE_BATTERY.
        Since the order of supplies is arbitrary, whatever found first is returned.
        """
        for supply in os.listdir(POWER_SUPPLY_PATH):
            supply_path = os.path.join(POWER_SUPPLY_PATH, supply)
            try:
                type = self.power_source_type(supply_path)
                if type == common.POWER_TYPE_AC:
                    if self.is_ac_online(supply_path):
                        return common.POWER_TYPE_AC
                elif type == common.POWER_TYPE_BATTERY:
                    if self.is_battery_present(supply_path) and self.is_battery_discharging(supply_path):
                        return common.POWER_TYPE_BATTERY
                else:
                    warnings.warn("UPS is not supported.")
            except (RuntimeError, IOError) as e:
                warnings.warn("Unable to read properties of {path}: {error}".format(path=supply_path, error=str(e)))

        return common.POWER_TYPE_AC

    def get_low_battery_warning_level(self):
        """
        Looks through all power supplies in POWER_SUPPLY_PATH.
        If there is an AC adapter online returns LOW_BATTERY_WARNING_NONE.
        Otherwise determines total percentage and time remaining across all attached batteries.
        """
        all_energy_full = []
        all_energy_now = []
        all_power_now = []
        for supply in os.listdir(POWER_SUPPLY_PATH):
            supply_path = os.path.join(POWER_SUPPLY_PATH, supply)
            try:
                type = self.power_source_type(supply_path)
                if type == common.POWER_TYPE_AC:
                    if self.is_ac_online(supply_path):
                        return common.LOW_BATTERY_WARNING_NONE
                elif type == common.POWER_TYPE_BATTERY:
                    if self.is_battery_present(supply_path) and self.is_battery_discharging(supply_path):
                        energy_full, energy_now, power_now, capacity = self.get_battery_state(supply_path)
                        all_energy_full.append(energy_full)
                        all_energy_now.append(energy_now)
                        all_power_now.append(power_now)
                else:
                    warnings.warn("UPS is not supported.")
            except (RuntimeError, IOError) as e:
                warnings.warn("Unable to read properties of {path}: {error}".format(path=supply_path, error=str(e)))

        try:
            total_percentage = sum(all_energy_full) / sum(all_energy_now)
            total_time = sum([energy_now / power_now * 60.0 for energy_now, power_now in zip(all_energy_now, all_power_now)])
            if total_time <= 10.0:
                return common.LOW_BATTERY_WARNING_FINAL
            elif total_percentage <= 22.0:
                return common.LOW_BATTERY_WARNING_EARLY
            else:
                return common.LOW_BATTERY_WARNING_NONE
        except ZeroDivisionError as e:
            warnings.warn("Unable to calculate low battery level: {error}".format(error=str(e)))
            return common.LOW_BATTERY_WARNING_NONE

    def get_ac_status(self):
        """
        Looks through all power sources.
        @return: Tuple (status, time_remaining, capacity)
        status in: STATUS_UNKNOWN(0, on error), STATUS_AC(AC only, 1), STATUS_CHARGING(2),
                   STATUS_DISCHARGING(3), STATUS_FULL(4), STATUS_FULL_ONAC(5)
        time_remaining: amount of minutes left until full or empty, whether battery is being charged or is 
                        discharging. Returns TIME_REMAINING_UNLIMITED(-2.0) when battery is full and ac is
                        online. TIME_REMAINING_UNKNOWN is returned on error.
        capacity: battery's capacity in %'s between 0-100. If multiple batteries are found, this
                  will be average. 0 is returned on error.
        
        On AC only systems returns STATUS_AC, TIME_REMAINING_UNLIMITED, capacity 100.
        On error will return STATUS_UNKNOWN, TIME_REMAINING_UNKNOWN, capacity 0.
        """
        all_energy_now = []
        all_power_now = []
        all_energy_full = []
        all_capacity = []
        battery_full = True
        battery_discharging = True
        ac_is_online = False
        for supply in os.listdir(POWER_SUPPLY_PATH):
            supply_path = os.path.join(POWER_SUPPLY_PATH, supply)
            try:
                type = self.power_source_type(supply_path)
                if type == common.POWER_TYPE_AC:
                    if self.is_ac_online(supply_path):
                        ac_is_online = True
                elif type == common.POWER_TYPE_BATTERY:
                    if self.is_battery_present(supply_path):
                        energy_full, energy_now, power_now, capacity = self.get_battery_state(supply_path)
                        all_energy_now.append(energy_now)
                        all_power_now.append(power_now)
                        all_energy_full.append(energy_full)
                        all_capacity.append(capacity)
                        if self.is_battery_charging(supply_path):
                            battery_discharging = False
                        if not self.is_battery_full(supply_path):
                            battery_full = False
                else:
                    warnings.warn("UPS is not supported.")
            except (RuntimeError, IOError) as e:
                warnings.warn("Unable to read properties of {path}: {error}".format(path=supply_path, error=str(e)))

        if len(all_energy_now) == 0:
            if ac_is_online:
                return common.STATUS_AC, common.TIME_REMAINING_UNLIMITED, 100
            else:
                return common.STATUS_UNKNOWN, common.TIME_REMAINING_UNKNOWN, 0

        capacity = sum(all_capacity) / len(all_capacity)

        if battery_full and ac_is_online:
            return common.STATUS_FULL_ONAC, common.TIME_REMAINING_UNLIMITED, capacity
        elif battery_full and not ac_is_online:
            try:
                return common.STATUS_FULL, sum([energy_now / power_now * 60.0 for energy_now, power_now in zip(all_energy_now, all_power_now)]), capacity
            except ZeroDivisionError as e:
                warnings.warn("Unable to calculate time remaining estimate: {error}".format(error=str(e)))
                return common.STATUS_UNKNOWN, common.TIME_REMAINING_UNKNOWN, 0
        elif battery_discharging:
            try:
                return common.STATUS_DISCHARGING, sum([energy_now / power_now * 60.0 for energy_now, power_now in zip(all_energy_now, all_power_now)]), capacity
            except ZeroDivisionError as e:
                warnings.warn("Unable to calculate time remaining estimate: {error}".format(error=str(e)))
                return common.STATUS_UNKNOWN, common.TIME_REMAINING_UNKNOWN, 0
        elif not battery_discharging:
            if not ac_is_online:
                warnings.warn("AC is not online but battery is charging?")
            try:
                return common.STATUS_CHARGING, sum([((energy_full - energy_now) / power_now) * 60.0 for energy_full, energy_now, power_now in zip(all_energy_full, all_energy_now, all_power_now)]), capacity
            except ZeroDivisionError as e:
                warnings.warn("Unable to calculate time remaining estimate: {error}".format(error=str(e)))
                return common.STATUS_UNKNOWN, common.TIME_REMAINING_UNKNOWN, 0
        else:
            return common.STATUS_UNKNOWN, common.TIME_REMAINING_UNKNOWN, 0

    def add_observer(self, observer):
        warnings.warn("Current system does not support observing.")
        pass

    def remove_observer(self, observer):
        warnings.warn("Current system does not support observing.")
        pass
