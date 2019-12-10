# -*- coding: utf-8 -*-

import numpy as np


def get_node_tags(self, elem_tag=None):
    """Return a vector of nodes tags in the element(s) elem_tag

    Parameters
    ----------
    self : ElementDict
        an ElementDict object
    elem_tag : int
        some element tags

    Returns
    -------
    node_tags: ndarray
        Selected nodes coordinates

    """

    connect = self.connectivity
    tag = self.tag

    for key in connect:
        if len(connect[key].shape) == 1:  # If there is only 1 element
            if tag[key] == elem_tag:
                return connect[key]
        else:
            Ielem = np.where(tag[key] == elem_tag)[0]
            # There should only one solution
            if len(Ielem) > 0:
                return connect[key][Ielem[0]]
