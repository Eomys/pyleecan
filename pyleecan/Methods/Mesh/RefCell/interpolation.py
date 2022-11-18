# -*- coding: utf-8 -*-

import numpy as np


def interpolation(self, point, vertice, field):
    """Return interpolated value of the field in a cell

    Parameters
    ----------
    self : Interpolation
         an Interpolation object
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

    point_ref = self.get_ref_point(vertice, point)  # TODO: input only single point
    [values_ref, size] = self.shape_function(
        point_ref, 1
    )  # TODO: input only multipel points

    interp_func = np.tensordot(values_ref, field, axes=([2], [0]))

    return interp_func
