from ....Functions.labels import STATOR_LAB, ROTOR_LAB
from ....Methods import ParentMissingError


def get_label(self, is_add_id=True):
    """Return the label of the lamination (Stator-0 for instance)

    Parameters
    ----------
    self : Lamination
        a Lamination object
    is_add_id : bool
        True to add the "-X" part

    Returns
    -------
    label : str
        Label of the lamination

    """

    if self.is_stator:
        label = STATOR_LAB
    else:
        label = ROTOR_LAB

    if is_add_id:
        if self.parent is not None:
            lam_list = self.parent.get_lam_list(is_int_to_ext=True, key=label)
            label += "-" + str(lam_list.index(self))
        # else:
        #     raise ParentMissingError("Error: The slot is not inside a Lamination")

    return label
