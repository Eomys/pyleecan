# -*- coding: utf-8 -*-

import numpy as np


def interpolation(self, point, vertice, field):
    """ Return interpolated value of the field in a cell

    Parameters
     ----------
    self : RefCell
         an RefCell object
    points : ndarray
        evaluation points
    nb_pt : int
        nb of evaluation points
    vertice : ndarray
        vertices of the cell
    field : ndarray
        field to interpolate

     Returns
     -------
     value: array
         interpolated field

     """

    point_ref = self.ref_cell.get_ref_point(point, vertice)
    [values_ref, size] = self.ref_cell.shape_function(point_ref)

    value = np.dot(values_ref, field)

    return value
