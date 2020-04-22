# -*- coding: utf-8 -*-

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
