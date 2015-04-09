"""
Unit test script for convert.py
"""

import unittest

import pyeto


class TestConvert(unittest.TestCase):

    def test_celsius2kelvin(self):
        self.assertEqual(pyeto.celsius2kelvin(0), 273.15)

    def test_kelvin2celsius(self):
        self.assertEqual(pyeto.kelvin2celsius(273.15), 0.0)

    def test_degrees2radians(self):
        self.assertEqual(pyeto.degrees2radians(0), 0.0)
        self.assertAlmostEqual(pyeto.degrees2radians(-90), -1.5707963268, 10)
        self.assertAlmostEqual(pyeto.degrees2radians(90), 1.5707963268, 10)
        self.assertAlmostEqual(pyeto.degrees2radians(360), 6.2831853072, 10)

    def test_radians2degrees(self):
        self.assertEqual(pyeto.radians2degrees(0), 0.0)
        self.assertAlmostEqual(pyeto.radians2degrees(-1.5707963268), -90.0, 10)
        self.assertAlmostEqual(pyeto.radians2degrees(1.5707963268), 90.0, 10)
        self.assertAlmostEqual(pyeto.radians2degrees(6.2831853072), 360.0, 10)


if __name__ == '__main__':
    unittest.main()