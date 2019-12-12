# -*- coding: utf-8 -*-

import numpy as np


def get_node_tags(self, elem_tag):
    """Return a vector of (unique) node tags related to a vector of element tags.
    For only one element, use get connectivity.

    Parameters
    ----------
    self : Mesh
        an Mesh object
    elem_tag : numpy.array
        an element tag
    Returns
    -------
    all_node_tag: numpy.array
        Selected nodes tags

    """
    all_node_tag = np.array([], dtype=int)
    for ie in range(len(elem_tag)):
        all_node_tag = np.concatenate(
            (all_node_tag, self.get_connectivity(elem_tag[ie]))
        )

    return np.unique(all_node_tag)
