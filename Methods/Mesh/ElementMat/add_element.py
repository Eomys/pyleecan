# -*- coding: utf-8 -*-

import numpy as np


def add_element(self, node_tags, new_tag, group=-1):
    """Add a new element defined by a vector of node tags

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    new_tag : int
        an new element tag
    node_tags : numpy.array
        an array of node tags
    group : int
        the group number

    Returns
    -------
        is_created : bool
            False if the element already exist or if it is not possible to add the element
    """
    # Check the existence of the element
    if len(np.unique(node_tags)) != self.nb_node_per_element:
        return False

    if self.is_exist(node_tags):
        return False

    # Create the new element
    if self.connectivity.size == 0:
        self.connectivity = node_tags
        self.tag = np.array([new_tag])
        self.group = np.array([group], dtype=int)
    else:
        self.connectivity = np.vstack([self.connectivity, node_tags])
        self.tag = np.concatenate([self.tag, np.array([new_tag])])
        self.group = np.concatenate([self.group, np.array([group], dtype=int)])

    self.nb_elem = self.nb_elem + 1

    return True
