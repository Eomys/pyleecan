def get_constants_number(self):
    """Method description

    Parameters
    ----------
    self: Subdomain_Slot
        a Subdomain_Slot object

    Returns
    ----------
    var: type
        var description
    """

    return self.number_per_a * (1 + self.k.size)
