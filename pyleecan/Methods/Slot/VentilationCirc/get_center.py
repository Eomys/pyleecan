# -*- coding: utf-8 -*-

from numpy import exp, pi


def get_center(self):
    """Return a list of the center of the ventilations

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object

    Returns
    -------
    Zc_list: list
        List of list of center complex coordinates

    """

    Zc_list = list()

    for ii in range(self.Zh):
        Zc = self.H0 * exp(1j * self.Alpha0) * exp(ii * 1j * 2 * pi / self.Zh)
        Zc_list.append(Zc)

    return Zc_list
