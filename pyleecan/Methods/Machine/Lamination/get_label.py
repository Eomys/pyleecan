from ....Functions.labels import STATOR_LAB, ROTOR_LAB, STATOR_LAB_S, ROTOR_LAB_S
from ....Methods import ParentMissingError


def get_label(self, is_add_id=True, is_short=False):
    """Return the label of the lamination (Stator-0 for instance)

    Parameters
    ----------
    self : Lamination
        a Lamination object
    is_add_id : bool
        True to add the "-X" part
    is_short : bool
        True to return the short version of the label

    Returns
    -------
    label : str
        Label of the lamination

    """

    if self.is_stator and is_short:
        label = STATOR_LAB_S
    elif self.is_stator and not is_short:
        label = STATOR_LAB
    elif not self.is_stator and is_short:
        label = ROTOR_LAB_S
    else:
        label = ROTOR_LAB

    if is_add_id:
        if self.parent is not None:
            try:
                lam_list = self.parent.get_lam_list(is_int_to_ext=True, key=label)
                label += "-" + str(lam_list.index(self))
            except:
                pass
        # else:
        #     raise ParentMissingError("Error: The slot is not inside a Lamination")

    return label
