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
        pass  # TODO Search for indice of a node from coordiantes
