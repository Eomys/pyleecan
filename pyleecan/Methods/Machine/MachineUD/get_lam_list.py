# -*- coding: utf-8 -*-


def get_lam_list(self, is_int_to_ext=True):
    """Returns the ordered list of lamination of the machine

    Parameters
    ----------
    self : MachineUD
        MachineUD object
    is_int_to_ext : bool
        true to order the list from the inner lamination to the extrenal one

    Returns
    -------
    lam_list : list
        Ordered lamination list
    """

    lam_list = self.lam_list

    # Sort by Rint by assuming the lamination are not colliding
    return sorted(lam_list, key=lambda x: x.Rint, reverse=not is_int_to_ext)
