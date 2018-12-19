# -*- coding: utf-8 -*-
"""@package build_geometry
@date Created on juin 20 14:04 2018
@author franco_i
"""
from numpy import pi

from pyleecan.Methods import NotImplementedYetError
from pyleecan.Methods.Machine.LamSlot.build_geometry import build_geometry as build_geo


def build_geometry(self, sym=1, alpha=0, delta=0, is_simplified=False):
    """Build the geometry of the Lamination with winding in slots

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_simplified: bool
        True to avoid line superposition

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination
    
    """
    # getting the Lamination surface
    surf_lam = build_geo(self, sym=sym, alpha=alpha, delta=delta)
    surf_list = list()
    # getting number of slot
    Zs = self.slot.Zs
    # getting angle between Slot
    angle = 2 * pi / Zs
    # getting Nrad and Ntan
    try:
        Nrad, Ntan = self.winding.get_dim_wind()
    except NotImplementedYetError:
        Nrad, Ntan = 1, 1
    surf_Wind = self.slot.build_geometry_wind(
        Nrad=Nrad, Ntan=Ntan, is_simplified=is_simplified, alpha=alpha, delta=delta
    )

    assert (Zs % sym) == 0
    for ii in range(Zs // sym):  # for each slot
        # for each part of the winding surface in the slot
        for surf in surf_Wind:
            new_surf = type(surf)(init_dict=surf.as_dict())
            # changing the slot reference number
            new_surf.label = surf.label[:-1] + str(ii)
            new_surf.rotate(ii * angle)
            surf_list.append(new_surf)

    # Shift to have a tooth center on Ox
    for surf in surf_list:
        surf.rotate(pi / Zs)

    surf_list = surf_lam + surf_list

    return surf_list
