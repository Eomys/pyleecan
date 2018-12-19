# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Aug 18 10:27:08 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""


def get_machine_type(self):
    """Return a string with the may information about the machine architecture

    Parameters
    ----------
    self : MachineSIPMSM
        A MachineSIPMSM object

    Returns
    -------
    str
        type_str: SPMSM/IPMSM Zs/p (int/ext rotor)

    """

    if self.type_machine == 6:
        type_str = "SPMSM "
    elif self.type_machine == 7:
        type_str = "IPMSM "

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
