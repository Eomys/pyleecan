# -*- coding: utf-8 -*-

import numpy as np
from typing import Union
from typing import Optional


def get_indice(self, coordinate: Optional[np.ndarray] = None) -> Union[np.ndarray, int]:
    """Return the coordinates of node(s).

    Parameters
    ----------
    self : NodeMat
        an NodeMat object
    coordinate : Optional[np.ndarray]
        a node coordinate

    Returns
    -------
    Union[np.ndarray, int]
        Index of the provided node coordinates or every indices
    """

    if coordinate is None:
        return self.indice

    # The distance-based method is more time-consuming, but could provide a tolerance in the search of the node.
    # Compute the distance between nodes coordinates and the given ones
    dist_node = np.linalg.norm(self.coordinate - coordinate, axis=1)
    index_min = np.argmin(dist_node)
    if dist_node[index_min] < self.delta:
        return self.indice[index_min]
    else:
        raise ValueError(
            f"The node with coordinate {coordinate} has not been retrieved with tolerance {self.delta}, increasing the tolerance value may solve the issue."
        )
