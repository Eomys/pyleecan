# -*- coding: utf-8 -*-

import numpy as np


def get_node_tags(self, elem_tag):
    """Return a vector of all nodes tags related to the element

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    elem_tag : int
        an element tag
    Returns
    -------
    node_tags: numpy.array
        Selected nodes coordinates

    """

    return np.unique(self.get_connectivity(elem_tag))
