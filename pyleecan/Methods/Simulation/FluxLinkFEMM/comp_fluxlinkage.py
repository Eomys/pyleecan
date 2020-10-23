# -*- coding: utf-8 -*-

from ....Functions.Electrical.comp_fluxlinkage import comp_fluxlinkage as comp_flx
from numpy import zeros, split, mean
import matplotlib.pyplot as plt


def comp_fluxlinkage(self, output):
    """Compute using FEMM the flux linkage

    Parameters
    ----------
    self : FluxLinkFEMM
        a FluxLinkFEMM object
    output : Output
        an Output object
    """

    self.get_logger().info("INFO: Compute flux linkage with FEMM")

    # store orignal currents
    Is = output.elec.Is
    Id_ref = output.elec.Id_ref
    Iq_ref = output.elec.Iq_ref

    # Set currents at 0A for the FEMM simulation
    output.elec.Is = None
    output.elec.Id_ref = 0
    output.elec.Iq_ref = 0

    # compute the fluxlinkage
    fluxdq = comp_flx(self, output)

    # flux = split(Phi_wind, 3, axis=1)
    # fig = plt.figure()
    # plt.plot(angle, flux[0], color="tab:blue", label="A")
    # plt.plot(angle, flux[1], color="tab:red", label="B")
    # plt.plot(angle, flux[2], color="tab:olive", label="C")
    # plt.plot(angle, fluxdq[0], color="k", label="D")
    # plt.plot(angle, fluxdq[1], color="g", label="Q")
    # plt.legend()
    # fig.savefig("test_fluxlink.png")

    # restore orignal currents
    output.elec.Is = Is
    output.elec.Id_ref = Id_ref
    output.elec.Iq_ref = Iq_ref

    return mean(fluxdq[0])
