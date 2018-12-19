# -*- coding: utf-8 -*-
"""@package

@date Created on Tue Aug 23 14:44:15 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""


def is_synchronous(self):
    """Return if a machine is synchronous or not

    Parameters
    ----------
    self : MachineAsync
        A MachineAsync

    Returns
    -------
    is_synchronous: bool
        Asynchronous machines are not synchronous

    """
    return False
