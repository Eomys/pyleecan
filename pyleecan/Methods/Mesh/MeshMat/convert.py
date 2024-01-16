from itertools import repeat
from typing import Literal

import numpy as np
import pyvista as pv

from ....Classes.Mesh import Mesh
from ....Classes.RefLine3 import RefLine3
from ....Classes.RefQuad4 import RefQuad4
from ....Classes.RefQuad9 import RefQuad9
from ....Classes.RefTriangle3 import RefTriangle3
from ....Classes.RefTriangle6 import RefTriangle6


def convert(
    self,
    meshtype: Literal["MeshVTK", "MeshMat"] = "MeshMat",
    scale: float = 1.0,
) -> Mesh:
    """Convert the MeshMat to another type of Mesh object.

    Parameters
    ----------
    self : MeshMat
        a MeshMat object
    meshtype : str
        a type of Mesh object: MeshVTK or MeshMat
    scale : float
        scale factor

        Returns
    -------
    Mesh
        a Mesh object
    """

    if meshtype not in ["MeshMat", "MeshVTK"]:
        raise ValueError(
            f"Wrong meshtype value \"{meshtype}\", expected value: {', '.join(['MeshMat', 'MeshVTK'])}."
        )

    if meshtype == "MeshMat":
        new_mesh = self.copy()
        new_mesh.node.coordinate *= scale
        return new_mesh

    # Avoiding cicular import
    from ....Classes.MeshVTK import MeshVTK

    elements_ = []
    element_types = []

    # Map between pyleecan and pyvista element type
    element_types_dict = {
        RefTriangle3: pv.CellType.TRIANGLE,
        RefTriangle6: pv.CellType.QUADRATIC_TRIANGLE,
        RefQuad4: pv.CellType.QUAD,
        RefQuad9: pv.CellType.QUADRATIC_QUAD,
    }

    # Construct the element connectivity and element type vector to create the pyvista unstructured grid
    # https://docs.pyvista.org/version/stable/examples/00-load/create-unstructured-surface.html#creating-an-unstructured-grid
    for element in self.element_dict.values():
        connectivity = element.connectivity
        nb_element = connectivity.shape[0]
        element_types.extend(
            list(
                repeat(
                    element_types_dict[type(element.ref_element)],
                    nb_element,
                )
            )
        )

        elements_.append(
            np.hstack(
                [
                    connectivity.shape[1] * np.ones((nb_element, 1), dtype=np.int32),
                    connectivity,
                ]
            )
            .flatten()
            .astype(np.int32)
        )

    elements = np.hstack(elements_).astype(np.int32)

    pv_mesh = pv.UnstructuredGrid(elements, element_types, self.node.coordinate * scale)
    mesh_vtk = MeshVTK(mesh=pv_mesh, is_pyvista_mesh=True)

    return mesh_vtk
