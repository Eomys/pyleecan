# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the Trapeze surface

    Parameters
    ----------
    self : Trapeze
        A Trapeze object

    Returns
    -------
    surf: float
        The Trapeze surface [m**2]

    """

    return self.height * (self.W2 + self.W1) / 2
