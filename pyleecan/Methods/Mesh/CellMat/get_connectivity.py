# -*- coding: utf-8 -*-

import numpy as np


def get_connectivity(self, cell_indice=None):
    """Return the connectivity of one cell.

    Parameters
    ----------
    self : CellMat
        an CellMat object
    cell_indice : int
        the indice of a cell. If None, return all cells.

    Returns
    -------
    connect_select: ndarray
        Selected cell connectivity. Return None if the tag does not exist

    """

    connect = self.connectivity
    ind = self.indice
    nb_cell = self.nb_cell

    if cell_indice is None:  # Return all cells
        return connect
    else:
        if nb_cell == 0:  # No cell
            return None
        elif nb_cell == 1:  # Only one cell
            if ind[0] == cell_indice:
                return connect
            else:
                return None
        else:
            Ipos_select = np.where(ind == cell_indice)[0]
            if Ipos_select.size > 0:
                return connect[Ipos_select[0], :]
            else:
                return None
