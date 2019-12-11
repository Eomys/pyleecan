# -*- coding: utf-8 -*-

import numpy as np


def get_connectivity(self, elem_tag=None):
    """Return the connectivity for a selected element

    Parameters
    ----------
    self : Mesh
        an Mesh object
    elem_tag : int
        an element tag

    Returns
    -------
    connect_select: ndarray
        Selected element connectivity

    """

    connect_select = np.array([])
    tags_select = np.array([])

    for key in self.element:
        tmp_connect_select = self.element[key].get_connectivity(elem_tag)
        if tmp_connect_select is not None:
            return connect_select
