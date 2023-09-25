def comp_height_active(self):
    """Compute the height of the active area

    Parameters
    ----------
    self : SlotM18_2
        A SlotM18_2 object

    Returns
    -------
    Hwind: float
        Height of the active area [m]
    """

    return self.Hmag_bore + self.Hmag_gap
