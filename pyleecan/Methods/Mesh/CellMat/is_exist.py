# -*- coding: utf-8 -*-

import numpy as np


def is_exist(self, connectivity):
    """Check the existence of a cell defined by a connectivity (vector of points indices).
    The order of points indices does not matter.

    Parameters
    ----------
    self : CellMat
        an CellMat object
    connectivity : ndarray
        an array of node tags

    Returns
    -------
        bool
            True if the element already exist
    """

    # Check the existence of the element
    e = np.array([], dtype=int)
    for nd_tag in connectivity:
        e = np.concatenate((e, self.get_point2cell(nd_tag)))

    unique, unique_counts = np.unique(e, return_counts=True)
    for ie in range(len(unique)):
        if unique_counts[ie] == self.nb_pt_per_cell and unique_counts[ie] == len(
            connectivity
        ):
            # If this condition is valid, the element already exist
            return True
    return False
