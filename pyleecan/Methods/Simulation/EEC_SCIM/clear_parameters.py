def clear_parameters(self):
    """Clear all the parameters of an EEC_SCIM

    Parameters
    ----------
    self : EEC_SCIM
        An EEC_SCIM object
    """

    self.R1 = None
    self.R2 = None
    self.L1 = None
    self.L2 = None
    self.K21Z = None
    self.K21I = None
    self.Lm_table = None
    self.Im_table = None
    self.Xkr_skinS, self.Xke_skinS = 1, 1
    self.Xkr_skinR, self.Xke_skinR = 1, 1
