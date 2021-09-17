# -*- coding: utf-8 -*-


def get_pole_pair_number(self):
    """Returns the number of pole pairs of the machine

    Parameters
    ----------
    self : MachineSRM
        MachineSRM object

    Returns
    -------
    p: int
        Pole pair number of the machine
    """

    return self.rotor.get_Zs()
