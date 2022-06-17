# -*- coding: utf-8 -*-

import numpy as np


def get_node2cell(self, node_indice):
    """Return all cell indices of cells containing a node.

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    node_indice : int
        a node indice

    Returns
    -------
    node_to_cell: ndarray
        Indices of cells containing the node

    """

    node_to_cell = np.array([], dtype=int)

    for key in self.cell:
        connect = self.cell[key].connectivity
        indice_elem = self.cell[key].indice
        if len(connect[key].shape) > 1:  # If there is more than 1 element
            Ielem = np.where(connect[key] == node_indice)[0]
            node_to_cell = np.concatenate((node_to_cell, indice_elem[key][Ielem]))
        else:
            if connect[key] is not None and sum(connect[key] == node_indice) > 0:
                node_to_cell = np.concatenate((node_to_cell, indice_elem[key]))

    return node_to_cell
