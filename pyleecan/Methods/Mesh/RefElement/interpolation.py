# -*- coding: utf-8 -*-

import numpy as np


def interpolation(
    self, point: np.ndarray, node_coord: np.ndarray, field: np.ndarray
) -> np.ndarray:
    """Return interpolated value of the field in a element

    Parameters
    ----------
    self : Interpolation
         an Interpolation object
    point : ndarray
        evaluation point
    node_coord : ndarray
        coordinates of the element nodes
    field : ndarray
        field to interpolate

    Returns
    -------
    value: array
        interpolated field

    """

    point_ref = self.get_ref_point(node_coord, point)
    values_ref, _ = self.shape_function(point_ref)

    interp_func = np.tensordot(values_ref, field, axes=([2], [0]))

    return interp_func
