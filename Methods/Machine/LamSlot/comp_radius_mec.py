# -*- coding: utf-8 -*-


def comp_radius_mec(self):
    """Compute the mechanical radius of the Lamination [m]

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

    Returns
    -------
    Rmec: float
        Mechanical radius [m]

    """

    if self.is_internal:
        return self.Rext
    else:
        return self.Rint
