# -*- coding: utf-8 -*-

import numpy as np


def get_node2element(self, node_tag):
    """Return all element tags of elements containing the node tag node_tag

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    node_tag : int
        a node tag

    Returns
    -------
    nodes_to_elements: dict
        Element tags of all elements containing the node node_tag

    """

    nodes_to_elements = np.array([], dtype=int)
    connect = self.connectivity
    tag = self.tag

    if len(connect.shape) > 1:  # If there is more than 1 element
        Ielem = np.where(connect == node_tag)[0]
        nodes_to_elements = np.concatenate((nodes_to_elements, tag[Ielem]))
    else:
        if sum(connect == node_tag) > 0:
            nodes_to_elements = np.concatenate((nodes_to_elements, tag))

    return nodes_to_elements
