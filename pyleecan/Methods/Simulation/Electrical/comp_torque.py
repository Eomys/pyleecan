# -*- coding: utf-8 -*-

from numpy import pi


def comp_torque(self, output):
    """Compute the electrical average torque

    Parameters
    ----------
    self : Electrical
        an Electrical object
    output : Output
        an Output object
    """

    N0 = output.elec.OP.get_N0()
    omega = 2 * pi * N0 / 60

    P = output.elec.Pem_av_ref
    losses = output.elec.Pj_losses  # TODO update since there may also be other losses

    Tem_av_ref = (P - losses) / omega

    output.elec.Tem_av_ref = Tem_av_ref
