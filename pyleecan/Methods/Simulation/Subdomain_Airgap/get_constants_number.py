def get_constants_number(self):
    """Return the number of integration constants in airgap subdomain

    Parameters
    ----------
    self: Subdomain_Airgap
        a Subdomain_Airgap object

    Returns
    ----------
    nb_const: int
        Number of integration constants in airgap subdomain
    """

    return 4 * self.k.size
