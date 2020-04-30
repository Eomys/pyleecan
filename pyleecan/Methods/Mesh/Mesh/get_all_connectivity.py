# -*- coding: utf-8 -*-

import numpy as np


def get_all_connectivity(self, elem_type=None, group=None):
    """Return the connectivity and tags for a selected type of elements and a selected group.

    Parameters
    ----------
    self : Mesh
        an Mesh object
    elem_type : str
        a key corresponding to an element type
    group : numpy.array
        One or several group numbers to be returned

    Returns
    -------
    connect_select: numpy.array
        Selected connectivity
    tag_select: ndarray
        Selected element tags
    """

    connect_select = np.array([])
    tags_select = np.array([])

    for key in self.element:  # Protect from non-existing elem_type
        if key == elem_type:
            connect_select, tags_select = self.element[key].get_all_connectivity(group)

    return connect_select, tags_select
