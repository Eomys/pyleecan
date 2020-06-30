# -*- coding: utf-8 -*-


def comp_sym(self):
    """Compute the symmetry factor of the lamination

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    sym : int
        Number of symmetries of the Lamination
    is_antisym : bool
        True if an anti-symmetry is possible after the symmetries
    """

    return self.slot.Zs, False
