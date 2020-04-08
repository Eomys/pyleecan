# -*- coding: utf-8 -*-
from numpy import pi

from pyleecan.Methods.Machine.LamSlot.build_geometry import build_geometry as build_geo


def build_geometry(self, is_magnet=True, sym=1, alpha=0, delta=0, is_simplified=False):
    """ Build the geometry of the LamSlotMag

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

    assert (self.slot.Zs % sym) == 0

    if self.is_stator:
        st = "Stator"
    else:
        st = "Rotor"

    # getting the LamSlot surface
    surf_list = build_geo(self, sym=sym)

    Zs = self.slot.Zs
    slot_pitch = 2 * pi / Zs
    Nmag = len(self.slot.magnet)
    Sw = self.slot.comp_angle_opening()  # Opening angle of all the slots
    Sw_mag = self.slot.comp_angle_opening_magnet()  # Opening angle of one slot

    # Add the magnet surface(s)
    if is_magnet:
        # for each slot to draw
        for ii in range(Zs // sym):
            alpha_s = ii * slot_pitch + slot_pitch / 2  # Angle to rotate
            # the magnet
            for jj in range(Nmag):  # for each subslot in the slot
                beta = alpha_s - Sw / 2 + Sw_mag / 2 + (Sw_mag + self.slot.W3) * jj
                mag_surf = self.slot.magnet[jj].build_geometry(
                    alpha=beta, is_simplified=is_simplified
                )
                # Defining type of magnetization of the magnet
                if self.slot.magnet[jj].type_magnetization == 0:
                    type_mag = "Radial"
                elif self.slot.magnet[jj].type_magnetization == 1:
                    type_mag = "Parallel"
                elif self.slot.magnet[jj].type_magnetization == 2:
                    type_mag = "Hallbach"

                surf_list.extend(mag_surf)
                # Adapt the label
                if ii % 2 != 0:  # South pole
                    surf_list[-1].label = (
                        "Magnet"
                        + st
                        + type_mag
                        + "_S_R0"
                        + "_T"
                        + str(jj)
                        + "_S"
                        + str(ii)
                    )
                else:  # North pole
                    surf_list[-1].label = (
                        "Magnet"
                        + st
                        + type_mag
                        + "_N_R0"
                        + "_T"
                        + str(jj)
                        + "_S"
                        + str(ii)
                    )

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
