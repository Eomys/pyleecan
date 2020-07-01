# -*- coding: utf-8 -*-
import numpy as np


def set_field(self, field_value, field_name, field_type):
    """Set the value of variables stored in Solution.

     Parameters
     ----------
     self : Solution
         an Solution object
     field_value : array
         an array of field value
    field_value : str
         the name of the variable corresponding to field_value

     Returns
     -------
     """

    if field_type is "nodal":
        self.nodal[field_name] = field_value
    elif field_type is "edge":
        self.edge[field_name] = field_value
    elif field_type is "face":
        self.face[field_name] = field_value
    elif field_type is "volume":
        self.volume[field_name] = field_value
