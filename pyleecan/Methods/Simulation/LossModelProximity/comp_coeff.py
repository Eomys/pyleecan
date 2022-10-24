# -*- coding: utf-8 -*-
from numpy import pi


def comp_coeff(self):
    """Compute the Proximity loss coefficient [W/kg]

    Parameters
    ----------
    self : LossModelProximity
    """
    T_op = self.parent.Tsta
    winding = self.parent.parent.machine.stator.winding
    sigma = winding.conductor.cond_mat.elec.get_conductivity(T_op=T_op)
    d = winding.conductor.Wwire
    kf = self.parent.parent.machine.stator.comp_fill_factor()

    # Proximity loss coefficient [W/kg]
    self.k_p = kf * pi ** 2 / 8 * sigma * d ** 2
