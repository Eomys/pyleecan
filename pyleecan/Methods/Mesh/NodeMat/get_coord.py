# -*- coding: utf-8 -*-

import numpy as np


def get_coord(self, node_indice):
    """Return the coordinates of node(s).

    Parameters
    ----------
    self : NodeMat
        an NodeMat object
    node_indice : np.array
        an array of node indice

    Returns
    -------
    coord: np.array
        an array of node coordinates

    """

    nd_case = np.size(node_indice)
    # coord = np.zeros((nd_case, 2))
    if nd_case == 1:
        coord = self.coordinate[node_indice, :]
    else:
        coord = self.coordinate[node_indice, :]

    if np.size(coord) == 0:
        return None
    else:
        return coord
