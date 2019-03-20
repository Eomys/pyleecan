# -*- coding: utf-8 -*-
"""@package Methods.Machine.Lamination.comp_masses
Lamination computation of masses method
@date Created on Thu Jan 29 13:27:57 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_masses(self):
    """Compute the masses of the Lamination

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    M_dict: dict
        Lamination mass dictionnary (Mtot, Mlam) [kg]

    """
    rho = self.mat_type.struct.rho
    V_dict = self.comp_volumes()

    M_dict = dict()
    M_dict["Mlam"] = V_dict["Vlam"] * self.Kf1 * rho
    M_dict["Mtot"] = M_dict["Mlam"]

    return M_dict
