# coding=utf-8
from __future__ import print_function

try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    import unittest.mock as mock
except ImportError:
    import mock

import power.common


class TestPowerManagementCommon(unittest.TestCase):
    def test_get_low_battery_warningLevel(self):
        level = power.PowerManagement().get_low_battery_warning_level()
        self.assertIsNotNone(level)
        self.assertIsInstance(level, int)
        self.assertIn(level, [power.LOW_BATTERY_WARNING_NONE, power.LOW_BATTERY_WARNING_EARLY, power.LOW_BATTERY_WARNING_FINAL])

    def test_get_remaining_estimate(self):
        estimate = power.PowerManagement().get_time_remaining_estimate()
        self.assertIsNotNone(estimate)
        self.assertIsInstance(estimate, float)
        self.assertTrue(estimate == power.TIME_REMAINING_UNKNOWN or estimate == power.TIME_REMAINING_UNLIMITED or estimate >= 0.0)

    def test_get_providing_power_source(self):
        type = power.PowerManagement().get_providing_power_source_type()
        self.assertIsNotNone(type)
        self.assertIsInstance(type, int)
        self.assertIn(type, [power.POWER_TYPE_AC, power.POWER_TYPE_BATTERY, power.POWER_TYPE_UPS])

    def test_fallback_unsupported_platform(self):
        with mock.patch('sys.platform', 'planb'):
            self.assertEqual(power.get_power_management_class(), power.common.PowerManagementNoop)

    def test_fallback_importError(self):
        with mock.patch('power.get_platform_power_management_class', side_effect=RuntimeError):
            self.assertEqual(power.get_power_management_class(), power.common.PowerManagementNoop)

    def test_fallback_usage_error(self):
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

        with mock.patch('power.get_platform_power_management_class', return_value=PowerManagementFaulty):
            c = power.get_power_management_class()
            self.assertTrue(issubclass(c, PowerManagementFaulty))

            with self.assertWarns(RuntimeWarning):
                pm = c()
                self.assertEqual(pm.get_providing_power_source_type(), power.POWER_TYPE_AC)
