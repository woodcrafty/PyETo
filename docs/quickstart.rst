===========
Quick start
===========
You can install the library directly from PyPI::

   pip install pyeto

Usage
=====
All public functions and constants are available via the package name::

    >>> import pyeto


Estimating missing data
-----------------------
The evapotranspiration methods vary in the amount of input data they require.
Measurements of for each input variable are frequently not available so PyETo
implements many functions for estimating "missing data".

For example, atmospheric pressure can be estimated from altitude::

    >>> pyeto.atm_pressure(1000)  # pressure at 1000 m, in kilo Pascals
    90.02461995703662

And saturation vapour pressure (*es*), can be estimated from temperature::

    >>> pyeto.svp_from_t(15.0)  # Sat. vapour pressure in kilo Pascals
    1.7053462321157722

Converting units
----------------
Pay careful attention to the units of each argument supplied to a function.
Different functions may require the same variable, but in different units.
PyETo provides a small collection of functions for converting between commonly
used units. For example, a location's latitude in angular degrees can be
converted to radians::

    >>> pyeto.deg2rad(57.1)
    0.9965830028887622

...and from radians back into degrees::

    >>> pyeto.rad2deg(0.9965830028887622)
    57.1

See the Unit conversion section in the API for a full list of unit conversion
functions.

Calculating evapotranspiration
------------------------------
PyETo currently implements the following methods for estimating
evapotranspiration:

* FAO-56 Penman-Monteith using ``pyeto.fao56_penman_monteith()``
* Hargreaves method using ``pyeto.hargreaves()``
* Thornthwaite using ``pyeto.thornthwaite()``

