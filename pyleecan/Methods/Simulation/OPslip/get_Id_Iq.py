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

    if self.IPhi0_ref is None:
        IPhi0_ref = 0
    else:
        IPhi0_ref = self.IPhi0_ref

    Z = self.I0_ref * exp(1j * IPhi0_ref)

    return {"Id": Z.real, "Iq": Z.imag}
