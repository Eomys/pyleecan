# -*- coding: utf-8 -*-
"""@package

@date Created on Fri Apr 22 11:58:10 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import interp


def comp_B(self, H, f=None):
    """Compute the value B(H) at the specified frequency

    Parameters
    ----------
    self : BHCurveMat
        a BHCurveMat object
    H : numpy.ndarray
        Abscissa vector [A/m] (1, N)
    f : float
        Frequency to compute the B values [Hz] (Default value = None)

    Returns
    -------
    B: numpy.ndarray
        B(H) values

    """

    # Step 1 : Get the B value at the correct f
    # Find the frequency we have that is the closer to the asked one
    if f is None:
        f = self.f[0]
    f = float(f)
    tmp = abs(self.f - f)
    index = tmp.argmin()
    fobj = self.f[index]

    if fobj == f:
        # We have the B(H) value corresponding to the frequency
        B = self.matrix[:, index]
    elif fobj < f:
        if index == self.f.size - 1:
            # f is greater that the greatest f value we have
            # Return the last column
            B = self.matrix[:, -1]
        else:  # Interpolate between index and index +1
            # Barycenter coef
            a = (f - self.f[index]) / (self.f[index + 1] - self.f[index])
            B = (1 - a) * self.matrix[:, index] + a * self.matrix[:, index + 1]
    elif fobj > f:
        if index == 0:  # f is smaller that the smallest f value we have
            # Return the first column
            B = self.matrix[:, 0]
        else:  # Interpolate between index-1 and index
            # Barycenter coef
            a = (f - self.f[index - 1]) / (self.f[index] - self.f[index - 1])
            B = (1 - a) * self.matrix[:, index - 1] + a * self.matrix[:, index]

    # Step 2 : Interpolate to the given H
    return interp(x=H, xp=self.H, fp=B)
