import unittest
import sys

from uiautomator import Device
from feature.Main import *
import Value

Value.MOBILE_SERIAL_NUMBER = str(sys.argv[1])
Value.dMobile = Device(Value.MOBILE_SERIAL_NUMBER)
suite = unittest.TestSuite()

# add_new_notes_in_list()
suite.addTest(Main('add_new_notes_in_list'))
# suite.addTest(TestAppTestCase('add_new_item_in_exist_note'))
# suite.addTest(TestAppTestCase('item_is_checked'))
unittest.TextTestRunner().run(suite)
