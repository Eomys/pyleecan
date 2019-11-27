# -*- coding: utf-8 -*-

import numpy as np


def get_connectivity(self, elem_type=None):
    """Return the connectivity for a selected type of elements

    Parameters
    ----------
    self : ElementDict
        an ElementDict object
    elem_type : str
        a key corresponding to an element type

    Returns
    -------
    connect_select: ndarray
        Selected connectivity

    """

    connect = self.connectivity
    tag = self.tag
    connect_select = np.array([])

    if elem_type is None:  # Return the first type of element to be found
        for key in connect:
            connect_select = connect[key]
            break
    else:
        connect_select = connect[elem_type]

    return connect_select
