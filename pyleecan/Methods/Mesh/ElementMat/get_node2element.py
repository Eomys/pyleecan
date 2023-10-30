# -*- coding: utf-8 -*-

import numpy as np


def get_node2element(self, node_indice):
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
    ind = self.indice

    if (
        connect is not None and len(connect.shape) > 1
    ):  # If there is more than 1 element
        idx_elem = np.where(connect == node_indice)[0]
        node_to_element = ind[idx_elem]
    else:
        if connect is not None and sum(connect == node_indice) > 0:
            node_to_element = ind

    return node_to_element
