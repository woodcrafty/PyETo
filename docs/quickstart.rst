===========
Quick start
===========

You can install the library directly from PyPI::

   pip install pyeto

Usage
=====
All public functions and constants are available via the package name::

    >>> import pyeto

The evapotranspiration methods vary in the amount of input data they require.
Measurements of for each input variable are frequently not available so PyETo
implements many functions for estimating "missing data".

For example, atmospheric pressure can be estimated from altitude::

    >>> pyeto.atm_pressure(1000)  # pressure at 1000 m, in kilo Pascals
    90.02461995703662

And saturation vapour pressure (*es*), can be estimated from temperature::

    >>> pyeto.svp_from_t(15.0)  # Sat. vapour pressure in kilo Pascals
    1.7053462321157722

