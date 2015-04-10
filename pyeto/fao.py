"""
Library of functions for estimating reference evapotransporation (ETo) for
a grass reference crop using the FAO Penman-Monteith and Hargreaves
equations. The library includes numerous functions for estimating missing
meteorological data.

:copyright: (c) 2015 by Mark Richards.
:license: BSD 3-Clause, see LICENSE.txt for more details.
"""

__license__ = 'BSD 3-clause'
__version__ = '0.1.0'
__author__ = 'Mark Richards'
__email__ = 'mark.l.a.richardsREMOVETHIS@gmail.com'

import math

from ._check import (
    check_day_hours,
    check_doy,
    check_latitude_rad,
    check_sol_dec_rad,
)

# Public constants
SOLAR_CONSTANT = 0.0820    # Solar constant [MJ m-2 min-1]
# Stefan-Boltzmann constant [MJ K-4 m-2 day-1]
STEFAN_BOLTZMANN_CONSTANT = 0.000000004903


def atm_pressure(altitude):
    """
    Estimate atmospheric pressure from altitude.

    This function uses equation (7), page 62 in Allen et al (1998). Calculated
    using a simplification of the ideal gas law, assuming 20 deg C for a
    standard atmosphere.

    :param altitude: Elevation/altitude above sea level [m]
    :return: atmospheric pressure [kPa]
    :rtype: float
    """
    tmp = (293.0 - (0.0065 * altitude)) / 293.0
    return math.pow(tmp, 5.26) * 101.3


def clear_sky_rad(altitude, et_rad):
    """
    Estimate clear sky radiation from altitude and extraterrestrial radiation.

    Based on equation 37 in Allen et al (1998) which is recommended when
    calibrated Angstrom values are not available.

    :param altitude: Elevation above sea level [m]
    :param et_rad: Extraterrestrial radiation [MJ m-2 day-1]
    :return: Clear sky radiation [MJ m-2 day-1]
    :rtype: float
    """
    return (0.00002 * altitude + 0.75) * et_rad


def daily_mean_t(tmin, tmax):
    """
    Estimate mean daily temperature from the daily minimum and maximum
    temperatures.

    :param tmin: Minimum daily temperature [deg C]
    :param tmax: Maximum daily temperature [deg C]
    :return: Mean daily temperature [deg C]
    :rtype: float
    """
    return (tmax + tmin) / 2.0


def daylight_hours(sha):
    """
    Calculate daylight hours from sunset hour angle.

    Based on FAO equation 34 in Allen et al (1998).

    :param sha: Sunset hour angle [rad].
    :return: Daylight hours.
    :rtype: float
    """
    # TODO: Put in validation of sunset hour angle?
    return (24.0 / math.pi) * sha


def delta_sat_vap_pressure(t):
    """
    Estimate the slope of the saturation vapour pressure curve at a given
    temperature.

    Based on equation 13 in Allen et al (1998). If using in the Penman-Monteith
    *t* should be the mean air temperature.

    :param t: Air temperature [deg C]. Use mean air temperature for use in
        Penman-Monteith.
    :return: Saturation vapour pressure [kPa degC-1]
    :rtype: float
    """
    tmp = 4098 * (0.6108 * math.exp((17.27 * t) / (t + 237.3)))
    return tmp / math.pow((t + 237.3), 2)


def ea_from_tmin(tmin):
    """
    Estimate actual vapour pressure (ea) from minimum temperature.

    Based on equation 48 in in Allen et al (1998). This method is to be used
    where humidity data are lacking or are of questionable quality. The method
    assumes that the dewpoint temperature is approximately equal to the
    minimum temperature (*tmin*), i.e. the air is saturated with water
    vapour at *tmin*.

    NOTE: This assumption may not hold in arid/semi-arid areas.
    In these areas it may be better to subtract 2 deg C from the
    minimum temperature (see Annex 6 in FAO paper).

    :param tmin: Daily minimum temperature [deg C]
    :return: Actual vapour pressure [kPa]
    :rtype: float
    """
    return 0.611 * math.exp((17.27 * tmin) / (tmin + 237.3))


