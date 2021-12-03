from ....Functions.Load.import_class import import_class


def build_geometry_active(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot active area in several zone
    This method assume that the active area is centered on X axis and symetrical
    Otherwise a dedicated build_geometry_active method must be provided

    Parameters
    ----------
    self : SlotUD2
        A SlotUD2 object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    is_simplified : bool
        boolean to specify if coincident lines are considered as one or different lines (Default value = False)
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : Complex
        complex for translation (Default value = 0)

    Returns
    -------
    surf_list:
        List of surface delimiting the active zone
    """

    Slot = import_class("pyleecan.Classes", "Slot")

    key = "Nrad=" + str(Nrad) + ", Ntan=" + str(Ntan)

    if self.split_active_surf_dict is not None and key in self.split_active_surf_dict:
        surf_list = [surf.copy() for surf in self.split_active_surf_dict[key]]
        Slot.set_label(self, surf_list, Nrad, Ntan, self.get_name_lam())
        return surf_list
    else:
        return Slot.build_geometry_active(
            self,
            Nrad=Nrad,
            Ntan=Ntan,
            is_simplified=is_simplified,
            alpha=alpha,
            delta=delta,
        )
