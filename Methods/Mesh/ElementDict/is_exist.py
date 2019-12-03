# -*- coding: utf-8 -*-

import numpy as np


def is_exist(self, node_tags):
    """Add a new element defined by a vector of node tags

    Parameters
    ----------
    self : ElementDict
        an ElementDict object
    node_tags : array
        an array of node tags

    Returns
    -------
        bool
            True if the element already exist
    """
    # Check the existence of the element
    if self.connectivity is not None:
        e = np.array([], dtype=int)
        for i in node_tags:
            e = np.concatenate((e, self.get_node2element(i)))

        unique, unique_counts = np.unique(e, return_counts=True)
        for ie in range(len(unique)):
            if unique_counts[ie] == len(
                self.get_node_tags(int(unique[ie]))
            ) and unique_counts[ie] == len(node_tags):
                # If this condition is valid, the element already exist
                return True
    return False
