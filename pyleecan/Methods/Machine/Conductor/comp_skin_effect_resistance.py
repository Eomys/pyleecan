from numpy import pi, sqrt, sin, cos, sinh, cosh


def comp_skin_effect_resistance(self, freq, T_op=20, T_ref=20, b=None, zt=None):
    """Compute the skin effect factor on resistance for the conductors from "Design of Rotating Electrical Machines", J. Pyrhonen, second edition
    All parameters are defined p.270 / 271

    Parameters
    ----------
    self : Conductor
        an Conductor object
    b: float
        Slot width [m]
    zt: int
        Number of turns in series per coil
    freq: float or ndarray
        electrical frequency [Hz]
    T_op: float
        Conductor operational temperature [degC]
    T_ref: float
        Conductor reference temperature [degC]

    Returns
    ----------
    kr_skin : float
        skin effect coeff for resistance at given frequency and temperature
    """

    if b is None:
        # Compute slot average width
        slot = self.parent.parent.slot
        b = slot.comp_width()

    if zt is None:
        # Get number of turns in series per coil
        zt = self.parent.Ntcoil

    # check if wires are round or rectangular
    is_round_wire = self.is_round_wire()

    # conductor height
    hc0 = self.comp_height_wire()
    # conductor width
    bc0 = self.comp_width_wire()
    # Number of circumferential adjacent wires
    za = self.comp_nb_circumferential_wire()
    # Number of radial adjacent wires
    zp = self.comp_nb_radial_wire()
    # Equivalent height of conductor
    hc = zp * hc0

    # Electrical conductivity accounting for temperature increase
    sigma = self.cond_mat.elec.get_conductivity(T_op=T_op, T_ref=T_ref)

    # Magnetic permeability
    mu0 = 4 * pi * 1e-7
    if self.cond_mat.mag is None or self.cond_mat.mag.mur_lin is None:
        mur = 1
    else:
        mur = self.cond_mat.mag.mur_lin

    # Electrical pulsation
    w = 2 * pi * freq

    # reduced conductor height Eq(5.24) p.270 + adding relative permeatibility
    ksi = hc * sqrt((1 / 2) * w * mu0 * mur * sigma * za * bc0 / b)

    if not isinstance(ksi, float):
        # Avoid numerical error with 0
        ksi[ksi == 0] = 1e-4

    # average resistance factor
    if is_round_wire:
        # Use round wire approximation Eq(5.28) p.271
        kr_skin = 1 + 0.59 * ((zt ** 2 - 0.2) / 9) * ksi ** 2
    else:
        # resistance factor function phi Eq(5.26) p.271
        phi = ksi * (sinh(2 * ksi) + sin(2 * ksi)) / (cosh(2 * ksi) - cos(2 * ksi))

        # resistance factor function psi Eq(5.27) p.271
        psi = 2 * ksi * (sinh(ksi) - sin(ksi)) / (cosh(ksi) + cos(ksi))

        kr_skin = phi + ((zt ** 2 - 1) / 3) * psi  # Eq(5.28) p.271
        # kr_approx = 1 + (zt ** 2 - 0.2) / 9 * ksi ** 4  # Eq(5.29) p.271

    return kr_skin
