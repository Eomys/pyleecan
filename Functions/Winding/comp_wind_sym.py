# -*- coding: utf-8 -*-
"""@package Functions.comp_wind_sym
computes the winding pattern periodicity and symmetries function
@date Created on Tue Dec 23 09:51:35 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import array_equal, roll, squeeze, sum as np_sum


def comp_wind_sym(wind_mat):
    """Computes the winding pattern periodicity and symmetries

    Parameters
    ----------
    wind_mat : numpy.ndarray
        Matrix of the Winding

    Returns
    -------
    Nperw: int
        Number of electrical period of the winding

    """
    assert len(wind_mat.shape) == 4, "dim 4 expected for wind_mat"

    # Summing on all the layers (Nlay_r and Nlay_theta)
    wind_mat2 = squeeze(np_sum(np_sum(wind_mat, axis=1), axis=0))

    qs = wind_mat.shape[3]  # Number of phase
    Zs = wind_mat.shape[2]  # Number of Slot

    Nperw = 1  # Number of electrical period of the winding
    Nperslot = 1  # Periodicity of the winding in number of slots

    # Looking for the periodicity of each phase
    for q in range(0, qs):
        k = 1
        is_sym = False
        while k <= Zs and not is_sym:
            # We shift the array arround the slot and check if it's the same
            if array_equal(wind_mat2[:, q], roll(wind_mat2[:, q], shift=k)):
                is_sym = True
            else:
                k += 1
        # least common multiple to find common periodicity between different
        #  phase
        Nperslot = lcm(Nperslot, k)

    # If Nperslot > Zs no symmetry
    if Nperslot > 0 and Nperslot < Zs:
        # nb of periods of the winding (2 means 180°)
        Nperw = Zs / float(Nperslot)
        # if Zs cannot be divided by Nperslot (non integer)
        if Nperw % 1 != 0:
            Nperw = 1

    return int(Nperw)


def gcd(a, b):
    """Return the greatest common divisor of a and b

    Parameters
    ----------
    a : int
        first number
    b : int
        second number

    Returns
    -------
    gcd : int
        greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return the least common multiple of a and b

    Parameters
    ----------
    a : int
        first number
    b : int
        second number

    Returns
    -------
    lcm : int
        least common multiple of a and b
    """
    return a * b // gcd(a, b)
