from numpy import pi, sqrt, sin, cos, sinh, cosh


def comp_coeff(self, T_op=20, T_ref=20):
    """Compute the skin effect factor on resistance for the conductors from "Design of Rotating Electrical Machines", J. Pyrhonen, second edition
    All parameters are defined p.270 / 271
    In this method, the returned value is the one from the reference divided by the frequency, as the effect of
    frequency will be taken into account in the coeff_dict

    Parameters
    ----------
    self : LossModelWinding
        a LossModelWinding object
    T_op: float
        Conductor operational temperature [degC]
    T_ref: float
        Conductor reference temperature [degC]

    Returns
    ----------
    kr_skin : float
        skin effect coeff for resistance at given frequency and temperature
    """

    conductor = self.parent.parent.machine.stator.winding.conductor

    # Compute slot average width
    slot = conductor.parent.parent.slot
    b = slot.comp_width()

    # Get number of turns in series per coil
    zt = conductor.parent.Ntcoil

    # check if wires are round or rectangular
    is_round_wire = conductor.is_round_wire()

    # conductor height
    hc0 = conductor.comp_height_wire()
    # conductor width
    bc0 = conductor.comp_width_wire()
    # Number of circumferential adjacent wires
    za = conductor.comp_nb_circumferential_wire()
    # Number of radial adjacent wires
    zp = conductor.comp_nb_radial_wire()
    # Equivalent height of conductor
    hc = zp * hc0

    # Electrical conductivity accounting for temperature increase
    sigma = conductor.cond_mat.elec.get_conductivity(T_op=T_op, T_ref=T_ref)

    # Magnetic permeability
    mu0 = 4 * pi * 1e-7
    if conductor.cond_mat.mag is None or conductor.cond_mat.mag.mur_lin is None:
        mur = 1
    else:
        mur = conductor.cond_mat.mag.mur_lin

    # reduced conductor height Eq(5.24) p.270 divided by the frequency + adding relative permeatibility
    ksi = hc * sqrt(pi * mu0 * mur * sigma * za * bc0 / b)

    if not isinstance(ksi, float):
        # Avoid numerical error with 0
        ksi[ksi == 0] = 1e-4

    # average resistance factor
    if is_round_wire:
        # Use round wire approximation Eq(5.30) p.271
        # --> kr_skin = 1 + 0.59 * ((zt ** 2 - 0.2) / 9) * ksi ** 4
        k = 0.59 * ((zt ** 2 - 0.2) / 9) * ksi ** 4
    else:
        # Use rectangular wire approximation Eq(5.29) p.271
        # --> kr_skin = 1 + (zt ** 2 - 0.2) / 9 * ksi ** 4
        k = (zt ** 2 - 0.2) / 9 * ksi ** 4

    return k
