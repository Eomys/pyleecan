# -*- coding: utf-8 -*-
from itertools import repeat
from typing import List, Optional, Union

from numpy import array, ndarray

from .get_element import _check_element_name


def get_element_area(
    self,
    element_indices: Optional[List[int]] = None,
    element_name: Union[List[str], str] = [],
) -> ndarray:
    """
    Return the area of the elements on the outer surface.
    #TODO address multiple element type issue, i.e. distracted indices
    Parameters
    ----------
    self : MeshMat
        a MeshMat object
    element_indices : list
        list of the element indices to extract (optional)
    element_name : list | str
        Name(s) of the element to extract
    Returns
    -------
    areas: ndarray
        Area of the elements
    """
    logger = self.get_logger()
    area = []

    element_name = _check_element_name(
        element_mat_dict=self.element_dict, element_name=element_name
    )

    element_coordinate_dict = self.get_element_coordinate(
        element_indices=element_indices, element_name=element_name
    )

    for element_name, element_coordinate in element_coordinate_dict.items():
        if len(element_coordinate) != 0:
            try:
                A = self.element_dict[element_name].ref_element.get_element_area(
                    element_coordinate
                )

            except (AttributeError, NotImplementedError):
                logger.warning(
                    (
                        f'MeshMat: Reference element for "{element_name}" of type "{type(self.element_dict[element_name])}" not found. ',
                        "Respective area set to zero.",
                    )
                )
                A = repeat(0, element_coordinate.shape[0])

            area.extend(A)

    return array(area)
