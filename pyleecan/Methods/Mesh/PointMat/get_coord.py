# -*- coding: utf-8 -*-

import numpy as np


def get_coord(self, node_tags):
    """Return the coordinates of node(s).

     Parameters
     ----------
     self : PointMat
         an PointMat object
     node_tags : np.array
         an array of node tags

     Returns
     -------
     coord: np.array
         an array of node coordinates

     """

    nd_case = np.size(node_tags)
    coord = np.zeros((nd_case, 2))
    if nd_case == 1:
        Ipos = np.where(self.tag == node_tags)[0]
        coord = self.coordinate[Ipos, :]
    else:
        for ind in range(nd_case):
            Ipos = np.where(self.tag == node_tags[ind])[0]
            coord[ind, :] = self.coordinate[Ipos, :]

    if np.size(coord) == 0:
        return None
    else:
        return coord
