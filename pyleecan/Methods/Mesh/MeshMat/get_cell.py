# -*- coding: utf-8 -*-
import collections
import numpy as np


def get_cell(self, indices=None):
    """Return the connectivity for one selected element

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    indices : list
        list of indice. If None, return all.

    Returns
    -------
    cells: dict
        Dict of connectivities

    """
    if not isinstance(indices, collections.Iterable):
        indices = (indices,)

    cells = dict()
    indice_dict = dict()
    nb_cell = 0
    for key in self.cell:
        cells[key] = list()
        indice_dict[key] = list()

        for ind in indices:
            connect = self.cell[key].get_connectivity(ind)
            if connect is not None:
                cells[key].append(connect)
                nb_cell = len(connect)
                indice_dict[key].append(ind)

        cells[key] = np.squeeze(np.array(cells[key]))

    return cells, nb_cell, indice_dict
