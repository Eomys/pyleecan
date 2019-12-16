# -*- coding: utf-8 -*-

import numpy as np


def get_node2element(self, node_tag):
    """Return all element tags of elements containing the node tag node_tag

    Parameters
    ----------
    self : Mesh
        an Mesh object
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

    if connect is not None:  # If there is at least one element
        for key in connect:
            if len(connect[key].shape) > 1:  # If there is more than 1 element
                Ielem = np.where(connect[key] == node_tag)[0]
                nodes_to_elements = np.concatenate((nodes_to_elements, tag[key][Ielem]))
            else:
                if sum(connect[key] == node_tag) > 0:
                    nodes_to_elements = np.concatenate((nodes_to_elements, tag[key]))

    if nodes_to_elements.size == 0:
        return None
    else:
        return nodes_to_elements
