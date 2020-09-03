# -*- coding: utf-8 -*-
import numpy as np


def get_axis(self, args=None):
    """Get the axis of variables stored in Solution.

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

    axis_dict = dict()

    along_arg = list()
    comp = self.field.components["x"]

    for axis in comp.axes:
        along_arg.append(axis.name)

    field = comp.get_along(tuple(along_arg))[comp.symbol]

    ## HOTFIX: Remove for next SCIDATATOOL release
    if self.parent.parent.Nt_tot == 1:
        field = field[np.newaxis, :]

    size_field = field.shape

    k = 0
    for ax in along_arg:
        axis_dict[ax] = size_field[k]
        k = k + 1

    axis_dict["component"] = len(self.field.components)

    return axis_dict
