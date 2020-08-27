# -*- coding: utf-8 -*-


def is_synchronous(self):
    """Return if a machine is synchronous or not

    Parameters
    ----------
    self : MachineUD
        A MachineUD

    Returns
    -------
    is_synchronous: bool
        User Defined machine are synchronous according to is_sync

    """
    return self.is_sync
