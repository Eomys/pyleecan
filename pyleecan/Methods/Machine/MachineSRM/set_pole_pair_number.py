def set_pole_pair_number(self, p):
    """Set the number of pole pairs of the machine

    Parameters
    ----------
    self : MachineSRM
        MachineSRM object
    p: int
        Pole pair number of the machine
    """

    # Set pole pair number for stator only
    self.stator.set_pole_pair_number(p)
