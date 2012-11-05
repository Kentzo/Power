from ctypes import cdll, util

iokit = cdll.LoadLibrary(util.find_library('IOKit'))
cf = cdll.LoadLibrary(util.find_library('CoreFoundation'))






