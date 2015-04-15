===================
Hargreaves equation
===================

The Hargreaves equation (Hargreaves and Samani, 1985) is a simple
evapotranspiration model that only requires a few easily accessible parameters:
mininimum, maximum and mean temperature, and extraterrestrial radiation.

The Hargreaves method is recommended by the FAO (Allen et al, 1998) as an
alternative method for estimating ETo if insufficient meteorological data are
available for the Penman-Monteith method. However, the FAO suggest that using
the Penman-Monteith method with estimated solar radiation, vapor pressure
and wind speed generally provides more accurate estimates than the Hargreaves
equation. This is due to the ability of the estimation equations to
incorporate general climatic characteristics such as high or low wind speed
or high or low relative humidity into the ET\ :sub:`o` estimate made using the
FAO Penman-Monteith method.

The Hargreaves equation has a tendency to under-estimate ET\ :sub:`o`\
under high wind conditions(u2 > 3m/s) and to over-estimate under conditions of
high relative humidity.

The following example uses the Hargreaves model to estimate monthly PET for the
1st of February, 2014, for Aberdeen, Scotland (latitude 57.1526 degrees N).

First, convert latitude to radians and the date to day of the year (Julian
day)::

    >>> import datetime, pyeto
    >>> lat = pyeto.deg2rad(57.1526)  # Convert latitude to radians
    >>> day_of_year = datetime.date(2014, 2, 1).timetuple().tm_yday

To estimate extraterrestrial radiation we first need to calculate
solar declination, sunset hour angle and inverse relative distance Earth-Sun::

    >>> sol_dec = pyeto.sol_dec(day_of_year)            # Solar declination
    >>> sha = pyeto.sunset_hour_angle(lat, sol_dec)
    >>> ird = pyeto.inv_rel_dist_earth_sun(day_of_year)
    >>> et_rad = pyeto.et_rad(lat, sol_dec, sha, ird)   # Extraterrestrial radiation

Finally, we can estimate ET\ :sub:`o`\ , assuming a minimum temperature of
1.3, maximum temperature of 5.6 and mean temperature of 3.8::

    >>> hargreaves(1.3, 5.6, 3.8, et_rad)

