# -*- coding: utf-8 -*-

import numpy as np


def interpolate(
    self, point: np.ndarray, node_coord: np.ndarray, field: np.ndarray
) -> np.ndarray:
    """Return interpolated value of the field in a element

    Parameters
    ----------
    self : ElementMat
         an ElementMat object
    points : ndarray
        evaluation points
    node_coord : ndarray
        coordinates of the element nodes
    field : ndarray
        field to interpolate

    Returns
    -------
    value: array
        interpolated field

    """
    # TODO: input only single point
    point_ref = self.ref_element.get_ref_point(node_coord, point)

    # TODO: input only multiple points
    values_ref, _ = self.ref_element.shape_function(point_ref)

    interp_func = np.tensordot(values_ref, field, axes=([2], [0]))

    return interp_func
