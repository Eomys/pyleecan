# -*- coding: utf-8 -*-
from collections import Iterable

import numpy as np


def get_element(self, indices=None):
    """Return the connectivity for one selected element

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    indices : list
        list of indice. If None, return all.

    Returns
    -------
    dict_element: dict
        Dict of connectivities
    nb_element: int
        Number of element in the connectivity
    dict_index: dict
        Dict of the element indices for each ElementMat
    """

    if not isinstance(indices, Iterable) and indices is not None:
        indices = (indices,)

    dict_element = {}
    dict_index = {}
    nb_element = 0
    # Extract full connectivity matrix and element indices
    if indices is None:
        for key, element in self.element.items():
            dict_element[key] = element.get_connectivity()
            dict_index[key] = element.indice
            nb_element += element.nb_element

    # Extract element connectivity and index for each element
    else:
        for key, element in self.element.items():
            list_connectivity = [element.get_connectivity(index) for index in indices]
            # Extract connectivity if the element index is present
            dict_element[key] = np.array(
                [
                    connectivity
                    for connectivity in list_connectivity
                    if connectivity is not None
                ]
            ).squeeze()

            # Extract index if the element index is present
            dict_index[key] = [
                index
                for index, connectivity in zip(indices, list_connectivity)
                if connectivity is not None
            ]

    return dict_element, nb_element, dict_index
