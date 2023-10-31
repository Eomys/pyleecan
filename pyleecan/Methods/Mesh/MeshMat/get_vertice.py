# -*- coding: utf-8 -*-

from numpy import array
from .get_element import _check_element_name


def get_vertice(self, element_indices=None, element_name=[]):
    """Return a connectivity matrix where the nodes indices are replaced by their coordinates.

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    element_indices : list
        list of the element indices to extract (optional)
    element_name : list | str
        One or several element names to be returned

    Returns
    -------
    node_coordinates: ndarray
        Nodes coordinates of each selected element

    """

    element_name = _check_element_name(
        element_mat_dict=self.element, element_name=element_name
    )

    element_connectivity_dict, *_ = self.get_element(
        element_indices=element_indices, element_name=element_name
    )
    node_coordinates = {}
    for key, connectivity in element_connectivity_dict.items():
        if connectivity.ndim > 1:
            node_coordinates[key] = array(
                [self.get_node_coordinate(nodes) for nodes in connectivity]
            )
        else:
            node_coordinates[key] = self.get_node_coordinate(connectivity)

    return node_coordinates
