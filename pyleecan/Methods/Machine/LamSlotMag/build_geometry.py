# -*- coding: utf-8 -*-
from numpy import pi

from ....Classes.LamSlot import LamSlot
from ....Functions.labels import MAG_LAB


def build_geometry(self, is_magnet=True, sym=1, alpha=0, delta=0, is_simplified=False):
    """Build the geometry of the LamSlotMag

    Parameters
    ----------
    self : LamSlotMag
        LamSlotMag object
    is_magnet : bool
        If True build the magnet surfaces
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

    st = self.get_label()

    assert (self.slot.Zs % sym) == 0, (
        "ERROR, Wrong symmetry for "
        + st
        + " "
        + str(self.slot.Zs)
        + " slots and sym="
        + str(sym)
    )
    # getting the LamSlot surface
    surf_list = LamSlot.build_geometry(self, sym=sym)

    Zs = self.slot.Zs
    slot_pitch = 2 * pi / Zs

    # Add the magnet surface(s)
    if is_magnet and self.magnet is not None:
        # for each magnet to draw
        for ii in range(Zs // sym):
            mag_surf = self.slot.get_surface_active(
                alpha=slot_pitch * ii + slot_pitch * 0.5
            )

            surf_list.append(mag_surf)
            # Adapt the label
            surf_list[-1].label = st + "_" + MAG_LAB + "_R0-T0-S" + str(ii)

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
