# -*- coding: utf-8 -*-
from numpy import abs, array, ndarray, newaxis


def get_element_area(self, element_coordinate: ndarray) -> ndarray:
    """Return the area of the elements.

    Parameters
    ----------
    self : RefElement
    element_coordinate : list or array
        the elements coordinates

    Returns
    -------
    area: array
        area of the elements
    """

    raise NotImplementedError(
        f"{type(self).__name__}.get_element_area is not implemented."
    )