def ea_from_rhmin_rhmax(e_tmin, e_tmax, rh_min, rh_max):
    """
    Estimate actual vapour pressure (ea) from saturation vapour pressure and
    relative humidity.

    Based on FAO equation 17 in Allen et al (1998).

    :param e_tmin: Saturation vapour pressure at daily minimum temperature [kPa]
    :param e_tmax: Saturation vapour pressure at daily maximum temperature [kPa]
    :param rh_min: Minimum relative humidity [%]
    :param rh_max: Maximum relative humidity [%]
    :return: Actual vapour pressure [kPa]
    :rtype: float
    """
    tmp1 = e_tmin * (rh_max / 100.0)
    tmp2 = e_tmax * (rh_min / 100.0)
    return (tmp1 + tmp2) / 2.0


def ea_from_rhmax(e_tmin, rh_max):
    """
    Estimate actual vapour pressure (ea) from saturation vapour pressure at
    daily minimum temperature and maximum relative humidity

    Based on FAO equation 18 in Allen et al (1998).

    :param e_tmin: Saturation vapour pressure at daily minimum temperature [kPa]
    :param rh_max: Maximum relative humidity [%]
    :return: Actual vapour pressure [kPa]
    :rtype: float
    """
    return e_tmin * (rh_max / 100.0)


def ea_from_rhmean(e_tmin, e_tmax, rh_mean):
    """
    Estimate actual vapour pressure (ea) from saturation vapour pressure at daily
    minimum and maximum temperature, and mean relative humidity.

    Based on FAO equation 19 in Allen et al (1998).

    :param e_tmin: Saturation vapour pressure at daily minimum temperature [kPa]
    :param e_tmax: Saturation vapour pressure at daily maximum temperature [kPa]
    :param rh_mean: Mean relative humidity [%] (average of RH min and RH max)
    :return: Actual vapour pressure [kPa]
    :rtype: float
    """
    return (rh_mean / 100.0) * ((e_tmax + e_tmin) / 2.0)


def ea_from_tdew(tdew):
    """
    Estimate actual vapour pressure (ea) from dewpoint temperature.

    Based on equation 14 in Allen et al (1998). As the dewpoint temperature is
    the temperature to which air needs to be cooled to make it saturated, the
    actual vapour pressure is the saturation vapour pressure at the dewpoint
    temperature.

    This method is preferable to calculating vapour pressure from
    minimum temperature.

    :param tdew: Dewpoint temperature [deg C]
    :return: Actual vapour pressure [kPa]
    :rtype: float
    """
    return 0.6108 * math.exp((17.27 * tdew) / (tdew + 237.3))


def ea_from_twet_tdry(twet, tdry, e_twet, psy_const):
    """
    Estimate actual vapour pressure (ea) from wet and dry bulb temperature.

    Based on equation 15 in Allen et al (1998). As the dewpoint temperature
    is the temperature to which air needs to be cooled to make it saturated, the
    actual vapour pressure is the saturation vapour pressure at the dewpoint
    temperature.

    This method is preferable to calculating vapour pressure from
    minimum temperature.

    Values for the psychrometric constant of the psychrometer (*psy_const*)
    can be calculated using ``psyc_const_of_psychrometer()``.

    :param twet: Wet bulb temperature [deg C]
    :param tdry: Dry bulb temperature [deg C]
    :param e_twet: Saturated vapour pressure at the wet bulb temperature [kPa]
    :param psy_const: Psychrometric constant of the pyschrometer [kPa deg C-1]
    :return: Actual vapour pressure [kPa]
    :rtype: float
    """
    return e_twet - (psy_const * (tdry - twet))


def energy2evap(energy):
    """
    Convert energy (e.g. radiation energy) in MJ m-2 day-1 to the equivalent
    evaporation, assuming a grass reference crop.

    Energy is converted to equivalent evaporation using a conversion
    factor equal to the inverse of the latent heat of vapourisation
    (1 / lambda = 0.408).

    Based on FAO equation 20 in Allen et al (1998).

    :param energy: Energy e.g. radiation or heat flux [MJ m-2 day-1].
    :return: Equivalent evaporation [mm day-1].
    :rtype: float
    """
    return 0.408 * energy


def es_from_t(t):
    """
    Estimate saturation vapour pressure (es) from air temperature.

    Based on equations 11 and 12 in Allen et al (1998).

    :param t: Temperature [deg C]
    :return: Saturation vapour pressure [kPa]
    :rtype: float
    """
    return 0.6108 * math.exp((17.27 * t) / (t + 237.3))


