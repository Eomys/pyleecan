# -*- coding: utf-8 -*-
"""@package Methods.Machine.Lamination.comp_surface_axial_vent
Compute the axial vent of the Lamination surface
@date Created on Thu Nov 08 17:09:42 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


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
