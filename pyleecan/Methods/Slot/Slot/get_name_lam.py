from ....Methods import ParentMissingError


def get_name_lam(self):
    """Return the name of the parent lamination

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    name: string
        The name of the parent lamination

    """

    if self.parent is not None:
        if self.get_is_stator():
            name = "Stator"
        else:
            name = "Rotor"
        return name
    else:
        return "NoLam"