def et_rad(latitude, sd, sha, irl):
    """
    Estimate daily extraterrestrial radiation (Ra, 'top of the atmosphere
    radiation').

    Based on equation 21 in Allen et al (1998). If monthly mean radiation is
    required make sure *sd*. *sha* and *irl* have been calculated using the day
    of the year that corresponds to the middle of the month.

    **Note**: From Allen et al (1998) "For the winter months in latitudes
    greater than 55 degrees (N or S), the equations have limited validity.
    Reference should be made to the Smithsonian Tables to assess possible
    deviations."

    :param latitude: Latitude [radians]
    :param sd: Solar declination [radians]
    :param sha: Sunset hour angle [radians]
    :param irl: Inverse relative distance earth-sun [dimensionless]
    :return: Daily extraterrestrial radiation [MJ m-2 day-1]
    :rtype: float
    """
    # TODO: raise exceptions for sd and sha?
    check_latitude_rad(latitude)
    check_sol_dec_rad(latitude)

    # Calculate daily extraterrestrial radiation based on FAO equation 21
    tmp1 = (24.0 * 60.0) / math.pi
    tmp2 = sha * math.sin(latitude) * math.sin(sd)
    tmp3 = math.cos(latitude) * math.cos(sd) * math.sin(sha)
    return tmp1 * SOLAR_CONSTANT * irl * (tmp2 + tmp3)


def fao56_penman_monteith(Rn, t, ws, es, ea, delta_es, psy, shf=0.0):
    """
    Estimate reference evapotranspiration (ETo) from a hypothetical
    grass reference surface using t he FAO-56 Penman-Monteith equation.

    Based on equation 6 in Allen et al (1998).

    :param Rn: Net radiation at crop surface [MJ m-2 day-1].
    :param t: Air temperature at 2 m height [deg Kelvin].
    :param ws: Wind speed at 2 m height [m s-1]. If not measured at 2m,
        convert using ``wind_speed_at_2m()``.
    :param es: Saturation vapour pressure [kPa].
    :param ea: Actual vapour pressure [kPa].
    :param delta_es: Slope of vapour pressure curve [kPa  deg C].
    :param psy: Psychrometric constant [kPa deg C].
    :param shf: Soil heat flux (G) [MJ m-2 day-1] (default = 0, fine for daily
        time step).
    :return: Reference evapotranspiration (ETo) from a hypothetical
        grass reference surface [mm day-1].
    :rtype: float
    """
    a1 = 0.408 * (Rn - shf) * delta_es / (delta_es + (psy * (1 + 0.34 * ws)))
    a2 = 900 * ws / t * (es - ea) * psy / (delta_es + (psy * (1 + 0.34 * ws)))
    return a1 + a2


def hargreaves(tmin, tmax, tmean, Ra):
    """
    Estimate reference evapotranspiration over grass (ETo) using the Hargreaves
    equation.

    Generally, when solar radiation data, relative humidity data
    and/or wind speed data are missing, it is better to estimate them using
    the functions available in this module, and then calculate ETo
    the FAO Penman-Monteith equation. However, as an alternative, ETo can be
    estimated using the Hargreaves ETo equation.

    Based on equation 52 in Allen et al (1998).

    :param tmin: Minimum daily temperature [deg C]
    :param tmax: Maximum daily temperature [deg C]
    :param tmean: Mean daily temperature [deg C]
    :param Ra: Extraterrestrial radiation (Ra) [MJ m-2 day-1]
    :return: Reference evapotranspiration over grass (ETo) [mm day-1]
    :rtype: float
    """
    # Note, multiplied by 0.408 to convert extraterrestrial radiation could
    # be given in MJ m-2 day-1 rather than as equivalent evaporation in
    # mm day-1
    return 0.0023 * (tmean + 17.8) * (tmax - tmin) ** 0.5 * 0.408 * Ra


def inv_rel_dist_earth_sun(doy):
    """
    Calculate the inverse relative distance between earth and sun from
    day of the year.

    Based on FAO equation 23 in Allen et al (1998).

    :param doy: Day of year [1 to 366]
    :return: Inverse relative distance between earth and the sun
    :rtype: float
    """
    check_doy(doy)

    return 1 + (0.033 * math.cos((2.0 * math.pi / 365.0) * doy))


