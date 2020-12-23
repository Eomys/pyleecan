# -*- coding: utf-8 -*-


def get_lam_index(self, label):
    """Returns list index of the lamination with the given label
    corresponding to machine.get_lam_list(is_int_to_ext=True, key=None).
    For convienence label 'Stator' or 'Rotor' are allowed here to get respective first
    stator or rotor lamination.

    Parameters
    ----------
    self : Machine
        Machine object

    label : str
        Label of the lamination

    Returns
    -------
    index : int
        List index of the lamination, if label doesn't exists index is None
    """
    # get list of lamination labels
    labels = self.get_lam_list_label()

    # if no index is provided with label append index 0
    if len(label.split("_")) == 1:
        label += "_0"

    # check if label exists
    if label in labels:
        return labels.index(label)
    else:
        return None
