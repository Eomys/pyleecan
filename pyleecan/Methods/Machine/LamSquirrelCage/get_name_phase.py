def get_name_phase(self):
    """Return the name of the winding phases

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    name_phase: list
        Empty list

    """
    if (
        not hasattr(self, "winding")
        or self.winding is None
        # or self.winding.conductor is None
    ):
        return list()
    return ["Bar " + str(ii + 1) for ii in range(self.winding.qs)]
