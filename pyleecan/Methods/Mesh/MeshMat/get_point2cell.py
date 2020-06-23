# -*- coding: utf-8 -*-

import numpy as np


def get_point2cell(self, pt_indice):
    """Return all cell indices of cells containing a point.

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    pt_indice : int
        a point indice

    Returns
    -------
    pt_to_cell: ndarray
        Indices of cells containing the point

    """

    pt_to_cell = np.array([], dtype=int)

    for key in self.cell:
        connect = self.cell[key].connectivity
        indice_elem = self.cell[key].indice
        if len(connect[key].shape) > 1:  # If there is more than 1 element
            Ielem = np.where(connect[key] == pt_indice)[0]
            pt_to_cell = np.concatenate((pt_to_cell, indice_elem[key][Ielem]))
        else:
            if sum(connect[key] == pt_indice) > 0:
                pt_to_cell = np.concatenate((pt_to_cell, indice_elem[key]))

    return pt_to_cell
