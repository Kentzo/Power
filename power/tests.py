# coding=utf-8
from __future__ import print_function

__author__ = 'kulakov.ilya@gmail.com'

import unittest
import power


class TestPowerManagementCommon(unittest.TestCase):
    def testGetLowBatteryWarningLevel(self):
        level = power.PowerManagement().get_low_battery_warning_level()
        self.assertIsNotNone(level)
        self.assertIsInstance(level, int)
        self.assertIn(level, [power.LOW_BATTERY_WARNING_NONE, power.LOW_BATTERY_WARNING_EARLY, power.LOW_BATTERY_WARNING_FINAL])

    def testGetRemainingEstimate(self):
        estimate = power.PowerManagement().get_time_remaining_estimate()
        self.assertIsNotNone(estimate)
        self.assertIsInstance(estimate, float)
        self.assertTrue(estimate == -1.0 or estimate == -2.0 or estimate >= 0.0)

    def testGetProvidingPowerSource(self):
        type = power.PowerManagement().get_providing_power_source_type()
        self.assertIsNotNone(type)
        self.assertIsInstance(type, int)
        self.assertIn(type, [power.POWER_TYPE_AC, power.POWER_TYPE_BATTERY, power.POWER_TYPE_UPS])

    def testGetRemainingPercentage(self):
        rem_percentage = power.PowerManagement().get_remaining_percentage()
        self.assertIsNotNone(rem_percentage)
        self.assertIsInstance(rem_percentage, float)
        self.assertTrue(rem_percentage >= 0 and rem_percentage <= 100)


class TestObserver(power.PowerManagementObserver):
    def on_power_sources_change(self, power_management):
        print("on_power_sources_change")

    def on_time_remaining_change(self, power_management):
        print("on_time_remaining_change")


if __name__ == "__main__":
    o = TestObserver()
    p = power.PowerManagement()
    p.add_observer(o)
    try:
        print("Power management observer is registered")
        import time
        while True:
            time.sleep(1)
    finally:
        p.remove_observer(o)
