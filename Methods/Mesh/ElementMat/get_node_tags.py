# -*- coding: utf-8 -*-

import numpy as np


def get_node_tags(self, elem_tag=None):
    """Return a vector of nodes tags in the element elem_tag

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    elem_tag : int
        an element tag

    Returns
    -------
    node_tags: ndarray
        Selected nodes coordinates

    """

    connect = self.connectivity
    tag = self.tag

    if len(connect.shape) == 1:  # If there is only 1 element
        if tag == elem_tag:
            return connect
    elif len(connect.shape) > 1:
        line = np.where(tag == elem_tag)[0]
        return connect[line, :]
