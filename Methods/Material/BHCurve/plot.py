# -*- coding: utf-8 -*-
"""@package

@date Created on Fri Apr 22 11:46:19 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from matplotlib.pyplot import subplots


def plot(self, H, f):
    """Plot the curve B(H) at the specified frequency

    Parameters
    ----------
    self : BHCurve
        a BHCurve object
    H : numpy.ndarray
        Abscissa vector [A/m] (1,N)
    f : float
        Frequency to compute the B values [Hz]

    Returns
    -------
    None
    """

    B = self.comp_B(H, f)

    fig, axes = subplots()
    axes.plot(H, B, color="r")

    axes.set_xlabel("H [A/m]")
    axes.set_ylabel("B [T]")
    axes.set_title("B(H) curve at f = " + str(f) + " Hz")
    fig.show()
