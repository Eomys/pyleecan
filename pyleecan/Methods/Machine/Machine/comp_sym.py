# -*- coding: utf-8 -*-
from math import gcd


def comp_sym(self):
    """Compute the symmetry factor of the machine

    Parameters
    ----------
    self : Machine
        A Machine object

    Returns
    -------
    sym : int
        Number of symmetries of the Machine
    is_antisym : bool
        True if an anti-symmetry is possible after the symmetries
    """

    sym_s, is_antisym_s = self.stator.comp_sym()
    sym_r, is_antisym_r = self.rotor.comp_sym()

    return gcd(sym_s, sym_r), is_antisym_s and is_antisym_r
