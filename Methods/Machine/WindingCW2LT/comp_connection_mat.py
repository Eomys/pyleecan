# -*- coding: utf-8 -*-
"""@package Methods.Machine.Winding._comp_wind_type_1
Compute the Winding Matrix (for type 1) Method
@date Created on Mon Dec 15 14:21:45 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it for every ms case
@todo link every winding type to a validation case and an article
"""
from numpy import array, mod, zeros

from pyleecan.Methods.Machine.Winding import WindingError
from pyleecan.Functions.Winding.reverse_wind_mat import reverse_wind_mat
from pyleecan.Functions.Winding.shift_wind_mat import shift_wind_mat


def comp_connection_mat(self, Zs=None):
    """Compute the Winding Matrix (for winding type 1)
    type 1 : TOOTH WINDING, DOUBLE LAYER ALL TEETH WOUND, ORTHORADIAL
    SUPERPOSITION  (Nlay_rad=1,Nlay_tan=2)

    Parameters
    ----------
    self : Winding
        A: Winding object
    Zs : int
        Number of Slot (Integer >0)

    Returns
    -------
    wind_mat: numpy.ndarray
        Winding Matrix (Nlay_rad, Nlay_tan, Zs, qs)

    Raises
    ------
    WindingT1DefMsError
        You must have 0.25< Zs/2/p/qs <= 0.5

    """
    if Zs is None:
        if self.parent is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object."
            )

        if self.parent.slot is None:
            raise WindingError(
                "ERROR: The Winding object must be in a Lamination object with Slot."
            )

        Zs = self.parent.slot.Zs

    assert Zs > 0, "Zs must be >0"
    assert Zs % 1 == 0, "Zs must be an integer"

    # ex "Effect of Pole and Slot Combination on Noise and Vibration in Permanent
    # Magnet Synchronous Motor" creates highest harmonic at Zs/2+1 and Zs/2-1
    nlay = 2.0
    qs = float(self.qs)
    p = float(self.p)
    Ncgr = Zs / nlay / qs
    ms = Zs / 2.0 / p / qs
    # Ncspc= Zs/(2.0*qs*self.Npcpp/nlay)  # number of coils in series per parallel circuit
    # Ntspc = self.Ntcoil * Ncspc #Number of turns in series per phase
    Ntcoil = self.Ntcoil  # number of turns per coils

    wind_mat = zeros((1, 2, Zs, int(qs)))
    # creates highest harmonic at Zs/2+1 and Zs/2-1
    if ms == 0.5:  # then Zs/qs is integer
        # traditional non overlapping all teeth wound winding
        for q in range(0, int(qs)):
            for k in range(0, int(Zs / qs)):  # number of Ncgr coils
                xenc = -(q) + array([1, 0]) - (k) * qs
                wind_mat[
                    0, 0, int(mod(xenc[0] - 1, Zs)), q
                ] = +Ntcoil  # right / top / 2
                wind_mat[
                    0, 1, int(mod(xenc[1] - 1, Zs)), q
                ] = -Ntcoil  # left / bottom / 1
    elif ms != 0.5 and Ncgr % 1 == 0:
        # ms!=0.5 and Ncgr is an integer (ms>0.25 && ms<0.5)
        # new algorithm to reverse the coils
        for q in range(0, int(qs)):
            for k in range(0, int(nlay)):  # number of Ncgr coils
                for l in range(0, int(Ncgr)):
                    wind_mat[
                        0, 1, int(mod((q) * Ncgr + (k) * qs * Ncgr - 1 + (l), Zs)), q
                    ] = (
                        -((-1) ** (l + q - 1 + k)) * Ntcoil
                    )  # left / bottom / 1
                    wind_mat[
                        0,
                        0,
                        int(mod((q) * Ncgr + 1 + (k) * qs * Ncgr - 1 + (l), Zs)),
                        q,
                    ] = (
                        +((-1) ** (l + q - 1 + k)) * Ntcoil
                    )  # right / top / 2

    else:
        raise WindingT1DefMsError(
            "Winding geometry not handled yet, enter "
            "your own winding matrix with type_winding=0"
            " and contact EOMYS"
        )

    # Apply the transformations
    if self.is_reverse_wind:
        wind_mat = reverse_wind_mat(wind_mat)
    if self.Nslot_shift_wind > 0:
        wind_mat = shift_wind_mat(wind_mat, self.Nslot_shift_wind)

    return wind_mat


class WindingT1DefMsError(WindingError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    must
        be 0

    """

    pass
