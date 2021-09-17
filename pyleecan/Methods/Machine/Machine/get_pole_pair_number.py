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
    is_add_id = len(lam_list) > 2

    lam_0 = lam_list.pop()
    p = lam_0.get_pole_pair_number()
    lab_0 = lam_0.get_label(is_add_id=is_add_id)

    # Get pole pair number for all laminations
    for i, lam in enumerate(lam_list):
        # Check that the pole pair number of lam is the same as the previous one
        if lam.get_pole_pair_number() != p:
            raise Exception(
                "ERROR, "
                + lam.get_label(is_add_id=is_add_id)
                + " has a different pole pair number than "
                + lab_0
            )

    return p
