# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Nov 29 17:20:16 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""


def get_machine_type(self):
    """Return a string with the may information about the machine architecture

    Parameters
    ----------
    self : MachineSyRM
        A MachineSyRM object

    Returns
    -------
    type_str: str
        SyRM Zs/Zr/p (int/ext rotor)

    """

    type_str = "SyRM "
    if self.stator.slot.Zs is not None:
        type_str += str(self.stator.slot.Zs) + "s / "
    else:
        type_str += "?s / "

    if self.stator.winding.p is not None:
        type_str += str(self.stator.winding.p) + "p"
    else:
        type_str += "?p"

    if self.stator.is_internal:
        type_str += " (ext rotor)"
    else:
        type_str += " (int rotor)"

    return type_str
