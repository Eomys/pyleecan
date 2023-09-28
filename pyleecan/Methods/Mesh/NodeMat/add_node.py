# -*- coding: utf-8 -*-

import numpy as np


def add_node(self, coord):
    """Define a new NodeMat object based on a set of elements.

    Parameters
    ----------
    self : NodeMat
        an NodeMat object
    element : Element
        an Element object

    Returns
    -------
    node: Node
        a Node object corresponding to Element

    """
    if self.is_exist(coord):
        return None
    else:
        if self.coordinate is not None and self.coordinate.size > 0:
            self.coordinate = np.vstack((self.coordinate, coord))
            new_ind = max(self.indice) + 1
            self.indice = np.concatenate((self.indice, np.array([new_ind], dtype=int)))
            self.nb_node = self.nb_node + 1
        else:
            if self.coordinate is not None:
                self.coordinate = np.concatenate((self.coordinate, coord))
            else:
                self.coordinate = np.array(coord)
            new_ind = 0
            self.indice = np.array([], dtype=int)
            self.indice = np.concatenate((self.indice, np.array([new_ind], dtype=int)))
            self.nb_node = self.nb_node + 1

    return new_ind
