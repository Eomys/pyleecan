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
    return self.ref_element.interpolation(
        point=point, node_coord=node_coord, field=field
    )
