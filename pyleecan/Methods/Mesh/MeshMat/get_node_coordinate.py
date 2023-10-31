# -*- coding: utf-8 -*-
from typing import Optional
from numpy.typing import ArrayLike
import numpy as np


def get_node_coordinate(self, indices: Optional[ArrayLike] = None) -> np.ndarray:
    """Return the coordinates of the node with provided indices.
    If indices is not specified, returns every node coordinates

    Parameters
    ----------
    indices : Optional[ArrayLike], optional
        Indices of the targeted nodes. If None, return all.

    Returns
    -------
    np.ndarray
        nodes coordinates
    """
    if indices is None:
        return self.node.coordinate
    else:
        return self.node.get_coord(indices)
