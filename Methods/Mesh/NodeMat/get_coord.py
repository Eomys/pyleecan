# -*- coding: utf-8 -*-

import numpy as np


def get_coord(self, node_tags=None):
    """Return the coordinates of node(s).

     Parameters
     ----------
     self : NodeMat
         an NodeMat object
     node_tags : np.array
         an array of node tags

     Returns
     -------
     coord: np.array
         an array of node coordinates

     """

    if node_tags is None:
        coord = self.coordinate
    else:
        nd_case = len(node_tags)
        coord = np.zeros((nd_case, 2))
        for ind in range(nd_case):
            Ipos = np.where(self.node_tag == node_tags[ind])[0]
            coord[ind, :] = self.coordinate[Ipos, :]

    return coord
