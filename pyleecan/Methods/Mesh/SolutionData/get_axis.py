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
    for axis in self.field.axes:
        axis_dict[axis.name] = self.field.get_along(axis.name)[self.field.symbol]

    return axis_dict
