# -*- coding: utf-8 -*-

from numpy import array, power, zeros

from ....Methods.Machine.Winding import WindingError
from ....Functions.Winding.reverse_wind_mat import reverse_wind_mat
from ....Functions.Winding.shift_wind_mat import shift_wind_mat


def init_as_CW1L(self, Zs=None):
    """Compute the Winding Matrix (for winding type 2)
    type 2 : TOOTH WINDING, SINGLE LAYER ALTERNATE TEETH WOUND
    (Nlay_rad=1,Nlay_tan=1)

    Parameters
    ----------
    self : WindingUD
        A: WindingUD object
    Zs : int
        Number of Slot (Integer >0)

    Raises
    ------
    WindingT2DefNtError
        Zs/qs/2 must be an integer

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

    # non overlapping ALTERNATE TEETH WOUND-> single layer
    # cf "2D exact analytical model for surface-mounted permanent-magnet motors
    # with semi-closed slots" -> U motor 10p/18s creates 2p, Zs/2+2p, Zs/2-2p

    qs = self.qs  # Phase Number
    Nt = Zs / float(qs) / 2.0  # Number of teeth by semi phase

    # Ncspc= Zs/(2.0*qs*self.Npcp/nlay)  # number of coils in series per parallel circuit
    # Ntspc = self.Ntcoil * Ncspc #Number of turns in series per phase
    Ntcoil = self.Ntcoil  # number of turns per coils

    if round(Nt) != Nt:  # Nt must be an integer
        raise WindingT2DefNtError(
            "wrong winding definition, cannot wind all "
            "the teeth (Zs/qs/2 is not an integer)!"
        )

    # first strategy - checked with Umbra_08 motor and Umbra_05: the winding
    # direction of each tooth is reversed
    wind_mat = zeros((1, 1, Zs, qs))

    for k in range(0, int(Nt)):  # winding alternatively the teeth
        for q in range(0, qs):
            xenc = q * 4 + k * 2 * qs + array([1, 2])
            wind_mat[0][0][int((xenc[0] - 1) % Zs)][q] = power(-1, xenc[0] + k + 1)
            wind_mat[0][0][int((xenc[1] - 1) % Zs)][q] = power(-1, xenc[1] + k + 1)

    wind_mat *= Ntcoil

    # Set default values
    if self.is_reverse_wind is None:
        self.is_reverse_wind = False
    if self.Nslot_shift_wind is None:
        self.Nslot_shift_wind = 0
    self.Nlayer = 1
    # Apply the transformations
    if self.is_reverse_wind:
        wind_mat = reverse_wind_mat(wind_mat)
    if self.Nslot_shift_wind > 0:
        wind_mat = shift_wind_mat(wind_mat, self.Nslot_shift_wind)

    self.wind_mat = wind_mat
    # Matrix changed, compute again periodicity
    self.per_a = None
    self.is_aper_a = None


class WindingT2DefNtError(WindingError):
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
