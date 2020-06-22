# -*- coding: utf-8 -*-
import numpy as np


def get_field(self, field_name, j_t0=None):
    """Get the value of variables stored in Solution.

     Parameters
     ----------
     self : Solution
         an Solution object
     field_name : str
         name of the field to return

     Returns
     -------
     field: ndarray
         an ndarray of field values

     """

    if field_name == self.label:
        if j_t0 is None:
            return self.field
        else:
            return self.field[j_t0, :]
    else:
        return None
