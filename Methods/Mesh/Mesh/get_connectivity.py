# -*- coding: utf-8 -*-

import numpy as np


def get_connectivity(self, elem_tag):
    """Return the connectivity for one selected element

    Parameters
    ----------
    self : Mesh
        an Mesh object
    elem_tag : int
        an element tag

    Returns
    -------
    connect_select: numpy.array
        Selected connectivity. Return None if the tag does not exist

    """

    for key in self.element:
        connect_select = self.element[key].get_connectivity(elem_tag)
        if connect_select is not None:
            return connect_select
