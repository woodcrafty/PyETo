=============================
FAO-56 Penman-Monteith method
=============================
This is the method recommended by the Food and Agriculture Organisation of
the United Nations (FAO) for estimating (ET\ :sub:`o`\ ) for a short grass
crop using limited meteorological data (see Allen et al, 1998).

The FAO-56 Penman-Monteith equation requires site location, air temperature,
humidity, radiation and wind speed data for daily, weekly, ten-day or
monthly ET\ :sub:`o` calculations. It is important to verify the units of
all input data.*PyETo* provides functions to convert common units to the
standard unit (see the API of the ``pyeto.convert`` module).

The instructions given below are a brief summary of those given in Allen et al
(1998). It is recommended that you familiarise yourself with chapters 1 to 4
of Allen et al (1998) before proceeding.

-------------
Required data
-------------
The sections below describe each of the inputs required by the FAO-56
Penman-Monteith equation in ``fao.fao56_penman_monteith()``. If measured
meteorological data are not available, many of the variables can be
estimated using functions in the ``fao`` module::

    >>> from pyeto import fao

If a measured value is not available for a function's parameter, functions
for estimating that parameter are suggested in the function's documentation.

Note, that if monthly ET\ :sub:`o`\ is desired, the value of ET\ :sub:`o`\
calculated with mean monthly weather data is very similar to the average of
the daily ET\ :sub:`o`\  values calculated with average weather data for that
month.

Location
========
Altitude above sea level (m) and latitude (degrees north or south) of the
location should be specified. These data are needed to adjust some weather
parameters for the local average value of atmospheric pressure (a function
of the site elevation above mean sea level) and to compute extraterrestrial
radiation (Ra) and, in some cases, daylight hours (N). In the calculation
procedures for Ra and N, the latitude is expressed in radians (you can use
``pyeto.deg2rad()`` to convert degrees to radians).

Temperature
===========
The (average) daily maximum and minimum air temperatures in degrees Celsius
(°C) are required. Where only (average) mean daily temperatures are available,
the calculations can still be executed but some underestimation of ET\ :sub:`o`
will probably occur due to the non-linearity of the saturation vapour pressure
- temperature relationship.

Humidity (vapour pressure)
==========================
The (average) daily actual vapour pressure, ea, is required. If measured actual
vapour pressure is not available the following functions can be used to
estimate actual vapour pressure (in order of preference):

1. If dewpoint temperature data are available use ``fao.avp_from_tdew()``.
2. If dry and wet bulb temperatures are available from a psychrometer
   use ``fao.avp_from_twet_tdry()``.
3. If reliable minimum and maximum relative humidity data available use
   ``fao.avp_from_rhmin_rh_max()``.
4. If measurement errors of relative humidity are large then use only
   maximum relative humidity using ``fao.avp_from_rhmax()``
5. If minimum and maximum relative humidity are not available but mean
   relative humidity is available then use ``fao.avp_from_rhmean()`` (but this
   is less reliable than options 3 or 4).
6. If no data for the above are available then use ``fao.avp_from_tmin()``.
   This function is less reliable in arid areas where it is recommended that
   2 degrees Celsius is subtracted from the minimum temperature before it is
   passed to the function (following advice given in Annex 6 of Allen et al
   (1998).

Saturation vapour pressure (es) is required and can be estimated from air
temperature using ``fao.svp_from_t()``. The slope of the saturation vapour
pressure curve is also required and can be calculated using
``fao.svp_from_t()``.

Net radiation
=============
The (average) daily net radiation, Rn, is required. These data are not commonly
available but can be derived from the (average) shortwave radiation measured
with a pyranometer or from the (average) daily actual duration of bright
sunshine (hours per day) measured with a (Campbell-Stokes) sunshine recorder.

Alternatively, if measurements are not available, net radiation can be
estimated from net incoming solar (or shortwave) radiation and net
outgoing longwave radiation using ``fao.net_rad()``.

Net incoming solar radiation
----------------------------
Net solar (or shortwave) radiation is the amount of solar radiation that is
not reflected by the surface and can be calculated using
``fao.net_in_sol_rad()``.

Solar (shortwave) radiation
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The amount of incoming solar radiation (or shortwave radiation) reaching a
horizontal plane after scattering by the atmosphere. If measured values of
gross incoming solar radiation are not available the following functions (in
order of preference), can be used to estimate it:

1. If sunshine duration data are available use ``fao.sol_rad_from_sun_hours()``.
2. Otherwise use ``fao.sol_rad_from_t()`` which requires minimum and
   maximum temperature. Suitable for coastal or inland areas but not islands.
3. For island locations (<= 20 km wide), where no measured values are
   available from elsewhere on the island and the altitude is 0-100 m, use
   ``fao.sol_rad_island()``. Only suitable for monthly calculations.

Net outgoing longwave radiation
-------------------------------
Net outgoing longwave radiation is the net longwave energy leaving the earth's
surface. It is proportional to the absolute temperature of the surface raised
to the fourth power according to the Stefan-Boltzmann law. However, water
vapour, clouds, carbon dioxide and dust are absorbers and emitters of longwave
radiation. This function corrects the Stefan-Boltzmann law for humidity (using
actual vapor pressure) and cloudiness (using solar radiation and clear sky
radiation). Net outgoing longwave radiation can be estimated using
``fao.net_out_lw_rad()``.

Psychrometric constant
======================
The psychrometric constant is the ratio of specific heat of moist air at
constant pressure to latent heat of vaporization of water. It can be
estimated from atmospheric pressure using ``fao.psy_const()`` or
``fao.psy_const_of_psychrometer()``.

Soil heat flux
==============
For a daily time step soil heat flux is small compared to net radiation
when the soil is covered by vegetation, so it can be assumed to be zero
(Allen et al, 1998).

For a monthly time step soil heat flux is significant and should be estimated
using:

1. ``fao.monthly_soil_heat_flux()`` if temperature data for the previous and
   next month is available, or
2. ``fao.monthly_soil_heat_flux2()`` if temperature for the next month is not
   available.
