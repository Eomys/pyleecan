# -*- coding: utf-8 -*-

from ....Methods import NotImplementedYetError


def get_dim_wind(self):
    """Get the two first dimension of the winding matrix

    Parameters
    ----------
    self : WindingUD
        A WindingUD object

    Returns
    -------
    (Nrad, Ntan): tuple
        Number of layer in radial and tangential direction

    """

    return self.user_wind_mat.shape[0:2]
