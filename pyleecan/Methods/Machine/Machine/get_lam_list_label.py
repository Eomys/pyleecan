# -*- coding: utf-8 -*-
from ....Functions.labels import STATOR_LAB, ROTOR_LAB


def get_lam_list_label(self):
    """Returns the ordered (from internal to external) list of lamination labels
    corresponding to machine.get_lam_list(is_int_to_ext=True, key=None)

    Parameters
    ----------
    self : Machine
        Machine object

    Returns
    -------
    label_list : list
        Ordered lamination list, for abstract Machine objects list will be empty
    """

    lam_list = self.get_lam_list(is_int_to_ext=True, key=None)

    label_list = []
    IDs = 0
    IDr = 0
    for lam in lam_list:
        if lam.is_stator:
            label_list.append(STATOR_LAB + "-" + str(IDs))
            IDs += 1
        else:
            label_list.append(ROTOR_LAB + "-" + str(IDr))
            IDr += 1

    return label_list
