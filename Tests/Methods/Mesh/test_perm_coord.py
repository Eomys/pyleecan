import numpy as np
import pytest

from SciDataTool import DataLinspace, DataFreq, VectorField

from pyleecan.Classes.MeshVTK import MeshVTK
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.SolutionMat import SolutionMat
from pyleecan.Classes.MeshSolution import MeshSolution
from Tests import save_plot_path as save_path


@pytest.mark.MeshSol
def test_perm_coord():
    # Generate mesh
    mesh = MeshMat(dimension=3)
    mesh.node = NodeMat()
    mesh.node.add_node([1, 0, -1])
    mesh.node.add_node([0.707, 0.707, -1])
    mesh.node.add_node([0, 1, -1])
    mesh.node.add_node([-0.707, 0.707, -1])
    mesh.node.add_node([-1, 0, -1])
    mesh.node.add_node([-0.707, -0.707, -1])
    mesh.node.add_node([0, -1, -1])
    mesh.node.add_node([0.707, -0.707, -1])
    mesh.node.add_node([1, 0, 1])
    mesh.node.add_node([0.707, 0.707, 1])
    mesh.node.add_node([0, 1, 1])
    mesh.node.add_node([-0.707, 0.707, 1])
    mesh.node.add_node([-1, 0, 1])
    mesh.node.add_node([-0.707, -0.707, 1])
    mesh.node.add_node([0, -1, 1])
    mesh.node.add_node([0.707, -0.707, 1])

    mesh.cell["quad"] = CellMat(nb_node_per_cell=4)
    mesh.add_cell([0, 8, 9, 1], "quad")
    mesh.add_cell([1, 9, 10, 2], "quad")
    mesh.add_cell([2, 10, 11, 3], "quad")
    mesh.add_cell([3, 11, 12, 4], "quad")
    mesh.add_cell([4, 12, 13, 5], "quad")
    mesh.add_cell([5, 13, 14, 6], "quad")
    mesh.add_cell([6, 14, 15, 7], "quad")
    mesh.add_cell([7, 15, 8, 0], "quad")
    mesh.cell["quad"].indice = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    mesh_pv = mesh.get_mesh_pv()
    mesh_vtk = MeshVTK(
        mesh=mesh_pv,
        is_pyvista_mesh=True,
    )

    # Generate field
    alpha = np.arange(8) * 2 * np.pi / 8
    k = -2
    field = np.exp(1j * k * alpha)
    field = np.hstack((field.T, field.T))
    field = np.stack((field, field, np.zeros(field.shape)), axis=1)
    solution = SolutionMat(
        field=field,
        label="Field",
    )

    # Generate MeshSolution
    MSol = MeshSolution(
        mesh=[mesh_vtk],
        solution=[solution],
        dimension=3,
    )
    MSol_before = MSol.copy()
    MSol.perm_coord(perm_coord_list=[0, 2, 1])

    assert (
        MSol_before.solution[0].field[0, [0, 2, 1]] == MSol.solution[0].field[0, :]
    ).all()
