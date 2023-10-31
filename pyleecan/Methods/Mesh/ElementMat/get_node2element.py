# -*- coding: utf-8 -*-

import numpy as np


def get_node2element(self, node_indice: int) -> np.ndarray:
    """Return all indices of elements containing a node.

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    node_indice : int
        a node indice

    Returns
    -------
    node_to_element: ndarray
        Indices of elements containing the node

    """

    node_to_element = np.array([], dtype=int)
    connect = self.connectivity

    if connect is None:
        return node_to_element

    if len(connect.shape) > 1:  # If there is more than 1 element
        idx_elem = (connect == node_indice).nonzero()[0]
        node_to_element = self.indice[idx_elem]

    elif sum(connect == node_indice) > 0:
        node_to_element = self.indice

    return node_to_element
