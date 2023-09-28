from numpy import pi
from ....Functions.labels import update_RTS_index
from ....Classes.Lamination import Lamination


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

    # Get notches closing surfaces
    close_list = Lamination.get_surfaces_closing(self=self, sym=sym)
    if not hasattr(self.slot, "get_surface_opening"):
        return close_list
    else:  # Get slot closing surfaces (no surface if wedges)
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
