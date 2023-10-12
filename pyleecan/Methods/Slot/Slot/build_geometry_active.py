# -*- coding: utf-8 -*-

from numpy import linspace


def build_geometry_active(self, Nrad, Ntan, alpha=0, delta=0):
    """Split the slot active area in several zone
    This method assume that the active area is centered on X axis and symetrical
    Otherwise a dedicated build_geometry_active method must be provided

    Parameters
    ----------
    self : Slot
        A Slot object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : Complex
        complex for translation (Default value = 0)

    Returns
    -------
    surf_list:
        List of surface delimiting the active zone

    """

    assert Ntan in [1, 2]

    surf_act = self.get_surface_active()

    # Find the two intersection point with Ox axis
    inter_list = list()
    for line in surf_act.get_lines():
        inter_list.extend(line.intersect_line(0, 100))
    # Remove/Merge intersection that are too close
    duplicate_list = list()
    for ii in range(len(inter_list)):
        for jj in range(ii + 1, len(inter_list)):  # Avoid comparing twice
            if jj not in duplicate_list and abs(inter_list[ii] - inter_list[jj]) < 1e-6:
                duplicate_list.append(jj)
    for duplicate in duplicate_list[::-1]:
        inter_list.pop(duplicate)

    assert (
        len(inter_list) == 2
    ), "Can't find the two points of the intersection with 0x axis"

    # Sort the intersection points (Ztan1 is closest to the bore)
    if abs(inter_list[0]) < abs(inter_list[1]) and self.is_outwards():
        Ztan1 = inter_list[0]
        Ztan2 = inter_list[1]
    elif abs(inter_list[0]) > abs(inter_list[1]) and self.is_outwards():
        Ztan1 = inter_list[1]
        Ztan2 = inter_list[0]
    elif abs(inter_list[0]) < abs(inter_list[1]) and not self.is_outwards():
        Ztan1 = inter_list[1]
        Ztan2 = inter_list[0]
    elif abs(inter_list[0]) > abs(inter_list[1]) and not self.is_outwards():
        Ztan1 = inter_list[0]
        Ztan2 = inter_list[1]

    # First Tan split
    tan_list = list()
    if Ntan == 2:
        top_surf, bot_surf = surf_act.split_line(
            0, 100, is_join=True, prop_dict_join=None
        )
        tan_list.append(bot_surf)
        tan_list.append(top_surf)
    else:
        tan_list = [surf_act]

    # Rad split
    surf_list = list()
    X_list = linspace(Ztan1, Ztan2, Nrad + 1, True).tolist()[1:-1]
    for ii in range(Ntan):
        surf = tan_list[ii]
        if Nrad > 1:
            for jj in range(Nrad - 1):
                X = X_list[jj]
                top_surf, bot_surf = surf.split_line(
                    X - 100j,
                    X + 100j,
                    is_join=True,
                    prop_dict_join=None,
                )
                if self.is_outwards():
                    surf_list.append(top_surf)
                    surf = bot_surf
                else:
                    surf_list.append(bot_surf)
                    surf = top_surf
            # Add the last surface
            surf_list.append(surf)
        else:  # add the radial surfaces without any other cut
            surf_list.append(surf.copy())

    # Set all label
    self.set_label(surf_list, Nrad, Ntan, self.parent.get_label())

    # Apply transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