def mean_es(tmin, tmax):
    """
    Estimate mean saturation vapour pressure es [kPa] from minimum and
    maximum temperature.

    Based on equations 11 and 12 in Allen et al (1998).

    Mean saturation vapour pressure is calculated as the mean of the
    saturation vapour pressure at tmax (maximum temperature) and tmin
    (minimum temperature).

    :param tmin: Minimum temperature [deg C]
    :param tmax: Maximum temperature [deg C]
    :return: Mean saturation vapour pressure (es) [kPa]
    :rtype: float
    """
    return (es_from_t(tmin) + es_from_t(tmax)) / 2.0


def monthly_soil_heat_flux(t_month_prev, t_month_next):
    """
    Estimate monthly soil heat flux (Gmonth) from the mean air temperature of
    the previous and next month, assuming a grass crop.

    Based on equation 43 in Allen et al (1998). If the air temperature of the
    next month is not known use ``monthly_soil_heat_flux2()`` instead. The
    resulting heat flux can be converted to equivalent evaporation [mm day-1]
    using ``energy2evap()``.

    :param t_month_prev: Mean air temperature of the previous month
        [deg Celsius]
    :param t_month2_next: Mean air temperature of the next month [deg Celsius]
    :return: Monthly soil heat flux (Gmonth) [MJ m-2 day-1]
    :rtype: float
    """
    return 0.07 * (t_month_next - t_month_prev)


def monthly_soil_heat_flux2(t_month_prev, t_month_cur):
    """
    Estimate monthly soil heat flux (Gmonth) [MJ m-2 day-1] from the mean
    air temperature of the previous and current month, assuming a grass crop.

    Based on equation 44 in Allen et al (1998). If the air temperature of the
    next month is available, use ``monthly_soil_heat_flux()`` instead. The
    resulting heat flux can be converted to equivalent evaporation [mm day-1]
    using ``energy2evap()``.

    Arguments:
    :param t_month_prev: Mean air temperature of the previous month
        [deg Celsius]
    :param t_month_cur: Mean air temperature of the current month [deg Celsius]
    :return: Monthly soil heat flux (Gmonth) [MJ m-2 day-1]
    :rtype: float
    """
    return 0.14 * (t_month_cur - t_month_prev)


def net_in_sol_rad(sol_rad, albedo=0.23):
    """
    Calculate net incoming solar (or shortwave) radiation from gross
    incoming solar radiation, assuming a grass reference crop.

    Net incoming solar radiation is the net shortwave radiation resulting
    from the balance between incoming and reflected solar radiation. The
    output can be converted to equivalent evaporation [mm day-1] using
    ``energy2evap()``.

    Based on FAO equation 38 in Allen et al (1998).

    :param sol_rad: Gross incoming solar radiation [MJ m-2 day-1].
    :param albedo: Albedo of the crop [dimensionless]. Default is 0.23,
        which is the value used by the FAO for a grass reference crop.
    :return: Net incoming solar (or shortwave) radiation [MJ m-2 day-1].
    :rtype: float
    """
    return (1 - albedo) * sol_rad


def net_out_lw_rad(tmin, tmax, sol_rad, clear_sky_rad, ea):
    """
    Estimate net outgoing longwave radiation.

    This is the net longwave energy (net energy flux) leaving the
    earth's surface. It is proportional to the absolute temperature of
    the surface raised to the fourth power according to the Stefan-Boltzmann
    law. However, water vapour, clouds, carbon dioxide and dust are absorbers
    and emitters of longwave radiation. This function corrects the Stefan-
    Boltzmann law for humidity (using actual vapor pressure) and cloudiness
    (using solar radiation and clear sky radiation). The concentrations of all
    other absorbers are assumed to be constant.

    The output can be converted to equivalent evaporation [mm day-1] using
    ``energy2evap()``.

    Based on FAO equation 39 in Allen et al (1998).

    :param tmin: Absolute daily minimum temperature [degrees Kelvin]
    :param tmax: Absolute daily maximum temperature [degrees Kelvin]
    :param sol_rad: Solar radiation [MJ m-2 day-1]
    :param clear_sky_rad: Clear sky radiation [MJ m-2 day-1]
    :param ea: Actual vapour pressure [kPa]
    :return: Net outgoing longwave radiation [MJ m-2 day-1]
    :rtype: float
    """
    tmp1 = (STEFAN_BOLTZMANN_CONSTANT *
        ((math.pow(tmax, 4) + math.pow(tmin, 4)) / 2))
    tmp2 = 0.34 - (0.14 * math.sqrt(ea))
    tmp3 = 1.35 * (sol_rad / clear_sky_rad) - 0.35
    return tmp1 * tmp2 * tmp3


