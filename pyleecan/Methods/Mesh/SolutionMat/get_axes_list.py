# -*- coding: utf-8 -*-
import numpy as np


def get_axes_list(self):
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

    return self.axis_name.copy(), self.axis_size.copy()
