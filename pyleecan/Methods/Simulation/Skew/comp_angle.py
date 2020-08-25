# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError
from numpy import pi, linspace, floor, finfo, concatenate, flip, unique
from scipy.interpolate import interp1d


def comp_angle(self, L, Z):
    """Compute skew angles  
    
    Parameters
    ----------
    self : Skew
        a Skew object
    L : float
        lamination length
    Z : int
        number of slots

    Returns
    -------
    angle_list : list
        list of skew angles
    index_list : list
        list of indices to avoid redundant computations
    """

    Nslices = self.Nslices
    rate = self.rate
    eps = finfo(float).eps

    if self.type == "linear":
        gamma = rate * 2 * pi / Z / L
        alphaf = L * gamma
        dalpha = alphaf / Nslices
        angle_list = linspace(
            -alphaf / 2 + dalpha / 2, alphaf / 2 - dalpha / 2, Nslices
        )
    elif self.type == "step":
        Nsegm = self.Nsegm
        try:
            alphaf = rate * 2 * pi / Z
            dalpha = alphaf / Nslices
            np = 500
            if self.is_stator:
                alpha_th = (
                    floor(linspace(0, L - eps, np) / (L / Nsegm)) * alphaf / (Nsegm - 1)
                    - alphaf / 2
                )
            else:
                alpha_th = (
                    floor(linspace(0, L - eps, np) / (L / Nsegm)) * alphaf / (Nsegm - 1)
                )
            f = interp1d(linspace(0, alphaf, np), alpha_th)
            angle_list = f(linspace(dalpha / 2, alphaf - dalpha / 2, Nslices))
        except InputError as error:
            error("Nsegm must be >0. Input Nsegm: " + str(Nsegm))
    elif self.type == "vshape":
        Nsegm = self.Nsegm
        try:
            alphaf = rate * 2 * pi / Z
            np = 500
            dalpha = alphaf / Nslices
            if Nslices % 2 == 0:
                alpha_th = (
                    floor(
                        linspace(0, 0.5 * L - eps, int(np / 2))
                        / (0.5 * L / (0.5 * Nsegm))
                    )
                    * alphaf
                    / (0.5 * Nsegm - 1)
                    - alphaf / 2
                )
                alpha_th = concatenate((alpha_th, flip(alpha_th)))
                f = interp1d(linspace(0, alphaf, np), alpha_th)
                angle_list = f(linspace(dalpha / 2, alphaf - dalpha / 2, Nslices))
            else:
                alpha_th = (
                    floor(linspace(0, 0.5 * L, int(np / 2)) / (0.5 * L / (0.5 * Nsegm)))
                    * alphaf
                    / (0.5 * Nsegm - 1)
                    - alphaf / 2
                )
                alpha_th = concatenate((alpha_th, flip(alpha_th)))
                f = interp1d(linspace(0, alphaf, np), alpha_th)
                angle_list = f(linspace(dalpha / 2, alphaf - dalpha / 2, Nslices))
        except InputError as error:
            error("Nsegm must be >0. Input Nsegm: " + str(Nsegm))
    elif self.type == "user-defined":
        alphaf = L / 2
        dalpha = L / Nslices
        try:
            angle_list = self.curve(
                linspace(-alphaf + dalpha / 2, alphaf - dalpha / 2, Nslices)
            )
        except InputError as error:
            error("Error in skew curve definition")
    else:
        raise InputError("Unknown skew type: " + self.type)

    # Find repeated angles
    (angles, indices) = unique(angle_list, return_inverse=True)

    self.angle_list = angle_list.tolist()
    self.index_list = indices.tolist()