def net_rad(ni_sw_rad, no_lw_rad):
    """
    Calculate daily net radiation at the crop surface, assuming a grass
    reference crop.

    Net radiation is the difference between the incoming net shortwave (or
    solar) radiation and the outgoing net longwave radiation. Output can be
    converted to equivalent evaporation [mm day-1] using
    ``energy2evap()``.

    Based on FAO equation 40 in Allen et al (1998).

    :param ni_sw_rad: Net incoming shortwave radiation [MJ m-2 day-1].
    :param no_lw_rad: Net outgoing longwave radiation [MJ m-2 day-1].
    :return: Daily net radiation [MJ m-2 day-1].
    :rtype: float
    """
    # Raise exceptions
    # TODO: raise exceptions for radiation arguments
    return ni_sw_rad - no_lw_rad


def psy_const(atmos_pres):
    """
    Calculate the psychrometric constant.

    This method assumes that the air is saturated with water vapour at T_min.
    This assumption may not hold in arid areas.

    Based on equation 8, page 95 in Allen et al (1998).

    :param atmos_pres: Atmospheric pressure [kPa]
    :return: Psychrometric constant [kPa degC-1].
    :rtype: float
    """
    return 0.000665 * atmos_pres


def psy_const_of_psychrometer(psychrometer, atmos_pres):
    """
    Calculate the psychrometric constant for different types of
    psychrometer at a given atmospheric pressure.

    Based on FAO equation 16 in Allen et al (1998).

    :param psychrometer: Integer between 1 and 3 which denotes type of
        psychrometer:
            1: ventilated (Asmann or aspirated type) psychrometer with
                an air movement of approximately 5 m/s
            2: natural ventilated psychrometer with an air movement
                of approximately 1 m/s
            3: non ventilated psychrometer installed indoors
    :param atmos_pres: Atmospheric pressure [kPa]
    :return: Psychrometric constant [kPa degC-1].
    :rtype: float
    """
    # Select coefficient based on type of ventilation of the wet bulb
    if psychrometer == 1:
        psy_coeff = 0.000662
    elif psychrometer == 2:
        psy_coeff = 0.000800
    elif psychrometer == 3:
        psy_coeff = 0.001200
    else:
        raise ValueError(
            'psychrometer should be in range 1 to 3: {0!r}'.format(psychrometer))

    return psy_coeff * atmos_pres


def rh_from_ea_es(ea, es):
    """
    Calculate relative humidity as the ratio of actual vapour pressure
    to saturation vapour pressure at the same temperature.

    See Allen et al (1998), page 67 for details.

    :param ea: Actual vapour pressure [units don't matter as long as same as
        es].
    :param es: Saturated vapour pressure [units don't matter as long as same as
        ea].
    :return: Relative humidity [%].
    :rtype: float
    """
    return 100.0 * ea / es


def sol_dec(doy):
    """
    Calculate solar declination from day of the year.

    Based on FAO equation 24 in Allen et al (1998).

    :param doy: Day of year (integer between 1 and 365 or 366).
    :return: solar declination [radians]
    :rtype: float
    """
    check_doy(doy)
    return 0.409 * math.sin(((2.0 * math.pi / 365.0) * doy - 1.39))


def sol_rad_from_sun_hours(daylight_hours, sunshine_hours, et_rad):
    """
    Calculate incoming solar (or shortwave) radiation (radiation hitting a
    horizontal plane after scattering by the atmosphere) from relative
    sunshine duration.

    If measured radiation data are not available this method is preferable
    to calculating solar radiation from temperature. If a monthly mean is
    required then divide the monthly number of sunshine hours by number of
    days in the month and ensure that *et_rad* and *daylight_hours* was
    calculated using the day of the year that corresponds to the middle of
    the month.

    Based on equations 34 and 35 in Allen et al (1998).

    :param dl_hours: Number of daylight hours [hours]
    :param sunshine_hours: Sunshine duration [hours]
    :param et_rad: Extraterrestrial radiation [MJ m-2 day-1]
    :return: Incoming solar (or shortwave) radiation [MJ m-2 day-1]
    :rtype: float
    """
    check_day_hours(sunshine_hours, 'sun_hours')
    check_day_hours(daylight_hours, 'daylight_hours')

    # 0.5 and 0.25 are default values of regression constants (Angstrom values)
    # recommended by FAO when calibrated values are unavailable.
    return (0.5 * sunshine_hours / daylight_hours + 0.25) * et_rad


