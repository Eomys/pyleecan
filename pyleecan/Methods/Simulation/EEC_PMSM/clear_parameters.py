def clear_parameters(self):
    """Clear all the parameters of an EEC_PMSM

    Parameters
    ----------
    self : EEC_PMSM
        An EEC_PMSM object
    """

    self.R1 = None
    self.Phid = None
    self.Phiq = None
    self.Phid_mag = None
    self.Phiq_mag = None
    self.Ld = None
    self.Lq = None
    self.Xkr_skinS, self.Xke_skinS = 1, 1
    self.Xkr_skinR, self.Xke_skinR = 1, 1
