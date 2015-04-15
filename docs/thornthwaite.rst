=====================
Thornthwaite equation
=====================

The Thornthwaite (1948) equation is a widely used empirical method for
estimating potential evapotranspiration (PET). The equation only requires mean
monthly air temperature and mean daily daylight hours for each month, which
can be calculated from latitude.

The following example estimates monthly PET in 2014 for Aberdeen, Scotland
(latitude 57.1526 degrees N):

First convert latitude to radians and calculate the monthly mean daylight
hours::

    >>> from pyeto import thornthwaite, monthly_mean_daylight_hours, deg2rad
    >>> lat = deg2rad(57.1526)  # Convert latitude in degrees to radians
    >>> # Calculate mean daylight hours of each month
    >>> mmdlh = monthly_mean_daylight_hours(lat, 2014)
    >>> mmdlh
    [7.182842574993897,
     9.13512841264262,
     11.523002734356053,
     14.035348256722466,
     16.277003584884323,
     17.505213218539176,
     16.891449464611544,
     14.861767363416547,
     12.394150156712453,
     9.88498386070613,
     7.658250142104072,
     6.489516585536734]
    >>> # Create iterable of monthly mean temperatures in degrees Celsius
    >>> monthly_t = [
    >>>     3.1, 3.5, 5.0, 6.7, 9.3, 12.1, 14.3, 14.1, 11.8, 8.9, 5.5, 3.8]
    >>> thornthwaite(monthly_t, mmdlh)   # Calculate PET
    [11.04590543317501,
     14.225860424373405,
     27.802870598091953,
     43.178869424774305,
     70.47694909766452,
     93.99420906995957,
     109.69881616481408,
     95.24491684988213,
     64.9945211942068,
     41.06371810827504,
     19.562094545836995,
     12.090183352107148]

