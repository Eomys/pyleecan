from numpy import linspace


def comp_time(self, N0):
    """Compute the time vector
    """
    return linspace(0, 60 / N0 * self.Nrev, self.Nt_tot)
