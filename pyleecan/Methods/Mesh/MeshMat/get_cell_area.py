# -*- coding: utf-8 -*-
from numpy import abs, newaxis


def get_cell_area(self, indices=None):
    """
    Return the area of the cells on the outer surface.
    Triangle: https://en.wikipedia.org/wiki/Shoelace_formula
    #TODO address multiple cell type issue, i.e. distracted indices
    Parameters
    ----------
    self : MeshMat
        a MeshMat object
    indices : list
        list of the points to extract (optional)
    Returns
    -------
    areas: ndarray
        Area of the cells
    """
    area = None

    vertices_dict = self.get_vertice(indices=indices)

    key = "triangle"
    if key in vertices_dict:
        vertices = vertices_dict[key]
        if vertices.shape[-1] == 2:  # 2D - case
            if len(vertices.shape) == 2:  # only one indice -> adapt array shape
                vertices = vertices[newaxis, :, :]

            a = vertices[:, 0, 0] - vertices[:, 1, 0]  # x1 - x2
            b = vertices[:, 0, 1] - vertices[:, 2, 1]  # y1 - y3
            c = vertices[:, 0, 0] - vertices[:, 2, 0]  # x1 - x3
            d = vertices[:, 0, 1] - vertices[:, 1, 1]  # y1 - y2

        area = 1 / 2 * abs(a * b - c * d)

    return area