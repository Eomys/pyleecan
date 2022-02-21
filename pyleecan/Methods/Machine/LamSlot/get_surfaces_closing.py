from numpy import pi
from ....Functions.labels import update_RTS_index


def get_surfaces_closing(self, sym=1):
    """Return the surfaces needed to close the radii of the Lamination

    Parameters
    ----------
    self : LamSlot
        A LamSlot object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    -------
    surf_list : list
        List of the closing surfaces
    """

    if not hasattr(self.slot, "get_surface_opening"):
        return list()
    else:
        close_list = list()
        slot_pitch = 2 * pi / self.slot.Zs
        # for slot to draw
        for ii in range(self.slot.Zs // sym):
            slot_surf = self.slot.get_surface_opening(
                alpha=slot_pitch * ii + slot_pitch * 0.5
            )
            for jj, surf in enumerate(slot_surf):
                # Adapt the label
                surf.label = update_RTS_index(
                    label=surf.label, R_id=None, T_id=jj, S_id=ii
                )
                close_list.append(surf)

        return close_list
