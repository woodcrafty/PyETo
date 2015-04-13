"""
Unit test script for pyeto._check.py
"""

import unittest

from pyeto import _check
from pyeto.convert import deg2rad


class TestCheck(unittest.TestCase):

    def test_check_day_hours(self):
        with self.assertRaises(ValueError):
            _check.check_day_hours(-1, 'test')

        with self.assertRaises(ValueError):
            _check.check_day_hours(25, 'test')

        self.assertIsNone(_check.check_day_hours(0, 'test'))
        self.assertIsNone(_check.check_day_hours(24, 'test'))

    def test_check_doy(self):
        with self.assertRaises(ValueError):
            _check.check_doy(0)

        with self.assertRaises(ValueError):
            _check.check_doy(367)

        self.assertIsNone(_check.check_doy(1))
        self.assertIsNone(_check.check_doy(366))

    def test_check_latitude_rad(self):
        with self.assertRaises(ValueError):
            _check.check_latitude_rad(deg2rad(-90.0001))

        with self.assertRaises(ValueError):
            _check.check_latitude_rad(deg2rad(90.0001))

        self.assertIsNone(_check.check_latitude_rad(deg2rad(-90)))
        self.assertIsNone(_check.check_latitude_rad(deg2rad(90)))

    def test_check_sol_dec_rad(self):
        with self.assertRaises(ValueError):
            _check.check_sol_dec_rad(deg2rad(-23.5001))

        with self.assertRaises(ValueError):
            _check.check_sol_dec_rad(deg2rad(23.5001))

        self.assertIsNone(_check.check_sol_dec_rad(deg2rad(-23.5)))
        self.assertIsNone(_check.check_sol_dec_rad(deg2rad(23.5)))

    def test_check_sunset_hour_angle_rad(self):
        with self.assertRaises(ValueError):
            _check.check_sunset_hour_angle_rad(deg2rad(-0.00001))

        with self.assertRaises(ValueError):
            _check.check_sunset_hour_angle_rad(deg2rad(180.00001))

        self.assertIsNone(_check.check_sunset_hour_angle_rad(deg2rad(0.0)))
        self.assertIsNone(_check.check_sunset_hour_angle_rad(deg2rad(180.0)))
