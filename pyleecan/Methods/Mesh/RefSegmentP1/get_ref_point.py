# -*- coding: utf-8 -*-

import numpy as np


def get_ref_point(
    self, element_coordinate: np.ndarray, point: np.ndarray
) -> np.ndarray:
    """Return the coordinate of the equivalent point in the ref element (-1,0) -- (1,0)

    Parameters
    ----------
    self : RefSegmentP1
        a RefSegmentP1 object
    element_coordinate : ndarray
        coordinates of the element
    point : ndarray
        coordinates of a point

        Returns
    -------
    pt1_ref : ndarray
        coordinates of the ref point
    """

    # Coordinate of the element node shift to the origin
    elem_node_origin = element_coordinate[1] - element_coordinate[0]

    # Compute angle and norm of the element
    elem_lenght = np.linalg.norm(elem_node_origin)
    elem_angle = np.arctan2(elem_node_origin[1], elem_node_origin[0])

    # Create rotation matrix to rotate the element on the x-axis
    mat_rot = np.array(
        [
            [np.cos(elem_angle), np.sin(elem_angle)],
            [-np.sin(elem_angle), np.cos(elem_angle)],
        ]
    )

    # ref_elem_node =  np.dot(mat_rot, elem_node_origin) / elem_lenght

    # Assume that the element is in the same plane with constant z
    point_in_ref_elem = (
        np.dot(mat_rot, point[:2] - element_coordinate[0]) / elem_lenght
    )  # (0,0) -- (1,0)
    point_in_ref_elem[0] *= 2  # (0,0) -- (2,0)
    point_in_ref_elem[0] -= 1  # (-1,0) -- (1,0)

    return point_in_ref_elem
