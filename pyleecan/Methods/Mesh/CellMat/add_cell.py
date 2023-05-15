# -*- coding: utf-8 -*-

import numpy as np


def add_cell(self, node_indices, new_index):
    """Add a new cell defined by node indices

    Parameters
    ----------
    self : CellMat
        a CellMat object
    node_indices : ndarray or list of int
        a ndarray of nodes indices (length must match self.nb_node_per_cell)
    new_index : int
        Index of the new cell to use

    Returns
    -------
    is_created : bool
        False if the element already exist or if it is not possible to add the element
    """

    # Check that there is the correct number of nodes
    if len(np.unique(node_indices)) != self.nb_node_per_cell:
        return False

    # Check if the Cell with these nodes already exist (The order of nodes indices does not matter)
    if self.is_exist(node_indices):
        return False

    # Create/Add the new cell
    if self.nb_cell == 0:  # First cell
        self.connectivity = node_indices
        self.indice = np.array([new_index])
    else:
        self.connectivity = np.vstack([self.connectivity, node_indices])
        self.indice = np.concatenate([self.indice, np.array([new_index])])

    self.nb_cell = self.nb_cell + 1

    return True
