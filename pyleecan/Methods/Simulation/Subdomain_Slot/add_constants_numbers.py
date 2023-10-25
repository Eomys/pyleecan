def add_constants_numbers(self, csts_number):
    """Method description

    Parameters
    ----------
    self: Subdomain_Slot
        a Subdomain_Slot object
    csts_number: list
        List of constants number

    """

    csts_number.extend([self.number_per_a, self.number_per_a * self.k.size])
