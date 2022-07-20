from numpy import angle, pi


def get_I0_Phi0(self):
    """Return I0 and Phi0

    Parameters
    ----------
    self : OPdq
        An OPdq object

    Returns
    -------
    I_dict : dict
        Dict with key "I0", "Phi0"
    """
    if self.Id_ref is None or self.Iq_ref is None:
        return {"I0": None, "Phi0": None}
    else:
        Z = self.Id_ref + 1j * self.Iq_ref
        return {"I0": abs(Z), "Phi0": angle(Z) % (2 * pi)}
