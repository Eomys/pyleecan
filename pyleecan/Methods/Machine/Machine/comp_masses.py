# -*- coding: utf-8 -*-


def comp_masses(self):
    """Compute the masses of the machine
    - Mmach : Mass total [kg]
    - Mfra : Mass of the Frame [kg]
    - Msha : Mass of the Shaft [kg]
    - Mrot : Mass dictionary of the rotor masses
    - Msta : Mass dictionary of the stator masses

    Parameters
    ----------
    self : Machine
        A Machine object

    Returns
    -------
    M_dict: dict
        A dictionary of the Machine's masses (Mmach, Msha,
        Mfra, Mrot, Msta) [kg]

    """

    M_dict = dict()
    if self.frame is None:
        M_dict["Frame"] = 0
    else:
        M_dict["Frame"] = self.frame.comp_mass()

    if self.shaft is None:
        M_dict["Shaft"] = 0
    else:
        M_dict["Shaft"] = self.shaft.comp_mass()

    Mlam = 0
    for lam in self.get_lam_list():
        M = lam.comp_masses()
        M_dict[lam.get_label()] = M
        Mlam += M["Mtot"]

    Mtot = M_dict["Frame"] + M_dict["Shaft"] + Mlam
    M_dict["All"] = Mtot
    return M_dict
