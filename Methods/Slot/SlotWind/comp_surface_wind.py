# -*- coding: utf-8 -*-


def comp_surface_wind(self):
    """Compute the Slot winding surface (by numerical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotWind
        A SlotWind object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    surf = self.build_geometry_wind(Nrad=1, Ntan=1)

    return surf[0].comp_surface()
