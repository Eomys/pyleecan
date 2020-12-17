# -*- coding: utf-8 -*-
from numpy import abs, newaxis, array


def get_cell_area(self, vertices):
    """Return the array of the cells.

    Parameters
    ----------
    self : RefTriangle3
        a RefTriangle3 object
    vertices : list or array
        the cells vertices

    Returns
    -------
    area: array
        area of the cells
    """
    if isinstance(vertices, list):
        vertices = array(vertices)

    if vertices.shape[-1] == 2:  # 2D - case
        if len(vertices.shape) == 2:  # only one indice -> adapt array shape
            vertices = vertices[newaxis, :, :]

        a = vertices[:, 0, 0] - vertices[:, 1, 0]  # x1 - x2
        b = vertices[:, 0, 1] - vertices[:, 2, 1]  # y1 - y3
        c = vertices[:, 0, 0] - vertices[:, 2, 0]  # x1 - x3
        d = vertices[:, 0, 1] - vertices[:, 1, 1]  # y1 - y2

    area = 1 / 2 * abs(a * b - c * d)

    return area
