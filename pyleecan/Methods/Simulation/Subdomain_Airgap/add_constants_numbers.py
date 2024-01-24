def add_constants_numbers(self, csts_number):
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

    csts_number.extend([self.k.size, self.k.size, self.k.size, self.k.size])
