def comp_polynoms(self):
    """Abstract method to store polynoms functions

    Parameters
    ----------
    self: Subdomain
        a Subdomain object

    Returns
    ----------
    var: type
        var description
    """

    return


def E(n, r, R):
    return (r / R) ** n - (R / r) ** n


def P(n, r, R):
    return (r / R) ** n + (R / r) ** n
