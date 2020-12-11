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
        Volume of the Lamination (Vlam, Vvent, Vyoke, Vteeth) [m**3]

    """

    Lf = self.comp_length()  # Include radial ventilation ducts

    S_dict = self.comp_surfaces()
    Vvent = Lf * S_dict["Svent"]
    # L1 is without ventilation ducts (volume to compute masses)
    Vlam = self.L1 * S_dict["Slam"]
    Vyoke = self.L1 * S_dict["Syoke"]
    Vteeth = self.L1 * S_dict["Steeth"]
    return {"Vlam": Vlam, "Vvent": Vvent, "Vyoke": Vyoke, "Vteeth": Vteeth}
