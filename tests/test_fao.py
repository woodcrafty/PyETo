"""
Unit test script for fao.py

TODO:
Find test values for hargreaves()
"""

import unittest

import pyeto
from pyeto import convert


class TestFAO(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_atm_pressure(self):
        # Test based on example 2, p.63 of FAO paper
        p = pyeto.atm_pressure(1800)
        self.assertAlmostEqual(p, 81.8, 1)

    def test_csy_rad(self):
        # Test based on example 18, p.115 of FAO paper
        csr = pyeto.cs_rad(100, 41.09)
        self.assertAlmostEqual(csr, 30.90, 2)

    def test_daily_mean_t(self):
        tmean = pyeto.daily_mean_t(10, 20)
        self.assertEqual(tmean, 15.0)

    def test_daylight_hours(self):
        # Test based on example 9, p.83 of FAO paper
        dh = pyeto.daylight_hours(1.527)
        self.assertAlmostEqual(dh, 11.7, 1)

    def test_delta_svp(self):
        # Test based on example 17, p.111 of FAO paper
        dh = pyeto.delta_svp(30.2)
        self.assertAlmostEqual(dh, 0.246, 3)

    def test_avp_from_tmin(self):
        # Test based on example 20, p.121 of FAO paper
        avp = pyeto.avp_from_tmin(14.8)
        self.assertAlmostEqual(avp, 1.68, 2)

    def test_avp_from_rhmin_rhmax(self):
        # Test based on example 5, p.72 of FAO paper
        avp = pyeto.avp_from_rhmin_rhmax(2.064, 3.168, 54, 82)
        self.assertAlmostEqual(avp, 1.70, 2)

    def test_avp_from_rhmax(self):
        avp = pyeto.avp_from_rhmax(2.064, 82)
        self.assertAlmostEqual(avp, 1.69, 2)

    def test_avp_from_rhmean(self):
        # Test based on FAO example 5
        avp = pyeto.avp_from_rhmean(2.064, 3.168, (82+54)/2.0)
        self.assertAlmostEqual(avp, 1.78, 2)

    def test_avp_from_tdew(self):
        # Test based on example 20, p.121 of FAO paper
        avp = pyeto.avp_from_tdew(14.8)
        self.assertAlmostEqual(avp, 1.68, 2)

    def test_avp_from_twet_tdry(self):
        # Test based on example 4, p.70 of FAO paper
        avp = pyeto.avp_from_twet_tdry(19.5, 25.6, 2.267, 0.000662*87.9)
        self.assertAlmostEqual(avp, 1.91, 2)

    def test_et_rad(self):
        # Test based on example 8, p.80 of FAO paper
        etrad = pyeto.et_rad(convert.deg2rad(-20), 0.120, 1.527, 0.985)
        self.assertAlmostEqual(etrad, 32.2, 1)

    def test_energy2evap(self):
        # Test based on example 13, p.90 of FAO paper
        evap = pyeto.energy2evap(0.33)
        self.assertAlmostEqual(evap, 0.13, 2)

    def test_fao56_penman_monteith(self):
        # Test based on example 17, p.110 (monthly calc) and
        # example 18, p.113 (daily calc) of FAO paper

        # Monthly ETo:
        # Note, due to rounding errors in the FAO's example we can only
        # test to 1 decimal place here!
        eto = pyeto.fao56_penman_monteith(
            net_rad=14.33,
            t=convert.celsius2kelvin(30.2),
            ws=2.0,
            svp=4.42,
            avp=2.85,
            delta_svp=0.246,
            psy=0.0674,
            shf=0.14,
        )
        self.assertAlmostEqual(eto, 5.72, 1)

        # Daily ETo:
        # (Rn, t, ws, es, ea, delta_es, psy, shf=0.0)
        eto = pyeto.fao56_penman_monteith(
            net_rad=13.28,
            t=convert.celsius2kelvin(16.9),
            ws=2.078,
            svp=1.997,
            avp=1.409,
            delta_svp=0.122,
            psy=0.0666
        )
        self.assertAlmostEqual(eto, 3.9, 1)

    def test_hargreaves(self):
        # Tested against worked example from "Estimating Evapotranspiration
        # from weather data" by Vishal K. Mehta, Arghyam/Cornell University,
        # Nov 2, 2006.
        eto = pyeto.hargreaves(tmin=28, tmax=38, tmean=35, et_rad=38.93715)
        self.assertAlmostEqual(eto, 6.1, 1)

    def test_inv_rel_dist_earth_sun(self):
        # Test based on example 8, p.80 of FAO paper
        irl = pyeto.inv_rel_dist_earth_sun(246)
        self.assertAlmostEqual(irl, 0.985, 3)

    def test_mean_svp(self):
        # Test based on example 3, p.69 of FAO paper
        mean_svp = pyeto.mean_svp(15, 24.5)
        self.assertAlmostEqual(mean_svp, 2.39, 2)

    def test_monthly_soil_heat_flux(self):
        # Test based on example 13, p.90 of FAO paper
        shf = pyeto.monthly_soil_heat_flux(14.1, 18.8)
        self.assertAlmostEqual(shf, 0.33, 2)

    def test_monthly_soil_heat_flux2(self):
        # Test based on approximate value expected from
        # example 13, p.90 of FAO paper
        shf = pyeto.monthly_soil_heat_flux2(14.1, 16.1)
        self.assertAlmostEqual(shf, 0.33, 1)

    def test_net_in_sol_rad(self):
        # Test based on example 12, p.87 of FAO paper
        # Note, there seems to be a rounding error in the answer given
        # in the FAO paper!
        rad = pyeto.net_in_sol_rad(14.5)
        self.assertAlmostEqual(rad, 11.1, 0)

    def test_net_out_lw_rad(self):
        # Test based on example 11, p.87 of FAO paper
        lwrad = pyeto.net_out_lw_rad(
            tmin=convert.celsius2kelvin(19.1),
            tmax=convert.celsius2kelvin(25.1),
            sol_rad=14.5,
            cs_rad=18.8,
            avp=2.1
        )
        self.assertAlmostEqual(lwrad, 3.5, 1)

    def test_net_rad(self):
        # Test based on example 16, p.99 of FAO paper
        net_rad = pyeto.net_rad(16.9, 3.0)
        self.assertAlmostEqual(net_rad, 13.9, 1)

    def test_psy_const(self):
        # Test based on example 2, p.63 of FAO paper
        psy = pyeto.psy_const(81.8)
        self.assertAlmostEqual(psy, 0.054, 3)

    def test_psy_const_of_psychrometer(self):
        # Test based on example 2, p.63 of FAO paper
        ea = 2.267 - pyeto.psy_const_of_psychrometer(
            1, 87.9) * (25.6 - 19.5)
        self.assertAlmostEqual(ea, 1.91, 2)

        self.assertEqual(
            pyeto.psy_const_of_psychrometer(1, 100), 100.0 * 0.000662)
        self.assertEqual(
            pyeto.psy_const_of_psychrometer(2, 100), 100.0 * 0.000800)
        self.assertEqual(
            pyeto.psy_const_of_psychrometer(3, 100), 100.0 * 0.001200)

        # Test bad pyschrometer
        with self.assertRaises(ValueError):
            pyeto.psy_const_of_psychrometer(0, 100)
        with self.assertRaises(ValueError):
            pyeto.psy_const_of_psychrometer(4, 100)

    def test_rh_from_avp_svp(self):
        rh = pyeto.rh_from_avp_svp(50, 100)
        self.assertAlmostEqual(rh, 50.0, 1)

    def test_sol_dec(self):
        # Test based on example 8, p.80 of FAO paper
        sol_dec = pyeto.sol_dec(246)
        self.assertAlmostEqual(sol_dec, 0.120, 3)

    def test_sol_rad_from_sun_hours(self):
        # Test based on example 10, p.84 of FAO paper
        solrad = pyeto.sol_rad_from_sun_hours(10.9, 7.1, 25.1)
        self.assertAlmostEqual(solrad, 14.45, 2)

    def test_sol_rad_from_t(self):
        # Test based on example 15, p.98 of FAO paper
        solrad = pyeto.sol_rad_from_t(40.6, 50.0, 14.8, 26.6, coastal=False)
        self.assertAlmostEqual(solrad, 22.3, 1)

        # Test that coastal param works
        solrad = pyeto.sol_rad_from_t(40.6, 50.0, 14.8, 26.6, coastal=True)
        # Multiply previous example by ratio of coastal to non-coastal
        # coefficient
        self.assertAlmostEqual(solrad, 22.3 * 0.19 / 0.16, 1)

        # Test that the clear sky radiation constraint is working:
        solrad = pyeto.sol_rad_from_t(
            40.6, 20.0, 14.8, 26.6, coastal=False)
        self.assertAlmostEqual(solrad, 20.0, 1)

    def test_sol_rad_island(self):
        # No example in FAO paper so have just done a visual check!
        solrad = pyeto.sol_rad_island(50.0)
        self.assertAlmostEqual(solrad, 31.0, 1)

    def test_sunset_hour_angle(self):
        # Test based on example 8, p.80 of FAO paper
        sha = pyeto.sunset_hour_angle(convert.deg2rad(-20), 0.120)
        self.assertAlmostEqual(sha, 1.527, 3)

    def test_wind_speed_2m(self):
        # Test based on example 14, p.92 of FAO paper
        ws = pyeto.wind_speed_2m(3.2, 10)
        self.assertAlmostEqual(ws, 2.4, 1)


if __name__ == '__main__':
    unittest.main()
