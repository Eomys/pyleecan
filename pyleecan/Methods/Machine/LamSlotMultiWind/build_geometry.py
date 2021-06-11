# -*- coding: utf-8 -*-
from numpy import pi

from ....Classes.Winding import Winding
from ....Methods import NotImplementedYetError
from ....Classes.LamSlot import LamSlot


def build_geometry(self, sym=1, alpha=0, delta=0, is_simplified=False):
    """Build the geometry of the LamSlotMulti with winding in slots

    Parameters
    ----------
    self : LamSlotMultiWind
        A LamSlotMultiWind object
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
    surf_lam = LamSlot.build_geometry(self, sym=sym, alpha=alpha, delta=delta)

    # getting the winding surface
    surf_list = list()
    if self.slot_list is not None and self.slot_list[0].Zs != 0:
        if self.is_stator:
            st = "Stator"
        else:
            st = "Rotor"
        # getting angle between Slot
        angle = self.alpha
        # getting Nrad and Ntan
        if self.winding is None or self.winding.conductor is None:
            Nrad, Ntan = 1, 1
            surf_Wind = list()
        else:
            try:
                Nrad, Ntan = self.winding.get_dim_wind()
            except Exception:
                Nrad, Ntan = 1, 1

            for ii in range(int(len(angle) / sym)):  # for each slot
                # get the winding surface
                surf_Wind = self.slot_list[ii].build_geometry_active(
                    Nrad=Nrad,
                    Ntan=Ntan,
                    is_simplified=is_simplified,
                    alpha=alpha,
                    delta=delta,
                )

                # for each part of the winding surface in the slot
                for surf in surf_Wind:
                    new_surf = type(surf)(init_dict=surf.as_dict())
                    # changing the slot reference number
                    new_surf.label = surf.label[:-1] + str(ii)
                    new_surf.rotate(angle[ii])
                    surf_list.append(new_surf)

    surf_list = surf_lam + surf_list

    return surf_list
