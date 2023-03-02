# -*- coding: utf-8 -*-

from ....Functions.labels import STATOR_LAB, ROTOR_LAB, STATOR_LAB_S, ROTOR_LAB_S


def get_lam_list(self, is_int_to_ext=True, key=None):
    """Returns the ordered list of lamination of the machine

    Parameters
    ----------
    self : Machine
        Machine object
    is_int_to_ext : bool
        true to order the list from the inner lamination to the extrenal one
    key : string
        keyword to return only stator or rotor laminations, accepted values are "Stator" or "Rotor" default None to return all

    Returns
    -------
    lam_list : list
        Ordered lamination list, for abstract Machine objects list will be empty
    """
    # Extract all laminations
    lam_list = []
    if hasattr(self, "lam_list"):
        lam_list = self.lam_list
    else:
        if hasattr(self, "stator"):
            lam_list.append(self.stator)
        if hasattr(self, "rotor"):
            lam_list.append(self.rotor)

    # Sort all laminations according to Rint by assuming the lamination are not colliding
    if is_int_to_ext is not None:
        lam_list = sorted(lam_list, key=lambda x: x.Rint, reverse=not is_int_to_ext)

    # Filter the lamination according to key
    if key is not None:
        if key in [STATOR_LAB, STATOR_LAB_S]:
            is_stator = True
        elif key in [ROTOR_LAB, ROTOR_LAB_S]:
            is_stator = False
        else:
            raise KeyInputError(
                f"'{key}' is not a valid input argument for key (only 'Stator' or 'Rotor' accepted for now)"
            )

        lam_list = [lam for lam in lam_list if lam.is_stator is is_stator]

    return lam_list


class KeyInputError(Exception):
    """ """

    pass
