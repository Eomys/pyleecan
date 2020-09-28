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
    comp = self.field.components["x"]
    for axis in comp.axes:
        axis_dict[axis.name] = comp.get_along(axis.name)[comp.symbol].size

    axis_dict["component"] = len(self.field.components)

    return axis_dict
