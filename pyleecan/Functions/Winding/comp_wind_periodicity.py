# -*- coding: utf-8 -*-

from numpy import array_equal, roll, squeeze, sum as np_sum
from numpy.linalg import norm


def comp_wind_periodicity(wind_mat):
    """Computes the winding pattern periodicity and symmetries

    Parameters
    ----------
    wind_mat : ndarray
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
        is_per = False
        while k <= Zs and not is_per:
            # We shift the array arround the slot and check if it's the same
            if array_equal(wind_mat2[:, q], roll(wind_mat2[:, q], shift=k)):
                is_per = True
            else:
                k += 1
        # least common multiple to find common periodicity between different phase
        Nperslot = lcm(Nperslot, k)

    # If Nperslot > Zs no symmetry
    if Nperslot > 0 and Nperslot < Zs:
        # nb of periods of the winding (2 means 180°)
        Nperw = Zs / float(Nperslot)
        # if Zs cannot be divided by Nperslot (non integer)
        if Nperw % 1 != 0:
            Nperw = 1

    # Check for anti symmetries in the elementary winding pattern
    if (
        Nperslot % 2 == 0
        and norm(
            wind_mat2[0 : Nperslot // 2, :] + wind_mat2[Nperslot // 2 : Nperslot, :]
        )
        == 0
    ):
        is_aper_wind = True
        Nperw = Nperw * 2
    else:
        is_aper_wind = False

    return int(Nperw), is_aper_wind


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
