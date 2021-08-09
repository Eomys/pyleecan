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

    if self.frame is None:
        Mfra = 0
    else:
        Mfra = self.frame.comp_mass()
    if self.shaft is None:
        Msha = 0
    else:
        Msha = self.shaft.comp_mass()
    Mrot = self.rotor.comp_masses()
    Msta = self.stator.comp_masses()

    Mtot = Mfra + Msha + Mrot["Mtot"] + Msta["Mtot"]

    return {"Mmach": Mtot, "Mfra": Mfra, "Msha": Msha, "Mrot": Mrot, "Msta": Msta}
