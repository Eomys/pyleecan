# -*- coding: utf-8 -*-

import numpy as np


def get_ref_point(self, vertice, point):
    """Return the coordinate of the equivalent point in the ref element

    Parameters
    ----------
    self : RefSegmentP1
        a RefSegmentP1 object
    vertice : ndarray
        vertice of the element
    point : ndarray
        coordinates of a point

        Returns
    -------
    pt1_ref : ndarray
        coordinates of the ref point
    """

    # Coordinate of the element node shift to the origin
    elem_node_origin = vertice[1] - vertice[0]

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
    point_in_ref_elem = np.dot(mat_rot, point - vertice[0]) / elem_lenght

    return point_in_ref_elem
