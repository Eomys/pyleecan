# -*- coding: utf-8 -*-
from numpy import array, mod, zeros

from ....Methods.Machine.Winding import WindingError
from ....Functions.Winding.reverse_wind_mat import reverse_wind_mat
from ....Functions.Winding.shift_wind_mat import shift_wind_mat


def init_as_CW2LT(self, Zs=None):
    """Compute the Winding Matrix (for winding type 1)
    type 1 : TOOTH WINDING, DOUBLE LAYER ALL TEETH WOUND, ORTHORADIAL
    SUPERPOSITION  (Nlay_rad=1,Nlay_tan=2)

    Parameters
    ----------
    self : WindingUD
        A: WindingUD object
    Zs : int
        Number of Slot (Integer >0)

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
    # Ncspc= Zs/(2.0*qs*self.Npcp/nlay)  # number of coils in series per parallel circuit
    # Ntspc = self.Ntcoil * Ncspc #Number of turns in series per phase
    Ntcoil = self.Ntcoil  # number of turns per coils

    wind_mat = zeros((1, 2, Zs, int(qs)))
    # creates highest harmonic at Zs/2+1 and Zs/2-1
    if ms == 0.5:  # then Zs/qs is integer
        # traditional non overlapping all teeth wound winding
        for q in range(0, int(qs)):
            for k in range(0, int(Zs / qs)):  # number of Ncgr coils
                xenc = q + array([1, 0]) + k * qs
                wind_mat[0, 0, int(mod(xenc[0] - 1, Zs)), q] = +Ntcoil  # right/top/2
                wind_mat[0, 1, int(mod(xenc[1] - 1, Zs)), q] = -Ntcoil  # left/bottom/1
    elif ms != 0.5 and Ncgr % 1 == 0:
        # ms!=0.5 and Ncgr is an integer (ms>0.25 && ms<0.5)
        # new algorithm to reverse the coils
        for q in range(0, int(qs)):
            for k in range(0, int(nlay)):  # number of Ncgr coils
                for l in range(0, int(Ncgr)):
                    id0 = int(mod(q * Ncgr + 0 + k * qs * Ncgr - 1 + l, Zs))
                    id1 = int(mod(q * Ncgr + 1 + k * qs * Ncgr - 1 + l, Zs))
                    # left / bottom / 1
                    wind_mat[0, 1, id0, q] = -((-1) ** (l + q - 1 + k)) * Ntcoil
                    # right / top / 2
                    wind_mat[0, 0, id1, q] = +((-1) ** (l + q - 1 + k)) * Ntcoil

    else:
        raise WindingT1DefMsError(
            "Winding geometry not handled yet. Enter "
            "your own winding matrix with WindingUD"
            " and contact EOMYS"
        )

    # Set default values
    if self.is_reverse_wind is None:
        self.is_reverse_wind = False
    if self.Nslot_shift_wind is None:
        self.Nslot_shift_wind = 0
    self.Nlayer = 2
    # Apply the transformations
    if self.is_reverse_wind:
        wind_mat = reverse_wind_mat(wind_mat)
    if self.Nslot_shift_wind > 0:
        wind_mat = shift_wind_mat(wind_mat, self.Nslot_shift_wind)

    self.wind_mat = wind_mat
    # Matrix changed, compute again periodicity
    self.per_a = None
    self.is_aper_a = None


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
