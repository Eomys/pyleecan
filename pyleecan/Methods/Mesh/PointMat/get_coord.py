# -*- coding: utf-8 -*-

import numpy as np


def get_coord(self, point_tags):
    """Return the coordinates of point(s).

     Parameters
     ----------
     self : PointMat
         an PointMat object
     point_tags : np.array
         an array of point tags

     Returns
     -------
     coord: np.array
         an array of point coordinates

     """

    nd_case = np.size(point_tags)
    coord = np.zeros((nd_case, 2))
    if nd_case == 1:
        coord = self.coordinate[point_tags, :]
    else:
        coord = self.coordinate[point_tags, :]

    if np.size(coord) == 0:
        return None
    else:
        return coord
