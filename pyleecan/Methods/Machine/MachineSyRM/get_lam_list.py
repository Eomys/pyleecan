# -*- coding: utf-8 -*-


def get_lam_list(self, is_int_to_ext=True):
    """Returns the ordered list of lamination of the machine

    Parameters
    ----------
    self : MachineSyRM
        MachineSyRM object
    is_int_to_ext : bool
        true to order the list from the inner lamination to the extrenal one

    Returns
    -------
    lam_list : list
        Ordered lamination list
    """
    if self.rotor.is_internal:
        In = self.rotor
        Ext = self.stator
    else:
        In = self.stator
        Ext = self.rotor

    if is_int_to_ext:
        return [In, Ext]
    else:
        return [Ext, In]
