# -*- coding: utf-8 -*-

import numpy as np
from typing import Union
from numpy.typing import ArrayLike


def add_element(self, node_indices: Union[ArrayLike, int], new_index: int) -> bool:
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

        # Force connectivity to have shape nb_element × nb_node_per_element
        if isinstance(node_indices, int):
            self.connectivity = np.array([[node_indices]])
        else:
            self.connectivity = np.array([node_indices])

        self.indice = np.array([new_index])
    else:
        self.connectivity = np.vstack([self.connectivity, node_indices])
        self.indice = np.concatenate([self.indice, np.array([new_index])])

    self.nb_element += 1

    return True
