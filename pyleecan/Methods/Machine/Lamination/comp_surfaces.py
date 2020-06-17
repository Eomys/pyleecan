# -*- coding: utf-8 -*-

from numpy import pi


def comp_surfaces(self):
    """Compute the Lamination surface (Total, Vent).

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    S_dict: dict
        Lamination surface dictionnary (Slam, Svent, Syoke, Steeth, Sslot) [m**2]

    """

    # Surface of the external disk
    S_ext = (self.Rext ** 2) * pi
    # Surface of the internal disk
    S_int = (self.Rint ** 2) * pi
    # Surface of lamination without hole
    Slam = S_ext - S_int

    # Surface of the ventilation ducts on the yoke
    Svent = self.comp_surface_axial_vent()

    return {
        "Slam": Slam - Svent,
        "Svent": Svent,
        "Syoke": Slam,
        "Steeth": 0,
        "Sslot": 0,
    }
