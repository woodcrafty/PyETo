========
Overview
========
Three methods for estimating reference evapotranspiration (ET\ :sub:`o`\ ) and
potential evapotranspiration (PET) are implemented:

1. FAO Penman-Monteith (Allen et al, 1998)
2. Hargreaves (Hargreaves and Samani, 1985)
3. Thornthwaite (Thornthwaite, 1948)

Numerous functions for estimating missing meteorological input data are
also available.

-----------------
Package structure
-----------------


The PyETo package contains two modules, ``fao`` and ``thornthwaite``. See the
API documentation for a description of what is in these two modules. Note, that
the functions in ``fao`` and ``thornthwaite`` and aso available via the
package name, ``pyeto``, for convenience.

