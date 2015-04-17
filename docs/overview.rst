========
Overview
========
You can install the library directly from PyPI::

   pip install pyeto

Once installed, all public functions and constants are available via the
package name::

    >>> import pyeto

PyETo currently implements the following methods for estimating
evapotranspiration:

* FAO-56 Penman-Monteith:``pyeto.fao56_penman_monteith()``
* Hargreaves: ``pyeto.hargreaves()``
* Thornthwaite: ``pyeto.thornthwaite()``

Instructions and examples of using each of these methods is given elsewhere in
the documentation.

Estimating missing data
-----------------------
Measurements of the necessary meteorological input variables for each method
are frequently not available. To help with this problem, PyETo implements
numerous functions for estimating "missing data". Most of these functions are
based on the methods described by Allen et al (1998).

For example, atmospheric pressure can be estimated from altitude::

    >>> pyeto.atm_pressure(1000)  # pressure at 1000 m, in kilo Pascals
    90.02461995703662

And saturation vapour pressure (*es*), can be estimated from temperature::

    >>> pyeto.svp_from_t(15.0)  # Sat. vapour pressure in kilo Pascals
    1.7053462321157722

The API provides details of the functions available for estimating missing data.

Converting units
----------------
Careful attention must be paid to the units of each parameter supplied to a
function. Different functions may require the same variable, but in different
units. To assist with the handling of units, PyETo provides a small
collection of functions for converting between commonly used units. For
example, a location's latitude in angular degrees can be converted to radians::

    >>> pyeto.deg2rad(57.1)
    0.9965830028887622

...or from radians into degrees::

    >>> pyeto.rad2deg(0.9965830028887622)
    57.1

See the unit conversion section in the API for a full list of unit conversion
functions.
