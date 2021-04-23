# -*- coding: utf-8 -*-


def get_lam_by_label(self, label):
    """Returns the lamination by its labels. Accepted labels are 'Stator_X' and
    'Rotor_X' with X the number of the lamination starting with 0.
    For convenience also 'Stator' or 'Rotor' are allowed here to get respective first
    stator or rotor lamination.

    Parameters
    ----------
    self : Machine
        Machine object
    label : string
        label of the lamination to return

    Returns
    -------
    lam : Lamination
        Lamination with the given label
    """
    # prepare error message just in case
    err_msg = (
        f"'{label}' is not a valid input argument for label."
        + " Only 'Stator_X' or 'Rotor_X', with X the index, are accepted."
    )

    # split the label components
    lam_str = label.split("_")

    # if no index is provided append index 0
    if len(lam_str) == 1:
        label += "_0"

    # check that 'Rotor' or 'Stator' is in label
    if lam_str[0] not in ["Stator", "Rotor"]:
        raise LabelInputError(err_msg)

    # get the requested lamination index
    try:
        index = self.get_lam_list_label().index(label)
    except:
        raise LabelInputError(err_msg)

    # return requested lamination
    return self.get_lam_list(is_int_to_ext=True, key=None)[index]


class LabelInputError(Exception):
    """ """

    pass
