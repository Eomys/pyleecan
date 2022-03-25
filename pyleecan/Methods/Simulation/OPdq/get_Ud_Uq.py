def get_Ud_Uq(self):
    """Return Ud and Uq

    Parameters
    ----------
    self : OPdq
        An OPdq object

    Returns
    -------
    U_dict : dict
        Dict with key "Ud", "Uq"
    """

    return {"Ud": self.Ud_ref, "Uq": self.Uq_ref}
