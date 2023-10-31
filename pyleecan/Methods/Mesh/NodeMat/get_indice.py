# -*- coding: utf-8 -*-

import numpy as np


def get_indice(self, coord=None):
    """Return the coordinates of node(s).

    Parameters
    ----------
    self : NodeMat
        an NodeMat object
    coord : ndarray
        a node coordinate

    Returns
    -------
    coord: np.array
        an array of node coordinates

    """

    if coord is None:
        return self.indice
    else:
        # The distance-based method is more time-consuming, but could provide a tolerance in the search of the node.
        # Compute the distance between nodes coordinates and the given ones
        dist_node = np.linalg.norm(self.coordinate - coord, axis=1)
        index_min = np.argmin(dist_node)
        if dist_node[index_min] < self.delta:
            return self.indice[index_min]
        else:
            raise ValueError(
                f"The node with coordinate {coord} has not been retrieved."
            )
