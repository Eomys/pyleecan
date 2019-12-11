# -*- coding: utf-8 -*-

import numpy as np


def add_element(self, node_tags, group=-1):
    """Add a new element defined by a vector of node tags

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    node_tags : numpy.array
        an array of node tags
    group : int
        the group number

    Returns
    -------
        is_created : bool
            False if the element already exist
    """
    # Check the existence of the element
    if self.is_exist(node_tags):
        return False

    # Create the new element
    if self.connectivity.size == 0:
        self.connectivity = node_tags
        self.tag = np.array([self.get_new_tag()])
        self.group = np.array([group], dtype=int)
    else:
        self.connectivity = np.vstack([self.connectivity, node_tags])
        self.tag = np.concatenate([self.tag, np.array([self.get_new_tag()])])
        self.group = np.concatenate([self.group, np.array([group], dtype=int)])

    self.nb_elem = self.nb_elem + 1

    return True
