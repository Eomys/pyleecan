def get_I0_Phi0(self):
    """Return I0 and Phi0

    Parameters
    ----------
    self : OPslip
        An OPslip object

    Returns
    -------
    I_dict : dict
        Dict with key "I0", "Phi0"
    """

    return {"I0": self.I0_ref, "Phi0": self.IPhi0_ref}
