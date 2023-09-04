from numpy import pi

from ....Classes.LamSlot import LamSlot
from ....Functions.labels import update_RTS_index
from ....Functions.labels import (
    BOUNDARY_PROP_LAB,
    COND_BOUNDARY_PROP_LAB,
    WIND_LAB,
    YSMR_LAB,
    YSML_LAB,
    decode_label,
)


def build_geometry(self, sym=1, alpha=0, delta=0, is_circular_radius=False):
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
    is_circular_radius : bool
        True to add surfaces to "close" the Lamination radii

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination

    """
    # getting the Lamination surface
    surf_lam = LamSlot.build_geometry(
        self, sym=sym, alpha=alpha, delta=delta, is_circular_radius=is_circular_radius
    )
    surf_list = list()
    if self.slot is not None and self.slot.Zs != 0:
        # getting number of slot
        Zs = self.slot.Zs
        # getting angle between Slot
        slot_pitch = 2 * pi / Zs
        # getting Nrad and Ntan
        if self.winding is None or self.winding.conductor is None:
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
                alpha=alpha,
                delta=delta,
            )

        st = self.get_label()
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
                new_surf = surf.copy()
                # changing the slot reference number
                new_surf.label = update_RTS_index(
                    label=surf.label, S_id=ii, surf_type_label=WIND_LAB
                )
                new_surf.rotate(ii * slot_pitch)
                surf_list.append(new_surf)
        # Update the winding BC (if winding side matches sym lines ex: SlotM18)
        if self.slot.is_full_pitch_active() and sym > 1:
            for surf in surf_list:
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
        # Add wedges if any
        if self.slot.wedge_mat is not None:
            wedge_list = self.slot.get_surface_wedges()
            for ii in range(Zs // sym):  # for each slot
                # for each wedges surface in the slot
                for surf in wedge_list:
                    new_surf = type(surf)(init_dict=surf.as_dict())
                    # changing the slot reference number
                    new_surf.label = update_RTS_index(label=surf.label, S_id=ii)
                    new_surf.rotate(ii * slot_pitch)
                    surf_list.append(new_surf)
        # Shift to have a tooth center on Ox
        for surf in surf_list:
            surf.rotate(pi / Zs)

    surf_list = surf_lam + surf_list

    return surf_list
