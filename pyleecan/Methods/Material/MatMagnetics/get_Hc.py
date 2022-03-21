from numpy import pi


def get_Hc(self, T_op=None, T_ref=20):
    """Get magnetic excitation coercitivity

    Parameters
    ----------
    self : MatMagnetics
        a MatMagnetics object
    T_op: float
        Material operational temperature [degC]
    T_ref: float
        Material reference temperature [degC]

    Returns
    -------
    Hc: float
        Magnetic excitation coercitivity

    """

    if T_op is None:
        T_op = T_ref

    # Calculate magnetic coercitivity at 20 degC from remanent flux density
    if self.Brm20 is None or self.mur_lin is None:
        raise Exception("Cannot calculate Hc if Brm20 or mur_lin is None")

    # Magnet coercitivity
    Hc20 = self.Brm20 / (4 * pi * 1e-7 * self.mur_lin)

    # Update magnetic coercitivity
    Hc = Hc20 * (1 + self.alpha_Br * (T_op - T_ref))

    return Hc
