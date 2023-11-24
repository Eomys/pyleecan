# -*- coding: utf-8 -*-
from itertools import repeat

from numpy import abs, array, newaxis

from .get_element import _check_element_name


def get_element_area(self, element_indices=None, element_name=[]):
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
        element_mat_dict=self.element, element_name=element_name
    )

    vertices_dict = self.get_element_coordinate(
        element_indices=element_indices, element_name=element_name
    )

    for element_name, vertices in vertices_dict.items():
        if len(vertices) != 0:
            try:
                A = self.element[element_name].ref_element.get_element_area(vertices)

            except (AttributeError, NotImplementedError):
                logger.warning(
                    f'MeshMat: Reference element for "{element_name}" of type "{type(self.element[element_name])}" not found. '
                    + "Respective area set to zero."
                )
                A = list(repeat(0, vertices.shape[0]))

            area.extend(A)

    return array(area)
