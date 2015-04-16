===
API
===

.. module:: pyeto

This part of the documentation shows the full API reference of all public
functions.

------------------
Evapotranspiration
------------------
.. autofunction:: fao56_penman_monteith
.. autofunction:: hargreaves
.. autofunction:: thornthwaite

--------------------
Atmospheric pressure
--------------------
.. autofunction:: atm_pressure

--------------
Daylight hours
--------------
.. autofunction:: daylight_hours
.. autofunction:: monthly_mean_daylight_hours

--------
Humidity
--------
Actual vapour pressure (ea)
---------------------------
.. autofunction:: avp_from_rhmax
.. autofunction:: avp_from_rhmean
.. autofunction:: avp_from_rhmin_rhmax
.. autofunction:: avp_from_tdew
.. autofunction:: avp_from_tmin
.. autofunction:: avp_from_twet_tdry

Saturated vapour pressure (es)
------------------------------
.. autofunction:: delta_svp
.. autofunction:: mean_svp
.. autofunction:: svp_from_t

Relative humidity (RH)
----------------------
.. autofunction:: rh_from_avp_svp

----------------------
Pyschrometric constant
----------------------
.. autofunction:: psy_const
.. autofunction:: psy_const_of_psychrometer

---------
Radiation
---------
.. autofunction:: cs_rad
.. autofunction:: et_rad
.. autofunction:: net_in_sol_rad
.. autofunction:: net_out_lw_rad
.. autofunction:: net_rad
.. autofunction:: sol_rad_from_sun_hours
.. autofunction:: sol_rad_from_t
.. autofunction:: sol_rad_island

--------------
Soil heat flux
--------------
.. autofunction:: monthly_soil_heat_flux
.. autofunction:: monthly_soil_heat_flux2

-----------------
Solar angles etc.
-----------------
.. autofunction:: inv_rel_dist_earth_sun
.. autofunction:: sol_dec
.. autofunction:: sunset_hour_angle

-----------
Temperature
-----------
.. autofunction:: daily_mean_t

----------
Wind speed
----------
.. autofunction:: wind_speed_2m

---------
Constants
---------
.. autodata:: pyeto.fao.SOLAR_CONSTANT
.. autodata:: pyeto.fao.STEFAN_BOLTZMANN_CONSTANT

---------------
Unit conversion
---------------
.. autofunction:: celsius2kelvin
.. autofunction:: deg2rad
.. autofunction:: energy2evap
.. autofunction:: kelvin2celsius
.. autofunction:: rad2deg
