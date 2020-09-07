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
    # if args is None:
    #    args = dict()

    # along_arg = list()
    # comp = list(self.field.components.values())[0]
    # for axis in comp.axes:
    #     if axis.name in args:
    #         along_arg.append(axis.name + "[" + str(args[axis.name]) + "]")
    #     else:
    #         along_arg.append(axis.name)
    #
    #
    # field = self.field.get_along_xyz(tuple(along_arg))[self.field.symbol]
    comp = dict()
    j = 0
    for key in self.field.components:
        comp[j] = self.field.components[key].values
        j = j + 1

    s = comp[0].shape
    vector = np.zeros(np.append(s, j))

    j = 0
    for key in self.field.components:
        vector[..., j] = comp[j]
        j = j + 1

    return vector
