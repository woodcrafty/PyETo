"""
Unit test script for pyeto.thornthwaite.py
"""

import unittest

import pyeto


class TestThornthwaite(unittest.TestCase):

    def test_monthly_mean_daylight_hours(self):
        # Test against values obtained for Los Angles, California,
        # latitude 34 deg 05' N, from
        # http://aa.usno.navy.mil/data/docs/Dur_OneYear.php
        latitude = pyeto.degrees2radians(34.0833333)
        la_mmdlh = [
            10.182,  # Jan
            10.973,  # Feb
            11.985,  # Mar
            13.046,  # Apr
            13.940,  # May
            14.388,  # Jun
            14.163,  # Jul
            13.404,  # Aug
            12.374,  # Sep
            11.320,  # Oct
            10.401,  # Nov
            9.928,   # Dec
        ]

        mmdlh = pyeto.monthly_mean_daylight_hours(latitude)

        # Check that the 2 methods are almost the same (within 15 minutes)
        for m in range(12):
            self.assertAlmostEqual(mmdlh[m], la_mmdlh[m], delta=0.25)

        # Test with bad latitude
        with self.assertRaises(ValueError):
            _ = pyeto.monthly_mean_daylight_hours(
                pyeto.degrees2radians(90.01))

        with self.assertRaises(ValueError):
            _ = pyeto.monthly_mean_daylight_hours(
                pyeto.degrees2radians(-90.01))

        # Test limits of latitude
        _ = pyeto.monthly_mean_daylight_hours(
            pyeto.degrees2radians(90.0))

        _ = pyeto.monthly_mean_daylight_hours(
            pyeto.degrees2radians(-90.0))


if __name__ == '__main__':
    unittest.main()
