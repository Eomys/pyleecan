# -*- coding: utf-8 -*-


from numpy import mod, zeros, arange, sign

from ....Methods.Machine.Winding import WindingError
from ....Functions.Winding.reverse_wind_mat import reverse_wind_mat
from ....Functions.Winding.shift_wind_mat import shift_wind_mat


def comp_connection_mat(self, Zs=None):
    """Compute the Winding Matrix (for winding type 3 or 4) (Nlay_rad=1 or 2,Nlay_tan=1)
    type 3 or 4 : DISTRIBUTED SHORTED PITCH INTEGRAL WINDING

    Parameters
    ----------
    self : Winding
        A: Winding object
    Zs : int
        Number of Slot (Integer >0)

    Returns
    -------
    wind_mat: numpy.ndarray
        Winding Matrix (1 or 2, 1, Zs, qs)

    Raises
    ------
    WindingDefMsError
        Zs/2/p/qs must be an integer

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

    coil_pitch = self.coil_pitch
    p = self.p
    nlay = self.get_dim_wind()[0]
    qs = self.qs
    ms = Zs / 2.0 / float(p) / float(qs)
    tausp = Zs / 2.0 / float(p)
    Ntcoil = self.Ntcoil  # number of turns per coils
    wind_mat = zeros((nlay, 1, Zs, qs))

    if qs == 3:
        phase_order = [1, -3, 2]
    else:
        phase_order = range(1, qs + 1)
    if ms % 1 != 0:  # if ms isn't an integer
        raise WindingDefMsError(
            "wrong winding definition, Zs/2/p/qs must " "be an integer !"
        )
    ms = int(ms)
    tausp = int(tausp)  # if ms is an integer, tausp is

    # shorted pitch Nlay-layered integral overlapping windings
    for nl in range(0, nlay):
        for i in range(0, p):
            for k in range(0, qs):
                ph = abs(phase_order[k])
                # cf Gieras p36
                z = (
                    arange(1, ms + 1)
                    + i * (Zs / p)
                    + k * ms
                    + nl * (coil_pitch - tausp)
                )

                sp = ((z - 1) % Zs).astype(int)  # positive pole
                sm = ((z + Zs / 2 / p - 1) % Zs).astype(int)  # negative pole
                for s in sp:
                    wind_mat[nl, 0, s, ph - 1] = Ntcoil * sign(
                        phase_order[k]
                    )  # Accumulation for a single slot
                for s in sm:
                    wind_mat[nl, 0, s, ph - 1] = -Ntcoil * sign(
                        phase_order[k]
                    )  # Accumulation for a single slot

    # Set default values
    if self.is_reverse_wind is None:
        self.is_reverse_wind = False
    if self.Nslot_shift_wind is None:
        self.Nslot_shift_wind = 0
    # Apply the transformations
    if self.is_reverse_wind:
        wind_mat = reverse_wind_mat(wind_mat)
    if self.Nslot_shift_wind > 0:
        wind_mat = shift_wind_mat(wind_mat, self.Nslot_shift_wind)

    return wind_mat


class WindingDefMsError(WindingError):
    """ """

    pass
