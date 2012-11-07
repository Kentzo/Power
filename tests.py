# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

import unittest
from power import *
from CoreFoundation import *


class Observer(PowerManagementObserver):
    def on_power_sources_change(self, power_management):
        pass

PowerManagementObserver.register(Observer)


class TestPowerManagementObserver(unittest.TestCase):
    def setUp(self):
        self.listner = Observer()
        self.power_management = PowerManagement()
        self.power_management.add_observer(self.listner)

    def testNothing(self):
        CFRunLoopRun()
        pass
