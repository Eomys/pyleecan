# -*- coding: utf-8 -*-

import numpy as np


def get_node2element(self, node_tag):
    """Return all elements (connectivity) containing the node tag node_tag

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

    Ielem = np.where(connect == node_tag)[0]
    nodes_to_elements = np.concatenate((nodes_to_elements, Ielem))

    return nodes_to_elements
