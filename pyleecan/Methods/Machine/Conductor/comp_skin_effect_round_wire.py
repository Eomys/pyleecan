# -*- coding: utf-8 -*-
import numpy as np


def comp_skin_effect_round_wire(self, f, rho=None, mu=None):

    """Compute skin effect factor for round wires


    Parameters
    ----------
    Inputs:
    f: float
        Frequency (Hz)
    rho: float
        Resistivity of wire material (Ohm meter)
    mu: float
        Relative permeability of wire material
    self : Conductor
        an Conductor object

    Outputs:
    K_R: float
        Skin effect resistance factor of round wires

    K_I: float
        Skin effect inductance factor of round wires
    """

    # Resistivity of wire material (Ohm meter)
    if rho is None:
        rho = self.cond_mat.elec.rho
    # Wire diameter
    d_w = self.Wwire
    # Vaccum or air permeability
    mu0 = 4 * np.pi * 1e-7
    # Wire material magnetic permeability (mu*mu0)
    if mu is None:
        mu = self.cond_mat.mag.mur_lin * mu0
    else:
        mu = mu * mu0
    # Thickness of skin
    delta = np.sqrt(rho / (np.pi * f * mu))

    """
    cf. SKIN EFFECT, PROXIMITY EFFECT AND THE RESISTANCE OF CIRCULAR AND RECTANGULAR
    CONDUCTORS, page 6

    """
    # # factor of skin effect (R_AC=R_DC*K)
    # K_R = 0.25*(d_w)**2/(d_w*delta-delta**2)

    """
    cf. A simple derivation for the skin effect in a round wire, page 8-9 eqa 30-31

    """
    # Radius of wire
    r_w = d_w / 2

    # Resistance factor of skin effect (R_AC=R_DC*K)
    K_R = 1 + 1 / 48(r_w / delta) ** 4
    # Inductance factor of skin effect (I_AC=I_DC*K)
    K_I = 1 - 1 / 96(r_w / delta) ** 4

    return K_R, K_I
