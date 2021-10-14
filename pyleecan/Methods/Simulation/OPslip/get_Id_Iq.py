from numpy import exp


def get_Id_Iq(self):
    """Return Id and Iq

    Parameters
    ----------
    self : OPslip
        An OPslip object

    Returns
    -------
    I_dict : dict
        Dict with key "Id", "Iq"
    """

    Z = self.I0 * exp(1j * self.IPhi0)
    return {"Id": Z.real, "Iq": Z.imag}
