# -*- coding: utf-8 -*-


def get_machine_type(self):
    """Return a string with the may information about the machine architecture

    Parameters
    ----------
    self : MachineDFIM
        A MachineDFIM object

    Returns
    -------
    type_str: str
        DFIM Zs/Zr/p (int/ext rotor)

    """

    type_str = "DFIM "

    if self.stator.slot.Zs is not None:
        type_str += str(self.stator.slot.Zs) + "s / "
    else:
        type_str += "?s / "

    if self.rotor.slot.Zs is not None:
        type_str += str(self.rotor.slot.Zs) + "r / "
    else:
        type_str += "?r / "

    if self.stator.winding.p is not None:
        type_str += str(self.stator.winding.p) + "p"
    else:
        type_str += "?p"

    if self.stator.is_internal:
        type_str += " (ext rotor)"
    else:
        type_str += " (int rotor)"

    return type_str
