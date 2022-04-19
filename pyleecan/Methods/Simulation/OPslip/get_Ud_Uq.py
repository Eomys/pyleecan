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

    if self.UPhi0_ref is None:
        UPhi0_ref = 0
    else:
        UPhi0_ref = self.UPhi0_ref

    Z = self.U0_ref * exp(1j * UPhi0_ref)

    return {"Ud": Z.real, "Uq": Z.imag}
