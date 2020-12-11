# -*- coding: utf-8 -*-

import numpy as np


def add_cell(self, pt_indice, new_ind):
    """Add a new element

    Parameters
    ----------
    self : CellMat
        an CellMat object
    new_ind : int
        an new cell indices
    pt_indice : ndarray
        connectivity

    Returns
    -------
        is_created : bool
            False if the element already exist or if it is not possible to add the element
    """
    # Check the existence of the element
    if len(np.unique(pt_indice)) != self.nb_pt_per_cell:
        return False

    if self.is_exist(pt_indice):
        return False

    # Create the new element
    if self.nb_cell == 0:
        self.connectivity = pt_indice
        self.indice = np.array([new_ind])
    else:
        self.connectivity = np.vstack([self.connectivity, pt_indice])
        self.indice = np.concatenate([self.indice, np.array([new_ind])])

    self.nb_cell = self.nb_cell + 1

    return True
