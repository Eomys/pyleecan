def get_constants_number(self):
    """Method description

    Parameters
    ----------
    self: Subdomain_SlotOpening
        a Subdomain_SlotOpening object

    Returns
    ----------
    var: type
        var description
    """

    return self.number_per_a * (self.k.size + 2 + 2 * self.v.size)
