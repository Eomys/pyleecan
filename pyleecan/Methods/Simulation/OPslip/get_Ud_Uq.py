from numpy import exp


def get_Ud_Uq(self):
    """Return Ud and Uq

    Parameters
    ----------
    self : OPslip
        An OPslip object

    Returns
    -------
    U_dict : dict
        Dict with key "Ud", "Uq"
    """

    Z = self.U0 * exp(1j * self.UPhi0)
    return {"Ud": Z.real, "Uq": Z.imag}
