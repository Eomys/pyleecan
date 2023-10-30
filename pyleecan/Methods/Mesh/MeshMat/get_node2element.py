# -*- coding: utf-8 -*-

import numpy as np


def get_node2element(self, node_indice):
    """Return all element indices of elements containing a node.

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    node_indice : int
        a node indice

    Returns
    -------
    node_to_element: ndarray
        Indices of elements containing the node

    """

    node_to_element = np.array([], dtype=int)

    for key in self.element:
        connect = self.element[key].connectivity
        indice_elem = self.element[key].indice
        if len(connect[key].shape) > 1:  # If there is more than 1 element
            Ielem = np.where(connect[key] == node_indice)[0]
            node_to_element = np.concatenate((node_to_element, indice_elem[key][Ielem]))
        else:
            if connect[key] is not None and sum(connect[key] == node_indice) > 0:
                node_to_element = np.concatenate((node_to_element, indice_elem[key]))

    return node_to_element