def sol_rad_from_t(et_rad, cs_rad, tmin, tmax, coastal):
    """
    Estimate incoming solar (or shortwave) radiation, Rs, (radiation hitting
    a horizontal plane after scattering by the atmosphere) from min and max
    temperature together with an empirical adjustment coefficient for
    'interior' and 'coastal' regions.

    The formula is based on equation 50 in Allen et al (1998) which is the
    Hargreaves radiation formula (Hargreaves and Samani, 1982, 1985). This
    method should be used only when solar radiation or sunshine hours data are
    not available. It is only recommended for locations where it is not
    possible to use radiation data from a regional station (either because
    climate conditions are heterogeneous or data are lacking).

    **NOTE**: this method is not suitable for island locations due to the
    moderating effects of the surrounding water.

    :param et_rad: Extraterrestrial radiation [MJ m-2 day-1].
    :param cs_rad: Clear sky radiation [MJ m-2 day-1].
    :param tmin: Daily minimum temperature [deg C].
    :param tmax: Daily maximum temperature [deg C].
    :param coastal: ``True`` if site is a coastal location, situated on or
        adjacent to coast of a large land mass and where air masses are
        influenced by a nearby water body, ``False`` if interior location
        where land mass dominates and air masses are not strongly influenced
        by a large water body.
    :return: Incoming solar (or shortwave) radiation (Rs) [MJ m-2 day-1].
    :rtype: float
    """
    # Determine value of adjustment coefficient [deg C-0.5] for
    # coastal/interior locations
    if coastal:
        adj = 0.19
    else:
        adj = 0.16

    solar_rad = adj * math.sqrt(tmax - tmin) * et_rad

    # The solar radiation value is constrained by the clear sky radiation
    return min(solar_rad, cs_rad)


def sol_rad_island(et_rad):
    """
    Estimate incoming solar (or shortwave) radiation (radiation hitting a
    horizontal plane after scattering by the atmosphere) for an island
    location.

    An island is defined as a land mass with width perpendicular to the
    coastline <= 20 km. Use this method only if radiation data from
    elsewhere on the island is not available.

    **NOTE**: This method is only applicable for low altitudes (0-100 m)
    and monthly calculations.

    Based on FAO equation 51 in Allen et al (1998).

    :param et_rad: Extraterrestrial radiation [MJ m-2 day-1].
    :return: Incoming solar (or shortwave) radiation [MJ m-2 day-1].
    :rtype: float
    """
    return (0.7 * et_rad) - 4.0


def sunset_hour_angle(latitude, sd):
    """
    Calculate sunset hour angle (Ws) from latitude and solar
    declination.

    Based on FAO equation 25 in Allen et al (1998).

    :param latitude: Latitude [radians]. Note: *latitude* should be negative
        if it in the southern hemisphere, positive if in the northern
        hemisphere.
    :param sd: Solar declination [radians].
    :return: Sunset hour angle [radians].
    :rtype: float
    """
    check_latitude_rad(latitude)
    check_sol_dec_rad(sd)

    # Calculate sunset hour angle (sha) [radians] from latitude and solar
    # declination using FAO equation 25
    tmp = -math.tan(latitude) * math.tan(sd)
    # Domain of acos = -1 <= x <= 1; this is not pointed out by FAO
    tmp = max(tmp, -1.0)
    tmp = min(tmp, 1.0)
    return math.acos(tmp)


def wind_speed_2m(meas_ws, z):
    """
    Convert wind speed measured at different heights above the soil
    surface to wind speed at 2 m above the surface, assuming a short grass
    surface.

    Based on FAO equation 47 in Allen et al (1998).

    :param meas_ws: Measured wind speed [m s-1]
    :param z: Height of wind measurement above ground surface [m]
    :return: Wind speed at 2 m above the surface [m s-1]
    :rtype: float
    """
    return meas_ws * (4.87 / math.log((67.8 * z) - 5.42))
