"""
Internal validation functions.

:copyright: (c) 2015 by Mark Richards.
:license: BSD 3-Clause, see LICENSE.txt for more details.
"""
from pyeto.convert import deg2rad

# Internal constants
_MINLAT_RADIANS = deg2rad(-90.0)
_MAXLAT_RADIANS = deg2rad(90.0)


def check_doy(doy):
    """
    Check day of the year is valid.
    """
    if not 1 <= doy <= 366:
        raise ValueError(
            'Day of the year (doy) must be in range 1-366: {0!r}'.format(doy))

def check_latitude_rad(latitude):
     if not _MINLAT_RADIANS <= latitude <= _MAXLAT_RADIANS:
        raise ValueError(
            'latitude outside of valid range: {0!r} radians'.format(latitude))


def check_sol_dec_rad(sd):
    """
    Solar declination can vary between -90 and +90 degrees, the same as
    latitude.
    """
    try:
        check_latitude_rad(sd)
    except ValueError:
        raise ValueError(
            'solar declination outside of valid range: {0!r} radians'
            .format(sd))


def check_day_hours(hours, arg_name):
    """
    Check that *hours* is in the range 1 to 24.
    """
    if not 0 <= hours <= 24:
        raise ValueError(
            '{0} should be in range 0-24: {1!r}'.format(arg_name, hours))
