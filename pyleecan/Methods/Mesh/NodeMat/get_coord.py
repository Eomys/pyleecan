# -*- coding: utf-8 -*-

import numpy as np
from numpy.typing import ArrayLike


def get_coord(self, node_indices: ArrayLike) -> np.ndarray:
    """Return the coordinates of node(s).

    Parameters
    ----------
    node_indices : ArrayLike
        Array of node indices

    Returns
    -------
    np.ndarray
        Array of node coordinates
    """

    # Extract position of the given node indices in the index vector
    coord_indices = [(self.indice == index).nonzero()[0][0] for index in node_indices]

    return self.coordinate[coord_indices]
