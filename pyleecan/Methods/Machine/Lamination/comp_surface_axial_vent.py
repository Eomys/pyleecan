# -*- coding: utf-8 -*-


def comp_surface_axial_vent(self):
    """Compute the Lamination axial vent

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    Svent: float
        Surface of the Lamination's axial ventilation [m**2]

    """

    if len(self.axial_vent) > 0:
        return sum([vent.comp_surface() for vent in self.axial_vent])
    else:
        return 0
