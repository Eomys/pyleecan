# -*- coding: utf-8 -*-
from typing import Optional

from numpy.typing import ArrayLike


def get_node_indice(self, coordinates: Optional[ArrayLike] = None) -> ArrayLike:
    """Return a matrix of nodes coordinates.

    Parameters
    ----------
    self : Mesh
        an Mesh object
    coordinates: ndarray
        nodes coordinates

    Returns
    -------
    indices : ndarray
        nodes indices

    """

    if coordinates is None:
        return self.node.get_indice()
    else:
        raise NotImplementedError("Providing coordinates is not supported yet.")
