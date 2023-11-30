# -*- coding: utf-8 -*-
from numpy import array, linspace, pi
import numpy as np
from scipy.optimize import curve_fit, root_scalar


def fit_model(self, BH):
    """
    Fit the BH model parameters based on input B(H) curve of the material, and perform extrapolation.

    Parameters
    ----------
    self : ModelBH
        a ModelBH object
    BH: numpy.ndarray
        B(H) input values
    Bmax: float
        Maximum B value required
    Hmax: float
        Maximum H value required

    Returns
    -------
    new_BH: numpy.ndarray
        B(H) values (two colums matrix: H and B(H))

    """
    Bmax = self.Bmax
    Hmax = self.Hmax

    H = BH[:, 0]
    B = BH[:, 1]

    # Find the optimum parameter for curve fitting
    popt, _ = curve_fit(self.BH_func, H, B, p0=array([self.param1, self.param2]))

    param1 = popt[0]
    param2 = popt[1]

    self.param1 = param1
    self.param2 = param2

    # Idea to use scipy to find Hmax corresponding to Bmax
    # def Langevin_root(H):
    #     B = Bs * (np.cosh(H / a) / np.sinh(H / a) - a / H)
    #     return B - self.Bmax_extrapolate

    # x1 = BH[-1, 0]*(2 - BH[-2, 0]/BH[-1, 0])
    # x0 = BH[-1, 0]
    # Hmax = root_scalar(Langevin_root, x0=x0, x1=x1)

    # Hmax is defined from Bmax if it exists
    if Bmax is not None:
        delta = H[-1] * 0.01
        Hmax = H[-1]
        iteration = 0
        new_B = B[-1]
        while new_B < Bmax and iteration < 1000:
            Hmax += delta
            iteration += 1
            new_B = self.BH_func(Hmax, param1, param2)

    # Either imposed from method call or calculated from Bmax
    if Hmax is not None:
        added_H = np.linspace(H[-1], Hmax, iteration)
        new_H = np.hstack((H, added_H))
        new_B = self.BH_func(new_H, param1, param2)

        new_BH = np.zeros((len(new_H), 2))
        new_BH[:, 0] = new_H
        new_BH[:, 1] = new_B

    # Last special case: the BH curve is recalculated from the initial H values (then it is not an extrapolation, but a smoothing of the data based on the analytical model)
    else:
        new_B = self.BH_func(H, Bs, a)

    return new_BH
