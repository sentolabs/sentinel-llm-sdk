# Plugin test
import unittest
from sentinel.plugins.servo_control import ServoControlPlugin

class TestPlugins(unittest.TestCase):
    def test_servo_control(self):
        plugin = ServoControlPlugin()
        plugin.move(90)
        self.assertTrue(True)  # Just a basic test