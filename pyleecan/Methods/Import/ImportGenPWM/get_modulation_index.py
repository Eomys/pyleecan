from numpy import sqrt


def get_modulation_index(self):
    """Function to compute the carrier

    Parameters
    ----------
    self : ImportGenPWM
        an ImportGenPWM object

    Returns
    -------
    M_I: float
        Modulation index

    """

    if self.U0 is None:
        raise Exception("Cannot calculate modulation index if self.U0 is None")

    if self.Vdc1 is None:
        raise Exception("Cannot calculate modulation index if self.Vdc1 is None")

    return 2 * sqrt(2) * self.U0 / self.Vdc1
