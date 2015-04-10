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

    def test_deg2rad(self):
        self.assertEqual(pyeto.deg2rad(0), 0.0)
        # Test values obtained form online conversion calculator
        self.assertAlmostEqual(pyeto.deg2rad(-90), -1.5707963268, 10)
        self.assertAlmostEqual(pyeto.deg2rad(90), 1.5707963268, 10)
        self.assertAlmostEqual(pyeto.deg2rad(360), 6.2831853072, 10)

    def test_rad2deg(self):
        self.assertEqual(pyeto.rad2deg(0), 0.0)
        # Test values obtained form online conversion calculator
        self.assertAlmostEqual(pyeto.rad2deg(-1.5707963268), -90.0)
        self.assertAlmostEqual(pyeto.rad2deg(1.5707963268), 90.0)
        self.assertAlmostEqual(pyeto.rad2deg(6.2831853072), 360.0)


if __name__ == '__main__':
    unittest.main()