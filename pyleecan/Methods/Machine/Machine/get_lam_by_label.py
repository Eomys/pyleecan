from ....Functions.labels import STATOR_LAB, ROTOR_LAB, ROTOR_LAB_S, STATOR_LAB_S


def get_lam_by_label(self, label):
    """Returns the lamination by its labels. Accepted labels are 'Stator-X' and
    'Rotor-X' with X the number of the lamination starting with 0.
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
        + " Only 'Stator-X' or 'Rotor-X', with X the index, are accepted."
    )

    # Short=>Label conversion
    if STATOR_LAB not in label and ROTOR_LAB not in label:
        label = label.replace(ROTOR_LAB_S, ROTOR_LAB)
        label = label.replace(STATOR_LAB_S, STATOR_LAB)

    # split the label components
    lam_str = label.split("-")

    # if no index is provided append index 0
    if len(lam_str) == 1:
        label += "-0"

    # check that 'Rotor' or 'Stator' is in label
    if lam_str[0] not in [STATOR_LAB, ROTOR_LAB]:
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
