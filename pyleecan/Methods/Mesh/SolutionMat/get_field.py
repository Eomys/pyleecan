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
    if args is None:
        args = dict()

    field = self.field
    if self.axis is not None:
        for key in self.axis:
            ax = np.where(np.array(field.shape) == self.axis[key])[0][0]
            if key in args:
                ind = args[key]
                field = np.take(field, indices=ind, axis=ax)

    return field
