# -*- coding: utf-8 -*-
import numpy as np


def get_field(self, args=None):
    """Get the value of variables stored in Solution.

    Parameters
    ----------
    self : Solution
        an Solution object
    field_name : str
        name of the field to return

    Returns
    -------
    field: array
        an array of field values

    """
    if args is None:
        args = dict()

    along_arg = list()
    for axis in self.field.axes:
        if axis.name in args:
            along_arg.append(axis.name + "[" + str(args[axis.name]) + "]")
        else:
            along_arg.append(axis.name)

    field = self.field.get_along(tuple(along_arg))[self.field.symbol]

    ## HOTFIX: Remove for next SCIDATATOOL release
    if self.parent.parent.Nt_tot == 1:
        field = field[np.newaxis, :]

    return field
