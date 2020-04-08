# -*- coding: utf-8 -*-

from pyleecan.Methods import NotImplementedYetError


def get_dim_wind(self):
    """Get the two first dimension of the winding matrix

    Parameters
    ----------
    self : WindingCW1L
        A WindingCW1L object

    Returns
    -------
    (Nrad, Ntan): tuple
        Number of layer in radial and tangential direction

    """

    return (1, 1)
