def comp_width(self):
    """Compute the average width of the Slot by dividing its surface by its height

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    W2: float
        Average width of the slot [m]
    """

    S = self.comp_surface()

    H = self.comp_height()

    return S / H
