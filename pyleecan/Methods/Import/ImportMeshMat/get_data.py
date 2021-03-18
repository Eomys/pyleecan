# -*- coding: utf-8 -*-

from os.path import splitext

from pyleecan.Classes.ImportMeshUnv import ImportMeshUnv
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.PointMat import PointMat


def get_data(self):
    """Import mesh and generate MeshMat object

    Parameters
    ----------
    self : ImportData
        An ImportData object

    Returns
    -------
    mesh: MeshMat
        The generated MeshMat object

    """

    # Get mesh data (points and elements)
    if splitext(self.file_path)[1] == ".unv":
        points, elements = ImportMeshUnv(self.file_path).get_data()
    else:
        raise Exception(splitext(self.file_path)[1] + " files are not supported")

    # Define MeshMat object
    mesh = MeshMat()
    mesh.label = "Imported mesh"

    # Define PointMat object
    mesh.point = PointMat(
        coordinate=points[:, 1:],
        nb_pt=points.shape[0],
        indice=points[:, 0],
    )

    # Define CellMat objects
    for elt_type, elt in elements.items():
        mesh.cell[elt_type] = CellMat(
            connectivity=elt[:, 1:],
            nb_cell=elt.shape[0],
            nb_pt_per_cell=elt.shape[1] - 1,
            indice=elt[:, 0],
        )

    return mesh
