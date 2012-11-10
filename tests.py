# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

import unittest
import power
from CoreFoundation import *


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

    def testGetExternalPowerAdapter(self):
        info = power.PowerManagement().get_external_power_adapter_info()
        self.assertTrue(info is None or isinstance(info, dict))
        if info is not None:
            self.assertTrue(info[power.POWER_ADAPTER_FAMILY_KEY] is None or isinstance(info[power.POWER_ADAPTER_FAMILY_KEY], int))
            self.assertTrue(info[power.POWER_ADAPTER_ID_KEY] is None or isinstance(info[power.POWER_ADAPTER_FAMILY_KEY], int))
            self.assertTrue(info[power.POWER_ADAPTER_REVISION_KEY] is None or isinstance(info[power.POWER_ADAPTER_FAMILY_KEY], int))
            self.assertTrue(info[power.POWER_ADAPTER_SERIAL_NUMBER_KEY] is None or isinstance(info[power.POWER_ADAPTER_FAMILY_KEY], int))
            self.assertTrue(info[power.POWER_ADAPTER_SOURCE_KEY] is None or isinstance(info[power.POWER_ADAPTER_FAMILY_KEY], int))
            self.assertTrue(info[power.POWER_ADAPTER_WATTS_KEY] is None or isinstance(info[power.POWER_ADAPTER_FAMILY_KEY], int))
            self.assertTrue(info[power.POWER_ADAPTER_CURRENT_KEY] is None or isinstance(info[power.POWER_ADAPTER_FAMILY_KEY], int))

    def testGetPowerSourcesInfo(self):
        info = power.PowerManagement().get_power_sources_info()
        self.assertTrue(info is None or isinstance(info, list))
        if info is not None:
            for source in info:
                pass