# -*- coding: utf-8 -*-

import numpy as np


def get_field(self, args=None):
    """Get the value of variables stored in Solution.

    Parameters
    ----------
    self : SolutionData
        an SolutionData object

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
            if isinstance(args[axis.name], int):
                along_arg.append(axis.name + "[" + str(args[axis.name]) + "]")
            else:
                along_arg.append(axis.name + str(args[axis.name]))
        else:
            along_arg.append(axis.name)

    field = self.field.get_along(tuple(along_arg))[self.field.symbol]

    all_ax = self.get_axis()
    pos = 0
    for i in all_ax:
        if all_ax[i] == 1:
            field = field[..., np.newaxis]
            field = np.moveaxis(field, -1, pos)
        pos = pos + 1

    return field
