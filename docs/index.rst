=====
PyETo
=====
*PyETo* is a Python package for calculating reference crop evapotranspiration
(ET\ :sub:`o`\ ), sometimes referred to as potential evapotranspiration (PET).
The library provides numerous functions for estimating missing meteorological
data.

Three methods for estimating ET\ :sub:`o`\ /PET are implemented:

* FAO-56 Penman-Monteith (Allen et al, 1998)
* Hargreaves (Hargreaves and Samani, 1985)
* Thornthwaite (Thornthwaite, 1948)

What does it look like? Here is a simple example that estimates monthly
potential evapotranspiration for Aberdeen, Scotland (latitude 57.1526
degrees N), using the Thornthwaite method::

   >>> import pyeto
   >>> latitude = pyeto.deg2rad(57.1526)   # Convert latitude to radians
   >>> mean_monthly_temperature = [
    >>>     3.1, 3.5, 5.0, 6.7, 9.3, 12.1, 14.3, 14.1, 11.8, 8.9, 5.5, 3.8]
   >>> monthly_mean_daylight = pyeto.monthly_mean_daylight_hours(latitude)
   >>> pyeto.thornthwaite(mean_monthly_temperature, monthly_mean_daylight)
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

Installation
------------
There is currently no way to install this package so you will have to include the source in your project in order to use it.

Documentation contents
----------------------
This part of the documentation guides you through the various
evapotranspiration methods.

.. toctree::
   :maxdepth: 2

   overview
   fao56_penman_monteith
   hargreaves
   thornthwaite
   references
   changelog
   license

API Reference
-------------
If you are looking for information on a specific function, this part of the
documentation is for you.

.. toctree::
   :maxdepth: 2

   api

