# -*- coding: utf-8 -*-

import numpy as np


def add_node(self, coord):
    """Add a new node defined by its coordinates to the NodeMat
    (if a node of this coordinate already exist, do nothing)

    Parameters
    ----------
    self : NodeMat
        an NodeMat object
    coord : list
        The list of coordinates (length must match mesh dimension)
    """
    if self.is_exist(coord):
        return None
    else:  # Add node only if it doesn't already exist
        if self.coordinate is not None and self.coordinate.size > 0:
            self.coordinate = np.vstack((self.coordinate, coord))
            new_ind = max(self.indice) + 1
            self.indice = np.concatenate((self.indice, np.array([new_ind], dtype=int)))
            self.nb_node = self.nb_node + 1
        else:  # Add first node
            if self.coordinate is not None:
                self.coordinate = np.concatenate((self.coordinate, coord))
            else:
                self.coordinate = np.array(coord)
            new_ind = 0
            self.indice = np.array([], dtype=int)
            self.indice = np.concatenate((self.indice, np.array([new_ind], dtype=int)))
            self.nb_node = self.nb_node + 1

    return new_ind
