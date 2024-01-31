# -*- coding: utf-8 -*-

import numpy as np
from typing import Optional
from typing import Union


def get_connectivity(
    self, element_index: Optional[int] = None
) -> Union[np.ndarray, None]:
    """_summary_

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    element_index : Optional[int], optional
       the indice of a element, by default None. If None, return all elements.

    Returns
    -------
    Union[np.ndarray, None]
        Selected element connectivity. Return None if the index does not exist
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
