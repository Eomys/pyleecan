from numpy import exp


def comp_parameters(self):
    """Compute the parameters of the equivalent electrical circuit:
    resistance, inductance according to OP/T

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object
    machine : Machine
        a Machine object
    OP : OP
        an OP object
    Tsta : float
        Average stator temperature
    Trot : float
        Average rotor temperature
    """

    # Check that OP and temperature are set
    assert self.OP is not None
    assert self.Tsta is not None

    # Update skin effect
    self.comp_skin_effect()

    # Compute winding transformation ratios
    if self.K21I is None:
        self.comp_K21()

    # Compute stator winding resistance
    if self.R1 is None:
        self.comp_R1()

    # Compute stator winding inductance
    if self.L1 is None:
        self.comp_L1()

    # Iron loss resistance
    if self.Rfe is None:
        self.Rfe = 1e12  # TODO calculate (or estimate at least)

    # Compute rotor winding resistance
    if self.R2 is None:
        self.comp_R2()

    # Compute rotor winding inductance
    if self.L2 is None:
        self.comp_L2()

    # check if inductances have to be calculated
    if self.Phi_m is None or self.I_m is None:
        raise Exception("Phi_m and I_m must be enforced for EEC_SCIM")
