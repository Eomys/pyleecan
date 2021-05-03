# -*- coding: utf-8 -*-
from numpy import pi

from ....Classes.Winding import Winding
from ....Methods import NotImplementedYetError
from ....Classes.LamSlot import LamSlot


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
    surf_lam = LamSlot.build_geometry(self, sym=sym, alpha=alpha, delta=delta)
    surf_list = list()
    if self.slot is not None and self.slot.Zs != 0:
        # getting number of slot
        Zs = self.slot.Zs
        # getting angle between Slot
        angle = 2 * pi / Zs
        # getting Nrad and Ntan
        if self.winding is None:
            Nrad, Ntan = 1, 1
            surf_Wind = list()
        else:
            try:
                Nrad, Ntan = self.winding.get_dim_wind()
            except Exception:
                Nrad, Ntan = 1, 1

            surf_Wind = self.slot.build_geometry_active(
                Nrad=Nrad,
                Ntan=Ntan,
                is_simplified=is_simplified,
                alpha=alpha,
                delta=delta,
            )

        if self.is_stator:
            st = "Stator"
        else:
            st = "Rotor"
        assert (self.slot.Zs % sym) == 0, (
            "ERROR, Wrong symmetry for "
            + st
            + " "
            + str(self.slot.Zs)
            + " slots and sym="
            + str(sym)
        )
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
