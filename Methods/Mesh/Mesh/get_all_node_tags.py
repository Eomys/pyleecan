# -*- coding: utf-8 -*-

import numpy as np


def get_all_node_tags(self):
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
    node_tags = np.array([], dtype=int)

    for key in connect:  # There should only one solution
        for ie in range(len(connect[key])):
            node_tags = np.concatenate((node_tags, connect[key][ie]))

    node_tags = np.unique(node_tags)

    return node_tags
