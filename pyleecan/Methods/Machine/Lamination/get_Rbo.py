# -*- coding: utf-8 -*-


def get_Rbo(self):
    """Return the bore lamination radius

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    Rbo: float
        The lamination bore radius [m]

    """

    if self.is_internal:
        return self.Rext
    else:
        return self.Rint
