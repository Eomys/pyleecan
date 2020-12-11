# -*- coding: utf-8 -*-

from numpy import exp, pi, tan


def comp_surface(self):
    """Compute the surface of the Hole

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    S: float
        Surface of the Hole. [m**2]

    """

    Rext = self.get_Rext()

    alpha = self.comp_alpha()

    # Angle between (P1,P2) and (0,P0) is slot_pitch /2
    # It is also the angle (P1,P2,S)
    hsp = pi / self.Zh  # Half Slot Pitch

    # Distance P1,P9
    D19 = ((Rext - self.H0) * exp(1j * alpha / 2)).imag * 2

    # S is the intersectioni between (P1,P9) and the parallel to x passing by P2
    D1S = tan(hsp) * (self.H1 - self.H2)

    W1 = D19 / 2.0 - D1S - self.W0 / 2.0

    Smag = self.comp_surface_magnets()
    # Two air trapeze area
    Strap = ((D19 / 2.0 - self.W0 / 2.0) + W1) * (self.H1 - self.H2)

    return Smag + Strap
