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

    param_dict = {"Rs": self.Rs, "Ls": self.Ls, "Tsta_ref": self.Tsta_ref}

    return param_dict
