# -*- coding: utf-8 -*-
"""@package

@date Created on Fri Apr 22 11:58:56 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import sqrt


def comp_B(self, H, f=None):
    """Compute the value B(H) at the specified frequency

    Parameters
    ----------
    self : BHCurveParam
        a BHCurveParam object
    H : numpy.ndarray
        Abscissa vector [A/m]
    f : float
        Frequency to compute the B values [Hz] (unused) (Default value = None)

    Returns
    -------
    B: numpy.ndarray
        B(H) values

    """

    mur_0 = self.mur_0
    mur_1 = self.mur_1
    Bmax = self.Bmax
    a = self.a

    Ha = mur_0 * H * (mur_0 - 1) / Bmax

    return mur_0 * mur_1 * H + Bmax * (
        Ha + 1 - sqrt((Ha + 1) ** 2 - 4 * Ha * (1 - a))
    ) / (2 * (1 - a))
