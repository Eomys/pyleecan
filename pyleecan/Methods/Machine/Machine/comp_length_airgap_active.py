# -*- coding: utf-8 -*-


def comp_length_airgap_active(self):
    """Compute the airgap active length

    Parameters
    ----------
    self : Machine
        A Machine object

    Returns
    -------
    Lgap: float
        Airgap active length [m]

    """

    return min(self.rotor.L1, self.stator.L1)
