from ....Functions.labels import WIND_LAB


def set_label(self, surf_list, Nrad, Ntan, lam_label):
    """Set the normalized label on the active surface
    (internal method of build_geometry_active)

    Parameters
    ----------
    self : Slot
        A Slot object
    surf_list : [Surface]
        List of split active surface of the winding (for one slot)
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangential layer
    lam_label : str
        Label of the lamination containing the slot
    """

    index = 0
    for jj in range(Ntan):
        for ii in range(Nrad):
            surf_list[index].label = (
                lam_label + "_" + WIND_LAB + "_R" + str(ii) + "-T" + str(jj) + "-S0"
            )
            index += 1
