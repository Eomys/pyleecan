# -*- coding: utf-8 -*-

from numpy import arcsin, arctan, cos, exp, array, angle, pi
from numpy import imag as np_imag
from scipy.optimize import fsolve

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.Arc1 import Arc1


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment) needed to plot the Hole.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleUD
        A HoleUD object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
       True to avoid line superposition (not used)

    Returns
    -------
    surf_list: list
        List of SurfLine needed to draw the Hole
    """

    surf_list = self.surf_list

    if self.get_is_stator():
        st = "_Stator"
    else:
        st = "_Rotor"

    # Update surface labels
    hole_id = 0
    mag_id = 0
    for surf in surf_list:
        if "HoleMagnet" in surf.label:
            key = "magnet_" + str(mag_id)
            if key in self.magnet_dict and self.magnet_dict[key] is not None:
                mag = self.magnet_dict[key]
                if mag.type_magnetization == 0:
                    type_mag = "_Radial"
                else:
                    type_mag = "_Parallel"
                surf.label = (
                    "HoleMagnet" + st + type_mag + "_N_R0_T" + str(mag_id) + "_S0"
                )
                mag_id += 1
            else:  # Magnet disabled or not defined
                surf.label = "Hole" + st + "_R0_T" + str(hole_id) + "_S0"
                hole_id += 1
        elif "Hole" in surf.label:
            surf.label = "Hole" + st + "_R0_T" + str(hole_id) + "_S0"
            hole_id += 1

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
