# -*- coding: utf-8 -*-
import numpy as np


def get_axis(self):
    """Get the value of variables stored in Solution.

     Parameters
     ----------
     self : SolutionMat
         an SolutionMat object

     Returns
     -------
     axis_dict: dict
         a dict of axis names containing axis sizes

     """

    return self.axis
