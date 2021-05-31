def set_pole_pair_number(self, p):
    """Set the number of pole pairs of the machine

    Parameters
    ----------
    self : Machine
        Machine object
    p: int
        Pole pair number of the machine
    """

    # Get list of laminations
    lam_list = self.get_lam_list()

    # Get pole pair number for all laminations
    for i, lam in enumerate(lam_list):

        if hasattr(lam, "set_pole_pair_number"):
            # Set the pole pair number of lam
            lam.set_pole_pair_number(p)

        else:
            raise Exception(
                "ERROR, cannot enforce pole pair number to lamination " + str(i + 1)
            )