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
    for key in self.cell:
        cells[key] = list()
        if indices is None:
            cells[key] = self.cell[key].get_connectivity()
        else:
            for ind in indices:
                connect = self.cell[key].get_connectivity(ind)
                if connect is not None:
                    cells[key].append(connect)
        cells[key] = np.squeeze(np.array(cells[key]))

    return cells
