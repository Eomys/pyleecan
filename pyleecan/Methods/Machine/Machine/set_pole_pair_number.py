def set_pole_pair_number(self, p):
    """Set the number of pole pairs of the machine

    Parameters
    ----------
    self : Machine
        Machine object
    p: int
        Pole pair number of the machine
    """

    # Set pole pair number for all laminations
    for lam in self.get_lam_list(is_int_to_ext=None):
        try:
            lam.set_pole_pair_number(p)
        except Exception as e:
            raise Exception(
                "Cannot enforce pole pair number to lamination "
                + lam.get_label()
                + ":\n"
                + str(e)
            )
