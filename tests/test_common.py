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
        self.assertTrue(estimate == power.TIME_REMAINING_UNKNOWN or estimate == power.TIME_REMAINING_UNLIMITED or estimate >= 0.0)

    def testGetProvidingPowerSource(self):
        type = power.PowerManagement().get_providing_power_source_type()
        self.assertIsNotNone(type)
        self.assertIsInstance(type, int)
        self.assertIn(type, [power.POWER_TYPE_AC, power.POWER_TYPE_BATTERY, power.POWER_TYPE_UPS])
