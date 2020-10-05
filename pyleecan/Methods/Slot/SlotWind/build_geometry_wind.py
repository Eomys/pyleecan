# -*- coding: utf-8 -*-

from numpy import angle, linspace
from scipy.optimize import fsolve

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
import matplotlib.pyplot as plt


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone
    This method assume that the winding area is centered on X axis and symetrical
    Otherwise a dedicated build_geometry_wind method must be provided

    Parameters
    ----------
    self : SlotWind
        A SlotWind object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    is_simplified : bool
        boolean to specify if coincident lines are considered as one or different lines (Default value = False)
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : Complex
        complex for translation (Default value = 0)

    Returns
    -------
    surf_list:
        List of surface delimiting the winding zone

    """

    assert Nrad in [1, 2]

    surf_wind = self.get_surface_wind()

    # Find the two intersection point with Ox axis
    inter_list = list()
    for line in surf_wind.get_lines():
        inter_list.extend(line.intersect_line(0, 100))
    assert len(inter_list) == 2

    if abs(inter_list[0]) < abs(inter_list[1]):
        Ztan1 = inter_list[0]
        Ztan2 = inter_list[1]
    else:
        Ztan1 = inter_list[1]
        Ztan2 = inter_list[0]

    # First Rad split
    rad_list = list()
    if Nrad == 2:
        rad_list.append(
            surf_wind.split_line(0, 100, is_top=False, is_join=True, label_join="")
        )
        rad_list.append(
            surf_wind.split_line(0, 100, is_top=True, is_join=True, label_join="")
        )
    else:
        rad_list = [surf_wind]

    # Tan split
    surf_list = list()
    X_list = linspace(Ztan1, Ztan2, Ntan + 1, True).tolist()[1:-1]
    for ii in range(Nrad):
        print("plop")
        surf = rad_list[ii]
        if Ntan > 1:
            for jj in range(Ntan - 1):
                X = X_list[jj]
                surf_list.append(
                    surf.split_line(
                        X - 100j, X + 100j, is_top=True, is_join=True, label_join=""
                    )
                )
                surf = surf.split_line(
                    X - 100j, X + 100j, is_top=False, is_join=True, label_join=""
                )
            # Add the last surface
            surf_list.append(surf)
        else:  # add the radial surfaces without any other cut
            surf_list.append(surf.copy())

    # Set all label
    set_label(surf_list, Nrad, Ntan, self.get_is_stator())

    # Apply transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list


def set_label(surf_list, Nrad, Ntan, is_stator):
    """Set the normalized label"""

    if is_stator:
        st = "S"
    else:
        st = "R"

    index = 0
    for ii in range(Nrad):
        for jj in range(Ntan):
            surf_list[index].label = (
                "Wind" + st + "_R" + str(ii) + "_T" + str(jj) + "_S0"
            )
            index += 1
