# -*- coding: utf-8 -*-

from typing import Dict, List, Optional, Union

from numpy import array, ndarray

from .get_element import _check_element_name


def get_element_coordinate(
    self,
    element_indices: Optional[List[int]] = None,
    element_name: Union[List[str], str] = [],
) -> Dict[str, ndarray]:
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
    node_coordinates: Dict[str, ndarray]
        Nodes coordinates of each selected element

    """

    element_name = _check_element_name(
        element_mat_dict=self.element_dict, element_name=element_name
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
