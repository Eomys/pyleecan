# -*- coding: utf-8 -*-
import collections

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
    elements: dict
        Dict of connectivities

    """
    if not isinstance(indices, collections.Iterable) and indices is not None:
        indices = (indices,)

    elements = dict()
    indice_dict = dict()
    nb_element = 0
    for key in self.element:
        if indices is None:
            elements[key] = self.element[key].get_connectivity()
            indice_dict[key] = self.element[key].indice
            nb_element = self.element[key].nb_element
        else:
            elements[key] = list()
            indice_dict[key] = list()

            for ind in indices:
                connect = self.element[key].get_connectivity(ind)
                if connect is not None:
                    elements[key].append(connect)
                    nb_element = nb_element + len(connect)
                    indice_dict[key].append(ind)

            elements[key] = np.squeeze(np.array(elements[key]))
    # TODO add other returned values in docstring
    return elements, nb_element, indice_dict
