# -*- coding: utf-8 -*-

from numpy import pi, sin


def comp_resistance_wind(self, T=20, qs=3):
    """Computation of the equivalent rotor resistance of a cage winding with 'qs' number of phases

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object
    qs : int
        number of the equivalent rotor winding phases, default value: 3 phases

    Returns
    -------
    Rrot: float
         resistance of the rotor[Ohm]

    """
    # calculate resistance ring
    alpha = self.ring_mat.elec.alpha
    rho20 = self.ring_mat.elec.rho
    rho = rho20 * (1 + alpha * (T - 20))

    Sring = self.comp_surface_ring()
    lring = self.comp_length_ring()
    Zs = self.get_Zs()
    P = self.get_pole_pair_number()

    Rring = rho * lring / Sring

    # calculate resistance rod
    alpha = self.winding.conductor.cond_mat.elec.alpha
    rho20 = self.winding.conductor.cond_mat.elec.rho
    rho = rho20 * (1 + alpha * (T - 20))

    Srod = self.winding.conductor.comp_surface_active()
    lrod = self.comp_length() + 2 * self.winding.Lewout
    Rrod = rho * lrod / Srod

    # calculate total resistance
    Rtot = Zs / qs * (Rrod + Rring / Zs / (2 * sin(pi * P / Zs) ** 2))

    return Rtot
