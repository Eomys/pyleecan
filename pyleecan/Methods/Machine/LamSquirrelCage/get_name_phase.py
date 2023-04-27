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
    qs = 3 if self.winding.qs is None else self.winding.qs

    return ["Bar " + str(ii + 1) for ii in range(qs)]
