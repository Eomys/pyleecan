# -*- coding: utf-8 -*-
import numpy as np


def get_axes_list(self, *args):
    """Get the value of variables stored in Solution.

    Parameters
    ----------
    self : SolutionMat
        an SolutionMat object

    Returns
    -------
    axis_dict: list
        a list of axis names containing axis sizes

    """

    if self.axis_name is not None:
        axis_name = self.axis_name.copy()
    else:
        axis_name = None

    if self.axis_size is not None:
        axis_size = self.axis_size.copy()
    else:
        axis_size = None

    return axis_name, axis_size
