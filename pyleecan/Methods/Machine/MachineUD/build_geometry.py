# -*- coding: utf-8 -*-


def build_geometry(self, sym=1, alpha=0, delta=0):
    """Build the geometry of the machine

    Parameters
    ----------
    self : MachineUD
        MachineUD object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination

    """
    surf_list = list()

    if self.frame is not None:
        surf_list.extend(self.frame.build_geometry(sym=sym, alpha=alpha, delta=delta))

    for lam in self.lam_list:
        surf_list.extend(lam.build_geometry(sym=sym, alpha=alpha, delta=delta))

    if self.shaft is not None:
        surf_list.extend(self.shaft.build_geometry(sym=sym, alpha=alpha, delta=delta))

    return surf_list
