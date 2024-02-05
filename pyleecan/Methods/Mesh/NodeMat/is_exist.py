# -*- coding: utf-8 -*-

import numpy as np


def is_exist(self, coordinate: np.ndarray) -> bool:
    """Check the existence of a node defined by its coordinates

    Parameters
    ----------
    self : NodeMat
        an NodeMat object
    coordinate : ndarray
        coordinate of the node

    Returns
    -------
    bool
        True if the element already exist
    """

    if self.nb_node == 0:
        return False

    # Compute the distance between the node coordinates and the provided coordinate
    dist_node = np.linalg.norm(self.coordinate - coordinate, axis=1)

    return np.any(dist_node < self.delta)
