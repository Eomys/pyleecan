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

    # Get pole pair number for all laminations
    for i, lam in enumerate(lam_list):
        if i == 0:
            p = lam.get_pole_pair_number()
        else:
            p_i = lam.get_pole_pair_number()

            # Check that the pole pair number of lam is the same as the previous one
            if p_i != p:
                raise Exception(
                    "ERROR, lamination "
                    + str(i)
                    + "has a different pole pair number than the others"
                )

    return p
