# -*- coding: utf-8 -*-
import numpy as np


def get_axis(self, args=None):
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

    axis_dict = dict()
    size_mat = np.size(self.field)
    k = 0
    for ax in self.axis:
        axis_dict[ax] = size_mat[k]
        k = k + 1

    return axis_dict
