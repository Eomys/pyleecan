def get_Id_Iq(self):
    """Return Id and Iq

    Parameters
    ----------
    self : OPdq
        An OPdq object

    Returns
    -------
    I_dict : dict
        Dict with key "Id", "Iq"
    """

    return {"Id": self.Id_ref, "Iq": self.Iq_ref}
