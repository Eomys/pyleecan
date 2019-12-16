# -*- coding: utf-8 -*-
import numpy as np


def set_field(self, field_value, field_name):
    """Set the value of variables stored in SolutionFEMM.

     Parameters
     ----------
     self : SolutionFEMM
         an SolutionFEMM object
     field_value : array
         an array of field value
    field_value : str
         the name of the variable corresponding to field_value

     Returns
     -------
     """

    if field_name is "B":
        self.B = field_value
    elif field_name is "H":
        self.H = field_value
    elif field_name is "mu":
        self.mu = field_value
