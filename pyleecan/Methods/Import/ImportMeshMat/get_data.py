# -*- coding: utf-8 -*-

from os.path import splitext

from pyleecan.Classes.ImportMeshUnv import ImportMeshUnv
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.NodeMat import NodeMat


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

    # Get mesh data (nodes and elements)
    if splitext(self.file_path)[1] == ".unv":
        nodes, elements = ImportMeshUnv(self.file_path).get_data()
    else:
        raise Exception(splitext(self.file_path)[1] + " files are not supported")

    # Define MeshMat object
    if min(nodes[:, 0]) == 0 and max(nodes[:, 0]) == len(nodes[:, 0])-1:
        is_renum=False
    else:
        is_renum=True

    mesh = MeshMat(_is_renum=is_renum)
    mesh.label = "Imported mesh"

    # Define NodeMat object
    mesh.node = NodeMat(
        coordinate=nodes[:, 1:],
        nb_node=nodes.shape[0],
        indice=nodes[:, 0],
    )

    # Define CellMat objects
    for elt_type, elt in elements.items():
        mesh.cell[elt_type] = CellMat(
            connectivity=elt[:, 1:],
            nb_cell=elt.shape[0],
            nb_node_per_cell=elt.shape[1] - 1,
            indice=elt[:, 0],
        )

    return mesh
