# -*- coding: utf-8 -*-


def get_pole_pair_number(self):
    """Returns the number of pole pairs of the machine

    Parameters
    ----------
    self : Machine
        Machine object

    Returns
    -------
    p: int
        Pole pair number of the machine
    """

    # Get list of laminations
    lam_list = self.get_lam_list()

    p = lam_list.pop().get_pole_pair_number()

    # Get pole pair number for all laminations
    for i, lam in enumerate(lam_list):
        # Check that the pole pair number of lam is the same as the previous one
        if lam.get_pole_pair_number() != p:
            raise Exception(
                "ERROR, lamination "
                + str(i + 1)
                + " has a different pole pair number than lamination 0"
            )

    return p
