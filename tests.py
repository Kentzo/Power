__author__ = 'kulakov.ilya@gmail.com'

# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

import unittest
from power import *

class TestPowerFunctions(unittest.TestCase):
    def test_providing_power_type(self):
        type = get_providing_power_type()
        self.assertIn(type, [POWER_TYPE_AC, POWER_TYPE_BATTERY, POWER_TYPE_UPS])
    def test_battery_warning(self):
        warning = get_providing_power_type()
        self.assertIn(warning, [LOW_BATTERY_WARNING_NONE, LOW_BATTERY_WARNING_EARLY, LOW_BATTERY_WARNING_FINAL])
