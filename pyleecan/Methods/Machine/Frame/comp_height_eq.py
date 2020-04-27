# -*- coding: utf-8 -*-


def comp_height_eq(self):
    """Computation of the Frame equivalent Height for the mechanical model

    Parameters
    ----------
    self : Frame
        A Frame object

    Returns
    -------
    Hfra: float
        Equivalent Height of the Frame [m]

    """

    return self.Rext - self.Rint
