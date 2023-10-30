from ....Methods import ParentMissingError


def get_label(self, is_add_id=True):
    """Return the label of the lamination (Stator-0 for instance)

    Parameters
    ----------
    self : Notch
        a Notch object
    is_add_id : bool
        True to add the "-X" part

    Returns
    -------
    label : str
        Label of the lamination

    """

    if self.parent is not None:
        return self.parent.get_label()
    else:
        raise ParentMissingError("Error: The notch is not inside a Lamination")
