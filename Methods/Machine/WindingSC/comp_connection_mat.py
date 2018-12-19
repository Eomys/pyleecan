# -*- coding: utf-8 -*-
"""@package Methods.Machine.Winding._comp_wind_type_10
Compute the Winding Matrix (for type 10) Method
@date Created on Tue Jan 27 11:55:02 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import zeros

from pyleecan.Methods.Machine.Winding import WindingError
from pyleecan.Functions.Winding.reverse_wind_mat import reverse_wind_mat
from pyleecan.Functions.Winding.shift_wind_mat import shift_wind_mat


def comp_connection_mat(self, Zs):
    """Compute the Winding Matrix (for winding type 10)
    type 10 : Squirrel cage Winding (elementary circuit loop involving bar n°1
    and bar n°Zr for alphar0_rad=0) (Nlay_rad=Nlay_tan=1)

    Parameters
    ----------
    self : Winding
        A: Winding object
    Zs : int
        Number of Slot (Integer >0)

    Returns
    -------
    numpy.ndarray
        Winding Matrix (Nlay_rad, Nlay_tan, Zs, qs)

    Raises
    ------
    WindingT10DefQsError
        qs must be equal to Zs

    """

    assert Zs > 0, "Zs must be >0"
    assert Zs % 1 == 0, "Zs must be an integer"

    if self.qs != Zs:
        raise WindingT10DefQsError(
            "wrong winding definition, you must have " "qs = Zs !"
        )

    wind_mat = zeros((1, 1, Zs, self.qs))

    for ii in range(Zs):
        # phase n°ii
        wind_mat[0, 0, ii, ii] = -1
        wind_mat[0, 0, (ii - 1) % Zs, ii] = 1

    # Apply the transformations
    if self.is_reverse_wind:
        wind_mat = reverse_wind_mat(wind_mat)
    if self.Nslot_shift_wind > 0:
        wind_mat = shift_wind_mat(wind_mat, self.Nslot_shift_wind)

    return wind_mat


class WindingT10DefQsError(WindingError):
    """ """

    pass
