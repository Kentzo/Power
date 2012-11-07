# coding=utf-8
__author__ = 'kulakov.ilya@gmail.com'

from sys import platform


if platform.startswith('darwin'):
    from darwin import PowerManagement
elif platform.startswith('win32'):
    from win32 import PowerManagement
else:
    raise NotImplementedError("%s is not supported. If you believe it should be supported, check the %s".format(platform, __file__))

from base import PowerManagementObserver

__all__ = ["PowerManagement", "PowerManagementObserver"]
