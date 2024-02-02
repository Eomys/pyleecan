# -*- coding: utf-8 -*-
from numpy import abs, array, ndarray, newaxis


def get_element_area(self, element_coordinate: ndarray) -> ndarray:
    """Return the area of the elements.
    https://en.wikipedia.org/wiki/Shoelace_formula

    Parameters
    ----------
    self : RefTriangle3
        a RefTriangle3 object
    element_coordinate : list or array
        the elements coordinates

    Returns
    -------
    area: array
        area of the elements
    """
    if isinstance(element_coordinate, list):
        element_coordinate = array(element_coordinate)

    if element_coordinate.shape[-1] == 2:  # 2D - case
        if len(element_coordinate.shape) == 2:  # only one indice -> adapt array shape
            element_coordinate = element_coordinate[newaxis, :, :]

        a = element_coordinate[:, 0, 0] - element_coordinate[:, 1, 0]  # x1 - x2
        b = element_coordinate[:, 0, 1] - element_coordinate[:, 2, 1]  # y1 - y3
        c = element_coordinate[:, 0, 0] - element_coordinate[:, 2, 0]  # x1 - x3
        d = element_coordinate[:, 0, 1] - element_coordinate[:, 1, 1]  # y1 - y2

    area = 1 / 2 * abs(a * b - c * d)

    return area
