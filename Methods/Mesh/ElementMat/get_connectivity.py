# -*- coding: utf-8 -*-

import numpy as np


def get_connectivity(self, elem_tag=None):
    """Return the connectivity for one element designed by its tag

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    elem_tag : int
        an element tag

    Returns
    -------
    connect_select: ndarray
        Selected element connectivity. Return None if the tag does not exist

    """

    connect = self.connectivity
    tag = self.tag
    nb_elem = self.nb_elem

    if nb_elem == 0:
        return None
    elif nb_elem == 1:
        if tag[0] == elem_tag:
            return connect
        else:
            return None
    else:
        Ipos_select = np.where(tag == elem_tag)[0]
        if Ipos_select.size > 0:
            return connect[Ipos_select[0], :]
        else:
            return None




