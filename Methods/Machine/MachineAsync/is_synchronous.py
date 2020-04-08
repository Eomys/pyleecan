# -*- coding: utf-8 -*-


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
