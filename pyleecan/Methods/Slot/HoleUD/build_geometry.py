# -*- coding: utf-8 -*-

from numpy import arcsin, arctan, cos, exp, array, angle, pi
from numpy import imag as np_imag
from scipy.optimize import fsolve

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.Arc1 import Arc1
from ....Methods import ParentMissingError
from ....Functions.labels import HOLEV_LAB, HOLEM_LAB


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

    # Get correct label for surfaces
    lam_label = self.parent.get_label()
    R_id = "R" + str(self.parent.hole.index(self)) + "-T"
    vent_label = lam_label + "_" + HOLEV_LAB + "_" + R_id
    mag_label = lam_label + "_" + HOLEM_LAB + "_" + R_id

    # Update surface labels
    hole_id = 0
    mag_id = 0
    for surf in surf_list:
        if HOLEM_LAB in surf.label:
            key = "magnet_" + str(mag_id)
            if key in self.magnet_dict and self.magnet_dict[key] is not None:
                surf.label = mag_label + str(mag_id) + "-S0"
                mag_id += 1
            else:  # Magnet disabled or not defined
                surf.label = vent_label + str(hole_id) + "-S0"
                hole_id += 1
        elif HOLEV_LAB in surf.label:
            surf.label = vent_label + str(hole_id) + "-S0"
            hole_id += 1

    # Apply the transformations
    return_list = list()
    for surf in surf_list:
        return_list.append(surf.copy())
        return_list[-1].rotate(alpha)
        return_list[-1].translate(delta)

    return return_list
