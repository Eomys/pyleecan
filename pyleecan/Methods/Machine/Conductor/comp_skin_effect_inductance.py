from numpy import pi, sqrt, sin, cos, sinh, cosh


def comp_skin_effect_inductance(self, bc, b4, h4, zt, freq, T_op=20, T_ref=20):
    """Compute the skin effect factor on inductance for the conductors from "Design of Rotating Electrical Machines", J. Pyrhonen, second edition
    All parameters bc, h4, z4, are defined in Fig(4.14) p.249

    Parameters
    ----------
    self : Conductor
        an Conductor object
    bc: float
        Conductor width [m]
    b4: float
        Slot width [m]
    h4: float
        Slot height [m]
    zt: int
        Number of radial adjacent conductors
    freq: float
        electrical frequency [Hz]
    T_op: float
        Conductor operational temperature [degC]
    T_ref: float
        Conductor reference temperature [degC]

    Returns
    ----------
    kl_skin : float
        skin effect coeff for inductance at given frequency and temperature
    """

    # Electrical conductivity accounting for temperature increase
    sigma = self.cond_mat.elec.get_conductivity(T_op=T_op, T_ref=T_ref)

    # Magnetic permeability
    mu0 = 4 * pi * 1e-7
    mur = self.cond_mat.mag.mur_lin
    if mur is None:
        mur = 1

    # Electrical pulsation
    w = 2 * pi * freq

    # reduced conductor height Eq(4.90) p.257 + addind relative permeatibility
    ksi = h4 * sqrt(w * mu0 * mur * sigma * bc / (2 * b4))

    # resistance factor function phi prime Eq(4.92) p.257
    phip = (
        3 / (2 * ksi) * (sinh(2 * ksi) - sin(2 * ksi)) / (cosh(2 * ksi) - cos(2 * ksi))
    )

    # resistance factor function psi prime Eq(4.91) p.257
    psip = 1 / ksi * (sinh(ksi) + sin(ksi)) / (cosh(ksi) + cos(ksi))

    # average resistance factor  Eq(4.91) p.257
    kl_skin = phip / zt ** 2 + ((zt ** 2 - 1) / zt ** 2) * psip

    return kl_skin
