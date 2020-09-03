# -*- coding: utf-8 -*-
import numpy as np


def get_field(self, args=None):
    """Get the value of variables stored in Solution.

     Parameterss
     ----------
     self : Solution
         an Solution object
     args : dict
         dict of selected entries (not used)

     Returns
     -------
     field: ndarray
         an ndarray of field values

     """

    return self.field
