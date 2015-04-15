===
API
===

.. module:: pyeto

This part of the documentation shows the full API reference of all public
functions.

-------------------------------------
FAO-56 Penman-Monteith and Hargreaves
-------------------------------------
Functions and constants described in the FAO-56 paper (Allen et al, 1998).

.. autofunction:: atm_pressure

.. autofunction:: avp_from_tmin

.. autofunction:: avp_from_rhmin_rhmax

.. autofunction:: avp_from_rhmax

.. autofunction:: avp_from_rhmean

.. autofunction:: avp_from_tdew

.. autofunction:: avp_from_twet_tdry

.. autofunction:: cs_rad

.. autofunction:: daily_mean_t

.. autofunction:: daylight_hours

.. autofunction:: delta_svp

.. autofunction:: energy2evap

.. autofunction:: et_rad

.. autofunction:: fao56_penman_monteith

.. autofunction:: hargreaves

.. autofunction:: inv_rel_dist_earth_sun

.. autofunction:: mean_svp

.. autofunction:: monthly_soil_heat_flux

.. autofunction:: monthly_soil_heat_flux2

.. autofunction:: net_in_sol_rad

.. autofunction:: net_out_lw_rad

.. autofunction:: net_rad

.. autofunction:: psy_const

.. autofunction:: psy_const_of_psychrometer

.. autofunction:: rh_from_avp_svp

.. autodata:: pyeto.fao.SOLAR_CONSTANT

.. autofunction:: sol_dec

.. autofunction:: sol_rad_from_sun_hours

.. autofunction:: sol_rad_from_t

.. autofunction:: sol_rad_island

.. autodata:: pyeto.fao.STEFAN_BOLTZMANN_CONSTANT

.. autofunction:: sunset_hour_angle

.. autofunction:: svp_from_t

.. autofunction:: wind_speed_2m

------------
Thornthwaite
------------
Functions related to the Thornthwaite (1948) method.

.. autofunction:: monthly_mean_daylight_hours

.. autofunction:: thornthwaite

---------------
Unit conversion
---------------
Functions for converting common units.

.. autofunction:: celsius2kelvin
.. autofunction:: deg2rad
.. autofunction:: kelvin2celsius
.. autofunction:: rad2deg
