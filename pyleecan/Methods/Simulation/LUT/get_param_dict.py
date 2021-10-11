def get_param_dict(self):
    """Get the parameters dict from ELUT

    Parameters
    ----------
    self : ELUT
        an ELUT object

    Returns
    ----------
    param_dict : dict
        a Dict object
    """

    param_dict = {"R1": self.R1, "L1": self.L1, "T1_ref": self.T1_ref}

    return param_dict
