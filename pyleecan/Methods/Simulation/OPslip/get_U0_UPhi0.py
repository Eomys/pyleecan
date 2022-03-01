def get_U0_UPhi0(self):
    """Return U0 and UPhi0
    Parameters
    ----------
    self : OPdq
        An OPdq object
    Returns
    -------
    U_dict : dict
        Dict with key "U0", "UPhi0"
    """

    return {"U0": self.U0_ref, "UPhi0": self.UPhi0_ref}