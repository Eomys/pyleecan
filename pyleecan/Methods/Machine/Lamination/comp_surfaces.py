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

    # Compute notches surfaces
    Snotch = 0
    if self.notch is not None and len(self.notch) > 0:
        for notch in self.notch:
            Snotch += notch.comp_surface()
    if self.yoke_notch is not None and len(self.yoke_notch) > 0:
        self.is_internal = not self.is_internal  # To use Ryoke instead of Rbo
        for yoke_notch in self.yoke_notch:
            Snotch += yoke_notch.comp_surface()
        self.is_internal = not self.is_internal  # Revert

    return {
        "Slam": Slam - Svent - Snotch,
        "Svent": Svent,
        "Syoke": Slam,
        "Steeth": 0,
        "Sslot": 0,
        "Snotch": Snotch,
    }
