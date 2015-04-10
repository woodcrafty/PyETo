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

    def test_atmospheric_pressure(self):
        # Test based on example 2, p.63 of FAO paper
        P = pyeto.atmospheric_pressure(1800)
        self.assertAlmostEqual(P, 81.8, 1)

    def test_ea_from_tmin(self):
        # Test based on example 20, p.121 of FAO paper
        ea = pyeto.ea_from_tmin(14.8)
        self.assertAlmostEqual(ea, 1.68, 2)

    def test_ea_from_rhmin_rhmax(self):
        # Test based on example 5, p.72 of FAO paper
        ea = pyeto.ea_from_rhmin_rhmax(2.064, 3.168, 54, 82)
        self.assertAlmostEqual(ea, 1.70, 2)

    def test_ea_from_rhmax(self):
        ea = pyeto.ea_from_rhmax(2.064, 82)
        self.assertAlmostEqual(ea, 1.69, 2)

    def test_ea_from_rhmean(self):
        # Test based on FAO example 5
        ea = pyeto.ea_from_rhmean(2.064, 3.168, (82+54)/2.0)
        self.assertAlmostEqual(ea, 1.78, 2)

    def test_ea_from_tdew(self):
        # Test based on example 20, p.121 of FAO paper
        ea = pyeto.ea_from_tdew(14.8)
        self.assertAlmostEqual(ea, 1.68, 2)

    def test_ea_from_twet_tdry(self):
        # Test based on example 4, p.70 of FAO paper
        ea = pyeto.ea_from_twet_tdry(19.5, 25.6, 2.267, 0.000662*87.9)
        self.assertAlmostEqual(ea, 1.91, 2)

    def test_clear_sky_radiation(self):
        # Test based on example 18, p.115 of FAO paper
        csr = pyeto.clear_sky_radiation(100, 41.09)
        self.assertAlmostEqual(csr, 30.90, 2)

    def test_daily_mean_t(self):
        tmean = pyeto.daily_mean_t(10, 20)
        self.assertEqual(tmean, 15.0)

    def test_daily_soil_heat_flux(self):
        # Have not found data to test against yet
        #shf = pyeto.daily_soil_heat_flux(t_cur, t_prev, delta_t, soil_heat_cap=2.1, delta_z=0.10)
        pass

    def test_daylight_hours(self):
        # Test based on example 9, p.83 of FAO paper
        dh = pyeto.daylight_hours(1.527)
        self.assertAlmostEqual(dh, 11.7, 1)

    def test_delta_sat_vap_pressure(self):
        # Test based on example 17, p.111 of FAO paper
        dh = pyeto.delta_sat_vap_pressure(30.2)
        self.assertAlmostEqual(dh, 0.246, 3)

    def test_extraterrestrial_radiation(self):
        # Test based on example 8, p.80 of FAO paper
        etrad = pyeto.extraterrestrial_radiation(
            convert.degrees2radians(-20), 0.120, 1.527, 0.985)
        self.assertAlmostEqual(etrad, 32.2, 1)

    def test_fao_penman_monteith(self):
        # Test based on example 17, p.110 (monthly calc) and
        # example 18, p.113 (daily calc) of FAO paper

        # Monthly ETo:
        # Note, due to rounding errors in the FAO's example we can only
        # test to 1 decimal place here!
        eto = pyeto.fao_penman_monteith(
            Rn=14.33,
            t=convert.celsius2kelvin(30.2),
            ws=2.0,
            es=4.42,
            ea=2.85,
            delta_es=0.246,
            psy=0.0674,
            shf=0.14,
        )
        self.assertAlmostEqual(eto, 5.72, 1)

        # Daily ETo:
        # (Rn, t, ws, es, ea, delta_es, psy, shf=0.0)
        eto = pyeto.fao_penman_monteith(
            Rn=13.28,
            t=convert.celsius2kelvin(16.9),
            ws=2.078,
            es=1.997,
            ea=1.409,
            delta_es=0.122,
            psy=0.0666
        )
        self.assertAlmostEqual(eto, 3.9, 1)

    def test_hargreaves(self):
        # Have not yet found data to test against
        #eto = pyeto.hargreaves(tmin, tmax, tmean, Ra)
        #self.assertAlmostEqual(eto, 32.2, 1)
        pass

    def test_inv_rel_dist_earth_sun(self):
        # Test based on example 8, p.80 of FAO paper
        irl = pyeto.inv_rel_dist_earth_sun(246)
        self.assertAlmostEqual(irl, 0.985, 3)

    def test_mean_es(self):
        # Test based on example 3, p.69 of FAO paper
        mean_es = pyeto.mean_es(15, 24.5)
        self.assertAlmostEqual(mean_es, 2.39, 2)

    def test_monthly_soil_heat_flux(self):
        # Test based on example 13, p.90 of FAO paper
        shf = pyeto.monthly_soil_heat_flux(14.1, 18.8)
        self.assertAlmostEqual(shf, 0.33, 2)

    def test_monthly_soil_heat_flux2(self):
        # Test based on approximate value expected from
        # example 13, p.90 of FAO paper
        shf = pyeto.monthly_soil_heat_flux2(14.1, 16.1)
        self.assertAlmostEqual(shf, 0.33, 1)

    def test_net_radiation(self):
        # Test based on example 16, p.99 of FAO paper
        net_rad = pyeto.net_radiation(16.9, 3.0)
        self.assertAlmostEqual(net_rad, 13.9, 1)

    def test_net_incoming_solar_radiation(self):
        # Test based on example 12, p.87 of FAO paper
        # Note, there seems to be a rounding error in the answer given
        # in the FAO paper!
        rad = pyeto.net_incoming_solar_radiation(14.5)
        self.assertAlmostEqual(rad, 11.1, 0)

    def test_net_outgoing_longwave_radiation(self):
        # Test based on example 11, p.87 of FAO paper
        lwrad = pyeto.net_outgoing_longwave_radiation(
            tmin=convert.celsius2kelvin(19.1),
            tmax=convert.celsius2kelvin(25.1),
            sol_rad=14.5,
            clear_sky_rad=18.8,
            ea=2.1
        )
        self.assertAlmostEqual(lwrad, 3.5, 1)

    def test_psychrometric_const(self):
        # Test based on example 2, p.63 of FAO paper
        psy = pyeto.psychrometric_const(81.8)
        self.assertAlmostEqual(psy, 0.054, 3)

    def test_psychrometric_const_of_psychrometer(self):
        # Test based on example 2, p.63 of FAO paper
        ea = 2.267 - pyeto.psychrometric_const_of_psychrometer(
            1, 87.9) * (25.6 - 19.5)
        self.assertAlmostEqual(ea, 1.91, 2)

    def test_energy2equiv_evaporation(self):
        # Test based on example 13, p.90 of FAO paper
        evap = pyeto.energy2equiv_evaporation(0.33)
        self.assertAlmostEqual(evap, 0.13, 2)

    def test_rh_from_ea_es(self):
        rh = pyeto.rh_from_ea_es(50, 100)
        self.assertAlmostEqual(rh, 50.0, 1)

    def test_solar_declination(self):
        # Test based on example 8, p.80 of FAO paper
        sol_dec = pyeto.solar_declination(246)
        self.assertAlmostEqual(sol_dec, 0.120, 3)

    def test_solar_radiation_from_sun_hours(self):
        # Test based on example 10, p.84 of FAO paper
        solrad = pyeto.solar_radiation_from_sun_hours(10.9, 7.1, 25.1)
        self.assertAlmostEqual(solrad, 14.45, 2)

    def test_solar_radiation_from_t(self):
        # Test based on example 15, p.98 of FAO paper
        solrad = pyeto.solar_radiation_from_t(
            40.6, 50.0, 14.8, 26.6, coastal=False)
        self.assertAlmostEqual(solrad, 22.3, 1)

        # Test that the clear sky radiation constraint is working:
        solrad = pyeto.solar_radiation_from_t(
            40.6, 20.0, 14.8, 26.6, coastal=False)
        self.assertAlmostEqual(solrad, 20.0, 1)

    def test_solar_radiation_island(self):
        # No example in FAO paper so have just done a visual check!
        solrad = pyeto.solar_radiation_island(50.0)
        self.assertAlmostEqual(solrad, 31.0, 1)

    def test_sunset_hour_angle(self):
        # Test based on example 8, p.80 of FAO paper
        sha = pyeto.sunset_hour_angle(convert.degrees2radians(-20), 0.120)
        self.assertAlmostEqual(sha, 1.527, 3)

    def test_wind_speed_2m(self):
        # Test based on example 14, p.92 of FAO paper
        ws = pyeto.wind_speed_2m(3.2, 10)
        self.assertAlmostEqual(ws, 2.4, 1)


if __name__ == '__main__':
    unittest.main()
