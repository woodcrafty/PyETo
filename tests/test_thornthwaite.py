"""
Unit test script for pyeto.thornthwaite.py
"""

import unittest

import pyeto


class TestThornthwaite(unittest.TestCase):

    def test_monthly_mean_daylight_hours(self):
        # Test against values for latitude 20 deg N from Bautista et al (2009)
        # Calibration of the equations of Hargreaves and Thornthwaite to
        # estimate the potential evapotranspiration in semi-arid and subhumid
        # tropical climates for regional applications. Atmosfera 22(4), 331-
        # 348.
        test_mmdlh = [
            10.9,  # Jan
            11.3,  # Feb
            11.9,  # Mar
            12.5,  # Apr
            12.9,  # May
            13.2,  # Jun
            13.1,  # Jul
            12.7,  # Aug
            12.1,  # Sep
            11.5,  # Oct
            11.0,  # Nov
            10.8,  # Dec
        ]
        mmdlh = pyeto.monthly_mean_daylight_hours(pyeto.deg2rad(20.0))
        # Values were only quoted to 1 decimal place so check they are accurate
        # to within 12 minutes (0.2 hours)
        for m in range(12):
            self.assertAlmostEqual(mmdlh[m], test_mmdlh[m], delta=0.15)

        # Test against values for latitude 46 deg N from Mimikou M. and
        # Baltas E., Technical hydrology, Second edition, NTUA, 2002.
        # cited in PAPADOPOULOU E., VARANOU E., BALTAS E., DASSAKLIS A., and
        # MIMIKOU M. (2003) ESTIMATING POTENTIAL EVAPOTRANSPIRATION AND ITS
        # SPATIAL DISTRIBUTION IN GREECE USING EMPIRICAL METHODS.
        test_mmdlh = [
            8.9,   # Jan
            10.1,  # Feb
            11.6,  # Mar
            13.3,  # Apr
            14.7,  # May
            15.5,  # Jun
            15.2,  # Jul
            13.9,  # Aug
            12.3,  # Sep
            10.7,  # Oct
            9.2,   # Nov
            8.5,   # Dec
        ]
        mmdlh = pyeto.monthly_mean_daylight_hours(pyeto.deg2rad(46.0))
        # Values were only quoted to 1 decimal place so check they are accurate
        # to within 12 minutes (0.2 hours)
        for m in range(12):
            self.assertAlmostEqual(mmdlh[m], test_mmdlh[m], delta=0.15)

        # Test against values obtained for Los Angles, California,
        # latitude 34 deg 05' N, from
        # http://aa.usno.navy.mil/data/docs/Dur_OneYear.php
        latitude = pyeto.deg2rad(34.0833333)
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

        # Test with year set to a non-leap year
        non_leap = pyeto.monthly_mean_daylight_hours(latitude, 2015)
        for m in range(12):
            self.assertEqual(mmdlh[m], non_leap[m])

        # Test with year set to a leap year
        leap = pyeto.monthly_mean_daylight_hours(latitude, 2016)
        for m in range(12):
            if m == 0:
                self.assertEqual(leap[m], non_leap[m])
            elif m == 1:  # Feb
                # Because Feb extends further into year in a leap year it
                # should have a slightly longer mean day length in northern
                # hemisphere
                self.assertGreater(leap[m], non_leap[m])
            else:
                # All months after Feb in a lieap year will be composed of
                # diffent Julian days (days of the year) compared to a
                # non-leap year so will have different mean daylengths.
                self.assertNotEqual(leap[m], non_leap[m])

        # Test with bad latitude
        with self.assertRaises(ValueError):
            _ = pyeto.monthly_mean_daylight_hours(
                pyeto.deg2rad(90.01))

        with self.assertRaises(ValueError):
            _ = pyeto.monthly_mean_daylight_hours(
                pyeto.deg2rad(-90.01))

        # Test limits of latitude
        _ = pyeto.monthly_mean_daylight_hours(
            pyeto.deg2rad(90.0))

        _ = pyeto.monthly_mean_daylight_hours(
            pyeto.deg2rad(-90.0))

    def test_thornthwaite(self):
        # Test values obtained from a worked example in Hydrology: An
        # Environmental Approach, pp 435-436 by Ian Watson.
        test_monthly_t = [
            2.1, 2.5, 4.8, 7.1, 8.3, 10.7, 13.4, 14.5, 11.1, 8.2, 5.4, 3.7]
        test_monthly_mean_dlh = [
            9.4, 10.6, 11.9, 13.4, 14.6, 15.2, 14.9, 13.9, 12.6, 11.1, 9.8, 9.1]
        test_pet = [
            10.67, 14.08, 28.49, 45.85, 57.47, 75.20, 89.91, 90.29, 64.26,
            43.34, 26.24, 17.31]

        # NOTE: The test PET was calculated using rounded coefficients, rounded
        # intermediate values and doesn't adjust for the number of days in
        # the month. This results in a small difference in estimated monthly
        # PET of up to +/- 4 mm.
        pet = pyeto.thornthwaite(test_monthly_t, test_monthly_mean_dlh)
        for m in range(12):
            diff = abs(pet[m] - test_pet[m])
            self.assertLess(diff, 4)

        # Test with non-leap year
        pet_non_leap = pyeto.thornthwaite(
            test_monthly_t, test_monthly_mean_dlh, year=2015)
        # Test results are same as above when year argument is set
        for m in range(12):
            self.assertEqual(pet[m], pet_non_leap[m])

        # Test with leap year
        pet_leap = pyeto.thornthwaite(
            test_monthly_t, test_monthly_mean_dlh, year=2016)
        for m in range(12):
            # 29 days in Feb so PET should be higher than in non-leap year
            # results
            if m == 1:  # Feb
                self.assertGreater(pet_leap[m], pet_non_leap[m])
            else:
                self.assertEqual(pet_leap[m], pet_non_leap[m])

        # Test with wrong length args
        with self.assertRaises(ValueError):
            _ = pyeto.thornthwaite(list(range(11)), test_monthly_mean_dlh)
        with self.assertRaises(ValueError):
            _ = pyeto.thornthwaite(list(range(13)), test_monthly_mean_dlh)
        with self.assertRaises(ValueError):
            _ = pyeto.thornthwaite(test_monthly_t, list(range(11)))
        with self.assertRaises(ValueError):
            _ = pyeto.thornthwaite(test_monthly_t, list(range(13)))


if __name__ == '__main__':
    unittest.main()
