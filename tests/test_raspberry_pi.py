# Raspberry Pi test
import unittest
from sentinel.hardware_backends.raspberry_pi import RaspberryPiBackend

class TestRaspberryPi(unittest.TestCase):
    def test_initialization(self):
        pi = RaspberryPiBackend()
        pi.initialize()
        self.assertTrue(True)  # Just a basic test