# -*- coding: utf-8 -*-


def comp_sym(self):
    """Compute the symmetry factor of the lamination

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

    Returns
    -------
    sym : int
        Number of symmetries of the Lamination
    is_antisym : bool
        True if an anti-symmetry is possible after the symmetries
    """

    return self.get_Zs(), False
