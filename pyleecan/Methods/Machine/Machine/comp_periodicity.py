# -*- coding: utf-8 -*-
from math import gcd


def comp_periodicity(self):
    """Compute the (anti)-periodicities of the machine in time and space domain

    Parameters
    ----------
    self : Machine
        A Machine object

    Returns
    -------
    per : int
        Number of periodicities of the machine
    is_antisym : bool
        True if an anti-periodicity is possible after the periodicities
    """
    # Get stator (anti)-periodicity in spatial domain only (because stator is not moving regarding time)
    pera_s, is_antipera_s, _, _ = self.stator.comp_periodicity()

    # Get rotor (anti)-periodicities both in time and spatial domains
    pera_r, is_antipera_r, pert_r, is_antipert_r = self.rotor.comp_periodicity()

    return (gcd(pera_s, pera_r), is_antipera_s and is_antipera_r, pert_r, is_antipert_r)
