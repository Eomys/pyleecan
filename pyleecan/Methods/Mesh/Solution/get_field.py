# -*- coding: utf-8 -*-
import numpy as np


def get_field(self, field_name):
    """Get the value of variables stored in Solution.

     Parameters
     ----------
     self : Solution
         an Solution object
     field_name : str
         name of the field to return

     Returns
     -------
     field: array
         an array of field values

     """

    field = None

    for key in self.nodal:
        if key == field_name:
            field = self.nodal[key]

    if field is None:
        for key in self.edge:
            if key == field_name:
                field = self.edge[key]

    if field is None:
        for key in self.face:
            if key == field_name:
                field = self.face[key]

    if field is None:
        for key in self.volume:
            if key == field_name:
                field = self.volume[key]

    return field
