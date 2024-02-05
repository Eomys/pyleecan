from typing import Optional

import numpy as np
from numpy.typing import ArrayLike


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

    raise NotImplementedError("Mesh is an abstract class")
