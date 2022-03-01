from numpy import angle, pi


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

    if self.Ud_ref is None or self.Uq_ref is None:
        return {"U0": None, "UPhi0": None}

    else:
        Z = self.Ud_ref + 1j * self.Uq_ref
        return {"U0": abs(Z), "UPhi0": angle(Z) % (2 * pi)}