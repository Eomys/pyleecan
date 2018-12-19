# -*- coding: utf-8 -*-
"""@package Methods.Machine.Winding._comp_wind_type_3
Compute the Winding Matrix (for type 3) Method
@date Created on Tue Dec 16 09:53:11 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import mod, zeros

from pyleecan.Methods.Machine.Winding import WindingError
from pyleecan.Functions.Winding.reverse_wind_mat import reverse_wind_mat
from pyleecan.Functions.Winding.shift_wind_mat import shift_wind_mat


def comp_connection_mat(self, Zs):
    """Compute the Winding Matrix (for winding type 3) (Nlay_rad=2,Nlay_tan=1)
    type 3 : DISTRIBUTED SHORTED PITCH INTEGRAL WINDING

    Parameters
    ----------
    self : Winding
        A: Winding object
    Zs : int
        Number of Slot (Integer >0)

    Returns
    -------
    wind_mat: numpy.ndarray
        Winding Matrix (2, 1, Zs, qs)

    Raises
    ------
    WindingT3DefMsError
        Zs/2/p/qs must be an integer

    """

    assert Zs > 0, "Zs must be >0"
    assert Zs % 1 == 0, "Zs must be an integer"

    coil_pitch = self.coil_pitch
    p = self.p
    nlay = 2
    qs = self.qs
    ms = Zs / 2.0 / float(p) / float(qs)
    tausp = Zs / 2.0 / float(p)
    # Ncspc= Zs/(2.0*qs*self.Npcpp/nlay)  # number of coils in series per parallel circuit
    # Ntspc = self.Ntcoil * Ncspc #Number of turns in series per phase
    Ntcoil = self.Ntcoil  # number of turns per coils
    wind_mat = zeros((2, 1, Zs, qs))

    if ms % 1 != 0:  # if ms isn't an integer
        raise WindingT3DefMsError(
            "wrong winding definition, Zs/2/p/qs must " "be an integer !"
        )
    ms = int(ms)
    tausp = int(tausp)  # if ms is an integer, tausp is

    # shorted pitch Nlay-layered integral overlapping windings
    for nl in range(0, nlay):
        for i in range(0, 2 * p):
            for ph in range(0, qs):
                for k in range(0, ms):  # cf Gieras p36
                    s = mod(
                        (i) * tausp
                        + (ph) * ms
                        + k
                        + 1
                        + (nl) * (coil_pitch - tausp)
                        - 1,
                        Zs,
                    )
                    wind_mat[nl, 0, s, ph] += ((-1) ** (i + ph)) * (Ntcoil)

    # Apply the transformations
    if self.is_reverse_wind:
        wind_mat = reverse_wind_mat(wind_mat)
    if self.Nslot_shift_wind > 0:
        wind_mat = shift_wind_mat(wind_mat, self.Nslot_shift_wind)

    return wind_mat


class WindingT3DefMsError(WindingError):
    """ """

    pass
