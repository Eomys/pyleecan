def has_key(self):
    """Check if a there is key in the notch

    Parameters
    ----------
    self : Notch
        A Notch object

    Returns
    -------
    has_key : bool
        True if the notch has a key
    """

    return self.key_mat is not None
