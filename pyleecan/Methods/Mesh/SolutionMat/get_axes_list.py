# -*- coding: utf-8 -*-
import numpy as np


def get_axis_list(self):
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

    return self.axis_name, self.axis_size
