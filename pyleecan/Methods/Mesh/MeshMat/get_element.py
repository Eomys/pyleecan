# -*- coding: utf-8 -*-
from typing import Dict, List, Optional, Tuple, Union

import numpy as np

from ....Classes.ElementMat import ElementMat


def _check_element_name(
    element_mat_dict: Dict[str, ElementMat], element_name: Union[List[str], str]
) -> List[str]:
    """Check if the element names provided are in the element dictionnary

    Parameters
    ----------
    element_mat_dict : Dict[str, ElementMat]
        Dict of elements
    element_name : Union[List[str], str]
        name of elements

    Returns
    -------
    List[str]
        Name of elements processed

    Raises
    ------
    ValueError
        A provided name is not in the dictionnary
    """
    if isinstance(element_name, str):
        element_name = [element_name]
    elif len(element_name) == 0:
        return list(element_mat_dict.keys())

    all_element_names = element_mat_dict.keys()
    for elem_name in element_name:
        if elem_name not in all_element_names:
            raise ValueError(
                f'Wrong element_name value, "{elem_name}" not in {list(all_element_names)}'
            )
    return element_name


def get_element(
    self,
    element_indices: Optional[Union[int, List[int]]] = None,
    element_name: Union[List[str], str] = [],
) -> Tuple[Dict[str, np.ndarray], int, Dict[str, np.ndarray]]:
    """Return the connectivity for one selected element

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    element_indices: list
        list of element index. If None, return all.
    element_name : list
        list of element names to extract the connectivity. If None, return every element_names

    Returns
    -------
    dict_connectivity: dict[str, ndarray]
        Dict of connectivity with element names as keys
    nb_element: int
        Number of element in the connectivity
    dict_index: dict
        Dict of the element element_indices for each ElementMat
    """

    if isinstance(element_indices, (int, np.integer)):
        element_indices = (element_indices,)

    element_name = _check_element_name(
        element_mat_dict=self.element_dict, element_name=element_name
    )

    dict_connectivity = {}
    dict_index = {}
    nb_element = 0
    # Extract full connectivity matrix and element element_indices
    if element_indices is None:
        for key in element_name:
            element = self.element_dict[key]
            dict_connectivity[key] = element.get_connectivity()
            dict_index[key] = element.indice
            nb_element += element.nb_element

    # Extract element connectivity and index for each element
    else:
        for key in element_name:
            element = self.element_dict[key]
            list_connectivity = [
                element.get_connectivity(index) for index in element_indices
            ]
            # Extract connectivity if the element index is present
            dict_connectivity[key] = np.array(
                [
                    connectivity
                    for connectivity in list_connectivity
                    if connectivity.size
                ]
            ).squeeze()

            # Extract index if the element index is present
            dict_index[key] = [
                index
                for index, connectivity in zip(element_indices, list_connectivity)
                if connectivity.size
            ]

    return dict_connectivity, nb_element, dict_index
