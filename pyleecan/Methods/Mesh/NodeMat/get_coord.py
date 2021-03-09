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

    coord = list()
    indices_all = self.indice
    coordinate = self.coordinate

    for ind in node_indice:
        Ipos = np.where(indices_all == ind)[0][0]
        coord.append(self.coordinate[Ipos, :])

    return np.array(coord)
