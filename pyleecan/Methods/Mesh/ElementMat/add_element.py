# -*- coding: utf-8 -*-

import numpy as np


def add_element(self, node_indices, new_index):
    """Add a new element defined by node indices

    Parameters
    ----------
    self : ElementMat
        a ElementMat object
    node_indices : ndarray or list of int
        a ndarray of nodes indices (length must match self.nb_node_per_element)
    new_index : int
        Index of the new element to use

    Returns
    -------
    is_created : bool
        False if the element already exist or if it is not possible to add the element
    """

    # Check that there is the correct number of nodes
    if len(np.unique(node_indices)) != self.nb_node_per_element:
        return False

    # Check if the Element with these nodes already exist (The order of nodes indices does not matter)
    if self.is_exist(node_indices):
        return False

    # Create/Add the new element
    if self.nb_element == 0:  # First element
        self.connectivity = node_indices
        self.indice = np.array([new_index])
    else:
        self.connectivity = np.vstack([self.connectivity, node_indices])
        self.indice = np.concatenate([self.indice, np.array([new_index])])

    self.nb_element += 1

    return True
