# -*- coding: utf-8 -*-

import numpy as np


def get_node2cell(self, node_indice):
    """Return all indices of cells containing a node.

    Parameters
    ----------
    self : CellMat
        an CellMat object
    node_indice : int
        a node indice

    Returns
    -------
    node_to_cell: ndarray
        Indices of cells containing the node

    """

    node_to_cell = np.array([], dtype=int)
    connect = self.connectivity
    ind = self.indice

    if (
        connect is not None and len(connect.shape) > 1
    ):  # If there is more than 1 element
        Ielem = np.where(connect == node_indice)[0]
        node_to_cell = ind[Ielem]
    else:
        if sum(connect == node_indice) > 0:
            node_to_cell = ind

    return node_to_cell
