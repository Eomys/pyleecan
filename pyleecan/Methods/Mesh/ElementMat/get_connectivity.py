# -*- coding: utf-8 -*-

import numpy as np
from typing import Optional


def get_connectivity(self, element_index: Optional[int] = None) -> np.ndarray:
    """Return the connectivity of one element.

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    element_index : Optional[int]
       the indice of a element, by default None. If None, return all elements.

    Returns
    -------
    np.ndarray
        Selected element connectivity. Return empty array if the index does not exist
    """

    connectivity = self.connectivity
    indices = self.indice
    nb_element = self.nb_element

    if element_index is None:  # Return all elements
        return connectivity

    if nb_element == 0:  # No element
        return np.array([[]])

    connectivity_index = (indices == element_index).nonzero()[0]
    if connectivity_index.size > 0:
        return connectivity[connectivity_index[0], :]
    else:
        return np.array([[]])
