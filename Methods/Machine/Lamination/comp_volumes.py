# -*- coding: utf-8 -*-
"""@package Methods.Machine.Lamination.comp_volumes
Lamination computation the volume methods
@date Created on Thu Jan 29 13:20:03 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi


def comp_volumes(self):
    """Compute the volumes of the Lamination

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    V_dict: dict
        Volume of the Lamination (Vlam, Vvent) [m**3]

    """

    Lf = self.comp_length()  # Include radial ventilation ducts

    S_dict = self.comp_surfaces()
    Vvent = Lf * S_dict["Svent"]
    Vlam = self.L1 * S_dict["Slam"]
    return {"Vlam": Vlam, "Vvent": Vvent}
