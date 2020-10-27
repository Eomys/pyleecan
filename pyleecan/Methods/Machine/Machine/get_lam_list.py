# -*- coding: utf-8 -*-


def get_lam_list(self, is_int_to_ext=True):
    """Returns the ordered list of lamination of the machine

    Parameters
    ----------
    self : Machine
        Machine object
    is_int_to_ext : bool
        true to order the list from the inner lamination to the extrenal one

    Returns
    -------
    lam_list : list
        Ordered lamination list, for abstract Machine objects list will be empty
    """
    lam_list = []
    if hasattr(self, "lam_list"):
        lam_list = self.lam_list
        # Sort by Rint by assuming the lamination are not colliding
    else:
        if hasattr(self, "stator"):
            lam_list.append(self.stator)
        if hasattr(self, "rotor"):
            lam_list.append(self.rotor)

    return sorted(lam_list, key=lambda x: x.Rint, reverse=not is_int_to_ext)
