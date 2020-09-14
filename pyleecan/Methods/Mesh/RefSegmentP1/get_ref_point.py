# -*- coding: utf-8 -*-

import numpy as np


def get_ref_point(self, vertice, point):
    """ Return the coordinate of the equivalent point in the ref cell

    Parameters
    ----------
    self : RefSegmentP1
        a RefSegmentP1 object
    vertice : ndarray
        vertice of the cell
    point : ndarray
        coordinates of a point

        Returns
    -------
    pt1_ref : ndarray
        coordinates of the ref point
    """

    point_ref = np.array([0, 0], dtype=float)
    point_decal = np.array([-1, 0], dtype=float)

    pt1 = point[0:2] - vertice[0, :]
    pt2 = vertice[1, :] - vertice[0, :]
    rho2 = np.sqrt(pt2[0] ** 2 + pt2[1] ** 2)
    phi2 = np.arctan2(pt2[1], pt2[0])
    Trot = np.array([[np.cos(phi2), np.sin(phi2)], [-np.sin(phi2), np.cos(phi2)]])

    pt1_ref = 2 * np.dot(Trot, pt1) / rho2 + point_decal
    # pt2_ref =np.dot(Trot, pt2) / rho2 - point_decal

    return pt1_ref
