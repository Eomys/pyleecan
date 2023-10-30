# -*- coding: utf-8 -*-

import numpy as np


def get_connectivity(self, element_indice=None):
    """Return the connectivity of one element.

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    element_indice : int
        the indice of a element. If None, return all elements.

    Returns
    -------
    connect_select: ndarray
        Selected element connectivity. Return None if the tag does not exist

    """

    connect = self.connectivity
    ind = self.indice
    nb_element = self.nb_element

    if element_indice is None:  # Return all elements
        return connect
    else:
        if nb_element == 0:  # No element
            return None
        elif nb_element == 1:  # Only one element
            if ind[0] == element_indice:
                return connect
            else:
                return None
        else:
            Ipos_select = np.where(ind == element_indice)[0]
            if Ipos_select.size > 0:
                return connect[Ipos_select[0], :]
            else:
                return None
