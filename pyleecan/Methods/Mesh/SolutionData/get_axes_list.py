# -*- coding: utf-8 -*-
import numpy as np

from pyleecan.Functions.make_ndarray_equal import make_ndarray_equal


def get_axes_list(self, *args):
    """Get the axis of variables stored in Solution.

    Parameters
    ----------
    self : SolutionData
        an SolutionData object
    field_name : str
        name of the field to return

    Returns
    -------
    field: array
        an array of field values

    """

    # Build axis list
    ax_name = list()
    ax_size = list()

    axes = self.field.get_axes()
    for axis in axes:
        if axis.name in args or len(args) == 0:
            ax_name.append(axis.name)
            ax_size.append(axis.get_length())

    return ax_name, ax_size
