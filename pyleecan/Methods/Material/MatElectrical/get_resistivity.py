def get_resistivity(self, T_op=None, T_ref=20):
    """Get resistivity for given temperature T_op

    Parameters
    ----------
    self : MatElectrical
        a MatElectrical object
    T_op: float
        Material operational temperature [degC]
    T_ref: float
        Material reference temperature [degC]

    Returns
    -------
    rho: float
        Electric resistivity [ohm.m]
    """

    if T_op is None:
        T_op = T_ref

    if self.rho is None:
        raise Exception("Cannot calculate resistivity if rho is None")

    # Update resistivity
    Brm = self.rho20 * (1 + self.alpha * (T_op - T_ref))

    return Brm
