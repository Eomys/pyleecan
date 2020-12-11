# -*- coding: utf-8 -*-

import numpy as np


def get_point2cell(self, pt_indice):
    """Return all indices of cells containing a point.

    Parameters
    ----------
    self : CellMat
        an CellMat object
    pt_indice : int
        a point indice

    Returns
    -------
    pt_to_cell: ndarray
        Indices of cells containing the point

    """

    pt_to_cell = np.array([], dtype=int)
    connect = self.connectivity
    ind = self.indice

    if (
        connect is not None and len(connect.shape) > 1
    ):  # If there is more than 1 element
        Ielem = np.where(connect == pt_indice)[0]
        pt_to_cell = ind[Ielem]
    else:
        if sum(connect == pt_indice) > 0:
            pt_to_cell = ind

    return pt_to_cell
