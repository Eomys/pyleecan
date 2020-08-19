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

    zp = output.simu.machine.stator.get_pole_pair_number()
    felec = output.elec.felec
    omega = 2 * pi * felec / zp

    P = output.elec.Pem_av_ref
    losses = output.elec.Pj_losses
    Tem_av_ref = (P - losses) / omega

    output.elec.Tem_av_ref = Tem_av_ref
