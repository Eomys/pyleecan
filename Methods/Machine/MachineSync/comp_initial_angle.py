# -*- coding: utf-8 -*-
"""@package Methods.MachineSync.comp_initial_angle
Compute the initial angle between the d-axis and the alpha-axis of the machine
@date Created on Thu Jul 30 21:56:00 2019
@author sebastian_g
@todo unittest it 
"""
from numpy import pi

from pyleecan.Methods.Machine.Winding import WindingError


def comp_initial_angle(self):
    """Compute initial angle between the d-axis and the alpha-axis of the machine

    Parameters
    ----------
    self : MachineSync
        A: MachineSync object
    
    Returns
    -------
    init_angle: float
        initial angle between rotor orientated coordinate system (dq) and stator orientated coordinate system (alpha-beta)

    Raises
    ------
    

    """
    if self.stator.winding is None:
        raise WindingError("ERROR: The Machine object must contain a Winding object.")

    Zs = self.stator.slot.Zs
    p = self.stator.winding.p

    stator_ang = self.stator.winding.comp_phasor_angle()[0] / p + pi / Zs - pi / (2 * p)
    rotor_ang = pi / (2 * p)

    return stator_ang - rotor_ang
