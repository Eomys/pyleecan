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
        Lamination surface dictionary (Slam, Svent, Syoke, Steeth, Sslot) [m**2]

    """
    if self.is_internal:
        ext_shape = self.bore
        int_shape = self.yoke
    else:
        ext_shape = self.yoke
        int_shape = self.bore

    # Surface of the external disk
    if ext_shape is not None:
        S_ext = ext_shape.comp_surface()
    else:
        S_ext = (self.Rext ** 2) * pi
    # Surface of the internal disk
    if int_shape is not None:
        S_int = int_shape.comp_surface()
    else:
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

    return {
        "Slam": Slam - Svent - Snotch,
        "Svent": Svent,
        "Syoke": Slam,
        "Steeth": 0,
        "Sslot": 0,
        "Snotch": Snotch,
    }
