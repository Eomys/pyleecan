# -*- coding: utf-8 -*-

import numpy as np


def is_exist(self, node_tags):
    """Check the existence of an element defined by a vector of node tags

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    node_tags : numpy.ndarray
        an array of node tags

    Returns
    -------
        bool
            True if the element already exist
    """

    # Check the existence of the element
    e = np.array([], dtype=int)
    for nd_tag in node_tags:
        e = np.concatenate((e, self.get_node2element(nd_tag)))

    unique, unique_counts = np.unique(e, return_counts=True)
    for ie in range(len(unique)):
        if unique_counts[ie] == self.nb_node_per_element and unique_counts[ie] == len(
            node_tags
        ):
            # If this condition is valid, the element already exist
            return True
    return False
