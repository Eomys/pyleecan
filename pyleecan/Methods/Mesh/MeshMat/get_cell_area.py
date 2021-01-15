# -*- coding: utf-8 -*-
from numpy import abs, newaxis, array


def get_cell_area(self, indices=None):
    """
    Return the area of the cells on the outer surface.
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
    logger = self.get_logger()
    area = []

    vertices_dict = self.get_vertice(indices=indices)

    for key, vertices in vertices_dict.items():
        if len(vertices) != 0:
            try:
                A = self.cell[key].interpolation.ref_cell.get_cell_area(vertices)
                A = A.tolist()
            except:
                logger.warning(
                    f'MeshMat: Reference Cell for "{key}" not found. '
                    + "Respective area set to zero."
                )
                A = [0 for i in range(vertices.shape[0])]

            area.extend(A)

    return array(area)
