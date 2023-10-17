from numpy import pi

from ....Classes.LamSlot import LamSlot
from ....Functions.labels import update_RTS_index
from ....Functions.labels import (
    BOUNDARY_PROP_LAB,
    COND_BOUNDARY_PROP_LAB,
    MAG_LAB,
    YSMR_LAB,
    YSML_LAB,
    LAM_LAB,
    YOKE_LAB,
    decode_label,
)


def build_geometry(
    self, is_magnet=True, sym=1, alpha=0, delta=0, is_circular_radius=False
):
    """Build the geometry of the LamSlotMag

    Parameters
    ----------
    self : LamSlotMagNS
        LamSlotMagNS object
    is_magnet : bool
        If True build the magnet surfaces
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_circular_radius : bool
        True to add surfaces to "close" the Lamination radii

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
    surf_list = LamSlot.build_geometry(
        self, sym=sym, alpha=alpha, delta=delta, is_circular_radius=is_circular_radius
    )

    Zs = self.slot.Zs
    slot_pitch = 2 * pi / Zs
    mag_surf_list = list()
    # Add North magnet surface(s)
    if is_magnet and self.magnet_north is not None:
        # Get the active surface to copy rotate
        Nrad, Ntan = self.get_dim_active()
        mag_layer_surf = self.slot.build_geometry_active(
            Nrad=Nrad,
            Ntan=Ntan,
            alpha=alpha,
            delta=delta,
        )

        # for each magnet to draw
        for ii in range(Zs // sym // 2):
            for surf in mag_layer_surf:
                mag_surf = surf.copy()
                # changing the slot reference number
                mag_surf.label = update_RTS_index(
                    label=surf.label, S_id=ii * 2, surf_type_label=MAG_LAB
                )
                mag_surf.rotate(ii * 2 * slot_pitch)
                mag_surf_list.append(mag_surf)
        # Update the magnets BC (if magnet side matches sym lines ex: SlotM18)
        if self.slot.is_full_pitch_active() and sym > 1:
            for surf in mag_surf_list:
                label_dict = decode_label(surf.label)
                # Set BC on Right side / Ox
                if label_dict["S_id"] == 0:
                    # Find the lines to add the BC
                    for line in surf.get_lines():
                        if (
                            line.prop_dict is not None
                            and COND_BOUNDARY_PROP_LAB in line.prop_dict
                            and line.prop_dict[COND_BOUNDARY_PROP_LAB] == YSMR_LAB
                        ):
                            line.prop_dict.update(
                                {
                                    BOUNDARY_PROP_LAB: st
                                    + "_"
                                    + YSMR_LAB
                                    + "-"
                                    + str(label_dict["R_id"])
                                }
                            )
        # Update Magnets BC when no lamination
        if self.Rint == self.Rext and self.Rint != 0:
            label_yoke = self.get_label() + "_" + LAM_LAB + YOKE_LAB
            for surf in mag_surf_list:
                label_dict = decode_label(surf.label)
                if label_dict["R_id"] == 0:
                    for line in surf.get_lines():
                        if (
                            line.prop_dict is not None
                            and COND_BOUNDARY_PROP_LAB in line.prop_dict
                            and line.prop_dict[COND_BOUNDARY_PROP_LAB] == YOKE_LAB
                        ):
                            line.prop_dict.update({BOUNDARY_PROP_LAB: label_yoke})

    # Add South magnet surface(s)
    if is_magnet and self.magnet_south is not None:
        # Get the active surface to copy rotate
        Nrad, Ntan = self.get_dim_active()
        mag_layer_surf = self.slot_south.build_geometry_active(
            Nrad=Nrad,
            Ntan=Ntan,
            alpha=alpha,
            delta=delta,
        )

        # for each magnet to draw
        for ii in range(Zs // sym // 2):
            id_mag = ii * 2 + 1
            for surf in mag_layer_surf:
                mag_surf = surf.copy()
                # changing the slot reference number
                mag_surf.label = update_RTS_index(
                    label=surf.label, S_id=id_mag, surf_type_label=MAG_LAB
                )
                mag_surf.rotate(id_mag * slot_pitch)
                mag_surf_list.append(mag_surf)
        # Update the magnets BC (if magnet side matches sym lines ex: SlotM18)
        if self.slot_south.is_full_pitch_active() and sym > 1:
            for surf in mag_surf_list:
                label_dict = decode_label(surf.label)
                # Set BC on Left side / last active surface
                if label_dict["S_id"] == Zs // sym - 1:
                    # Find the lines to add the BC
                    for line in surf.get_lines():
                        if (
                            line.prop_dict is not None
                            and COND_BOUNDARY_PROP_LAB in line.prop_dict
                            and line.prop_dict[COND_BOUNDARY_PROP_LAB] == YSML_LAB
                        ):
                            line.prop_dict.update(
                                {
                                    BOUNDARY_PROP_LAB: st
                                    + "_"
                                    + YSML_LAB
                                    + "-"
                                    + str(label_dict["R_id"])
                                }
                            )
        # Update Magnets BC when no lamination
        if self.Rint == self.Rext and self.Rint != 0:
            label_yoke = self.get_label() + "_" + LAM_LAB + YOKE_LAB
            for surf in mag_surf_list:
                label_dict = decode_label(surf.label)
                if label_dict["R_id"] == 0:
                    for line in surf.get_lines():
                        if (
                            line.prop_dict is not None
                            and COND_BOUNDARY_PROP_LAB in line.prop_dict
                            and line.prop_dict[COND_BOUNDARY_PROP_LAB] == YOKE_LAB
                        ):
                            line.prop_dict.update({BOUNDARY_PROP_LAB: label_yoke})

    # Shift to have a tooth center on Ox
    for surf in mag_surf_list:
        surf.rotate(pi / Zs)
    surf_list.extend(mag_surf_list)

    return surf_list
