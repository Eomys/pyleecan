# -*- coding: utf-8 -*-


def get_dim_wind(self):
    """Get the two first dimension of the winding matrix

    Parameters
    ----------
    self : Winding
        A Winding object

    Returns
    -------
    (Nrad, Ntan): tuple
        Number of layer in radial and tangential direction

    """

    return self.wind_mat.shape[0:2]
