# -*- coding: utf-8 -*-

import numpy as np
from numpy.typing import ArrayLike
from typing import Union


def add_node(self, coordinate: ArrayLike) -> Union[None, int]:
    """Add a new node defined by its coordinates to the NodeMat
    (if a node of this coordinate already exist, do nothing)

    Parameters
    ----------
    self : NodeMat
        an NodeMat object
    coordinate : ArrayLike
        The list of coordinates (length must match mesh dimension)

    Returns
    -------
    Union[None,int]
        Index of the new node or None if the node already exists
    """
    if self.is_exist(coordinate):
        return None

    # Empty coordinate case
    if self.coordinate is None or self.coordinate.size == 0:
        self.coordinate = np.array([coordinate])
        self.nb_node = 1
        self.indice = np.array([0], dtype=np.int32)

        return 0

    # Add node only if it doesn't already exist
    self.coordinate = np.vstack((self.coordinate, coordinate))
    new_index = np.max(self.indice) + 1
    self.indice = np.concatenate((self.indice, np.array([new_index])))
    self.nb_node += 1

    return new_index
