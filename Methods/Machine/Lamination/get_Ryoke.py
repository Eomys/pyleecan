# -*- coding: utf-8 -*-


def get_Ryoke(self):
    """Return the yoke lamination radius

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    Ryoke: float
        The lamination yoke radius [m]

    """

    if self.is_internal:
        return self.Rint
    else:
        return self.Rext
