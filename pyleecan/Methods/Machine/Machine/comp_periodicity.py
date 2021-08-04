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
    p = self.get_pole_pair_number()

    # Get stator (anti)-periodicity in spatial domain only (because stator is not moving regarding time)
    pera_s, is_antipera_s, _, _ = self.stator.comp_periodicity()
    pert_s = p  # Force polarity as time periodicity
    is_antipert_s = True  # Force anti-periodicity (pure sine current)

    # Get rotor (anti)-periodicities both in time and spatial domains
    pera_r, is_antipera_r, pert_r, is_antipert_r = self.rotor.comp_periodicity(p=p)

    # Get machine time and spatial periodicities
    pera = gcd(gcd(pera_s, pera_r), p)
    pert = gcd(gcd(pert_s, pert_r), p)

    # Get machine time and spatial anti-periodicities
    is_apera = is_antipera_s and is_antipera_r
    is_apert = is_antipert_s and is_antipert_r

    return int(pera), is_apera, int(pert), is_apert