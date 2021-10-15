# -*- coding: utf-8 -*-

from numpy import array, pi
from scipy.linalg import solve


def solve_EEC(self):
    """Compute the parameters dict for the analytical equivalent electrical circuit
    cf "Influence of the Number of Pole Pairs on the Audible
    Noise of Inverter-Fed Induction Motors: Radial
    Force Waves and Mechanical Resonances"
    I. P. Tsoumas, H. Tischmacher, B. Eichinger

    Parameters
    ----------
    self : EEC_ANL
        an EEC_ANL object
    Return
    ------
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in EEC
    """

    f = self.freq0
    ws = 2 * pi * f
    PAR = self.parameters

    out_dict = dict()

    # Solve system
    if "Ud" in PAR:  # Voltage driven
        out_dict["Id"] = PAR["Ud"] / (1j * ws * PAR["Ld"])
        out_dict["Iq"] = PAR["Uq"] / (1j * ws * PAR["Lq"])
        out_dict["Ud"] = PAR["Ud"]
        out_dict["Uq"] = PAR["Uq"]
    else:  # Current Driven
        out_dict["Ud"] = PAR["Id"] * (1j * ws * PAR["Ld"])
        out_dict["Uq"] = PAR["Iq"] * (1j * ws * PAR["Lq"])
        out_dict["Id"] = PAR["Id"]
        out_dict["Iq"] = PAR["Iq"]

    return out_dict
