# -*- coding: utf-8 -*-

from ....Functions.Electrical.comp_fluxlinkage import comp_fluxlinkage as comp_flx
from numpy import mean


def comp_inductance(self, output):
    """Compute using FEMM the inductance

    Parameters
    ----------
    self : IndMagFEMM
        an IndMagFEMM object
    output : Output
        an Output object
    """

    self.get_logger().info("INFO: Compute dq inductances with FEMM")

    # compute the fluxlinkage
    fluxdq = comp_flx(self, output)

    return (mean(fluxdq[0]), mean(fluxdq[1]))
