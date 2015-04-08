==========================
FAO Penman-Monteith method
==========================
These instructions are a brief summary of those given in Allen et al (1998).
It is recommended that you familiarise yourself with chapters 1 to 4 of
Allen et al (1998) before proceeding.

The data required to calculate the daily, ten-day or monthly
evapotranspiration over grass using the FAO Penman-Monteith equation are
specified below. If measured meteorological data are not available, many of
the variables can be estimated using functions in the library.

------------------------------
Monthly (or ten-day) time step
------------------------------
The value of ETo calculated with mean monthly weather data is very similar to
the average of the daily ETo values calculated with average weather data for
that month. The following data are required (if using a ten-day period
substitute the words 'ten-day' in place of 'monthly'):

* monthly average daily minimum and maximum temperature
* monthly average of actual vapour pressure derived from psychrometric,
  dewpoint or relative humidity data.
* monthly average of daily wind speed data measured at 2 m height (can be
  estimated from measurements made at different heights)
* monthly average of daily net radiation computed from monthly measured short-
  wave radiation or from actual duration of daily sunshine hours. The
  extraterrestrial radiation and daylight hours for a specific day of the
  month can be computed using functions in this module.
* soil heat flux for monthly periods can be significant when soil is warming in
  spring or cooling in autumn so its value should be determined from the
  mean monthly air temperatures of the previous and next month (see
  monthly_soil_heat_flux().

---------------
Daily time step
---------------
For daily ETo estimates the required meteorological data are:

* minimum and maximum daily air temperature
* mean daily actual vapour pressure derived from psychrometric, dewpoint
  temperature or relative humidity data (or even just minimum temperature)
* daily average wind speed measured at 2 m height (can be estimated from
  measurements made at different heights)
* net radiation measured or computed from solar (shortwave) and longwave
  radiation or from the actual duration of sunshine. The extraterrestrial
  radiation for a specific day of the month should be computed using
  the et_rad() and daylight_hours() functions.
* as the magnitude of daily soil heat flux beneath a reference grass crop
  is relatively small it may ignored (soil heat flux = 0) for daily time
  steps though if you wish you can calculate it using the
  daily soil_heat_flux() function.

To calculate ETo using ``fao_penman_monteith()`` gather the data
necessary for the function's arguments. It is best to provide measured
values for the inputs if possible, but if some of the data is not
available then use one of the 'missing-data' functions to estimate the input.

-----------------------------
Estimating missing input data
-----------------------------
For some input variables there is an order of preference for which function
to use to estimate missing values due to variation in the
robustness/generality of the different methods. For example, if you wish to
calculate daily net radiation you can estimate it from measured sunshine
hours (intermediate option) or from the minimum temperature (worst option).

Below is a list of variables for which multiple 'missing-data' functions exist,
along with the order of preference for their use:

Actual vapour pressure (AVP)
============================
If measured values are not available then use the following functions
to estimate AVP (in order of preference):

1. If dewpoint temperature data are available use ``ea_from_tdew()``
2. If dry and wet bulb temperatures are available from a psychrometer
   use ``ea_from_twet_tdry()``
3. If reliable min and max relative humidity data available use
   ``ea_from_rhmin_rh_max()``
4. If measurement errors of RH are large then use only RH max using
   ``ea_from_rhmax()``
5. If RH min and RH max are not available but RH mean is then use
   ``ea_from_rhmean()`` (but this is less reliable than options 3 or 4)
6. If no data for the above are available then use ``ea_from_tmin()``.
   This function is less reliable in arid areas where it is recommended that
   2 deg C is subtracted from Tmin before it is passed to the function
   following Annex 6 of the FAO paper.

Soil heat flux
==============
For a daily time step soil heat flux is small compared to net radiation
when the soil is covered by vegetation, so it can be assumed to be zero.
However, if you prefer, daily soil heat flux can be estimated using
``daily_soil_heat_flux()``.

For a monthly time step soil heat flux is significant and should be estimated
using:

1. ``monthly_soil_heat_flux()`` if temperature data for the previous and
   next month is available or
2. ``monthly_soil_heat_flux2()`` if temperature for the next month is not
   available.

Solar (shortwave) radiation
===========================
The amount of incoming solar radiation (AKA shortwave radiation) reaching a
horizontal plane after scattering by the atmosphere.
If measured values of gross solar radiation are not available the following
methods are available (in order of preference) to estimate it:

1. If sunshine duration data are available use ``sol_rad_from_sun_hours()``
2. Otherwise use ``sol_rad_from_t()`` which requires T min and T max data.
   Suitable for coastal or inland areas but not islands.
3. For island locations (island <= 20 km wide) where no measured values
   are available from elsewhere on the island and the altitude is 0-100 m use
   ``sol_rad_island()``. Only suitable for monthly calculations.

Net solar (shortwave) radiation
===============================
The amount of solar radiation (sometimes referred to as shortwave radiation)
that is not reflected by the surface. The methods listed below assume an
albedo of 0.23 for a grass reference crop. Use ``net_rad()`` to estimate net
solar radiation for a grass crop.

List of FAO functions
=====================
Below is a list of function based on equations from the FAO paper by Allen
et al (1998):

ETo/PET
-------
* fao_penman_monteith()
* hargreaves()
* thornthwaite()

Atmospheric pressure (P)
------------------------
* atmospheric_pressure()

Actual vapour pressure (ea)
---------------------------
* ea_from_tmin()
* ea_from_rhmin_rhmax()
* ea_from_rhmax()
* ea_from_rhmean()
* ea_from_tdew()
*ea_from_twet_tdry()

Pyschrometric constant
----------------------
* psychrometric_const()
* psychrometric_const_of_psychrometer()

Radiation
---------
* clear_sky_radiation()
* daylight_hours()
* energy2equiv_evaporation()
* net_incoming_solar_radiation()
* net_outgoing_longwave_radiation()
* net_radiation()
* solar_radiation_from_sun_hours()
* solar_radiation_from_t()
* solar_radiation_island()

Relative humidity (RH)
----------------------
* rh_from_ea_es()

Saturated vapour pressure (es)
------------------------------
* delta_sat_vap_pressure()
* es_from_t()
* mean_es()

Soil heat flux
--------------
* daily_soil_heat_flux()
* monthly_soil_heat_flux()
* monthly_soil_heat_flux2()

Solar angles etc
----------------
* inv_rel_dist_earth_sun()
* solar_declination()
* sunset_hour_angle()

Temperature
-----------
* daily_mean_t()

Wind speed
----------
* wind_speed_2m()
