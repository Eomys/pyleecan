def comp_temperature_effect(self, T_op, T_ref=20):
    """Compute the temperature effect factor for the conductor

    Parameters
    ----------
    self : Conductor
        an Conductor object
    T_op: float
        Conductor operational temperature [degC]
    T_ref: float
        Conductor reference temperature [degC]

    Returns
    ----------
    Tfact : float
        temperature effect coeff for resistance at T_op
    """

    alphasw = self.cond_mat.elec.alpha
    Tfact = 1 + alphasw * (T_op - T_ref)

    return Tfact
