from numpy import inf


def get_conductivity(self, T_op=None, T_ref=20):
    """Get conductivity for given temperature T_op

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
    sigma: float
        Electric conductivity [S]
    """

    if T_op is None:
        T_op = T_ref

    if self.rho is None:
        raise Exception("Cannot calculate conductivity if rh0 is None")

    if self.rh0 == 0:
        sigma = inf

    else:
        rho = self.get_resistivity(T_op, T_ref)
        sigma = 1 / rho

    return sigma
