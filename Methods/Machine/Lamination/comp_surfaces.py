# -*- coding: utf-8 -*-
"""@package Methods.Machine.Lamination.comp_surfaces
Lamination computation of all surfaces method
@date Created on Mon Jan 12 17:09:42 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

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
        Lamination surface dictionnary (Slam, Svent) [m**2]

    """

    # Surface of the external disk
    S_ext = (self.Rext ** 2) * pi
    # Surface of the internal disk
    S_int = (self.Rint ** 2) * pi
    # Surface of lamination without hole
    Slam = S_ext - S_int

    # Surface of the ventilation ducts on the yoke
    Svent = self.comp_surface_axial_vent()

    return {"Slam": Slam - Svent, "Svent": Svent}
