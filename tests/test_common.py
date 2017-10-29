# coding=utf-8
from __future__ import print_function
import unittest.mock

import power.common


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

    def testFallback(self):
        with self.subTest('unsupported platform'):
            with unittest.mock.patch('sys.platform', 'planb'):
                self.assertEqual(power.get_power_management_class(), power.common.PowerManagementNoop)

        with self.subTest('import error'):
            with unittest.mock.patch('power.get_platform_power_management_class', side_effect=RuntimeError):
                self.assertEqual(power.get_power_management_class(), power.common.PowerManagementNoop)

        with self.subTest('usage error'):
            class PowerManagementFaulty(power.common.PowerManagementBase):
                def add_observer(self, observer):
                    raise RuntimeError()

                def remove_observer(self, observer):
                    raise RuntimeError()

                def get_providing_power_source_type(self):
                    raise RuntimeError()

                def get_time_remaining_estimate(self):
                    raise RuntimeError()

                def get_low_battery_warning_level(self):
                    raise RuntimeError()

            with unittest.mock.patch('power.get_platform_power_management_class', return_value=PowerManagementFaulty):
                c = power.get_power_management_class()
                self.assertTrue(issubclass(c, PowerManagementFaulty))

                with self.assertWarns(RuntimeWarning):
                    pm = c()
                    pm.get_providing_power_source_type()
