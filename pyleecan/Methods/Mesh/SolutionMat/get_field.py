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
        nb_axis = len(self.axis_name)
        for i in range(nb_axis):
            ax = np.where(np.array(field.shape) == self.axis_size[i])[0][0]
            ax_name = self.axis_name[i]

            if ax_name in args:
                ind = args[ax_name]
                field = np.take(field, indices=ind, axis=ax)

    return field
