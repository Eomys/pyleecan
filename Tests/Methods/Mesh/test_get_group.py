# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.SolutionMat import SolutionMat
import numpy as np


DELTA = 1e-10


@pytest.mark.METHODS
@pytest.mark.MeshSol
# @pytest.mark.DEV
def test_MeshMat_1group():
    """unittest for 1 group"""

    mesh = MeshMat()
    mesh.cell["triangle"] = CellMat(nb_node_per_cell=3)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([1, 0]))
    mesh.node.add_node(np.array([1, 2]))
    mesh.node.add_node(np.array([2, 3]))
    mesh.node.add_node(np.array([3, 3]))

    mesh.add_cell(np.array([0, 1, 2]), "triangle")
    mesh.add_cell(np.array([1, 2, 3]), "triangle")
    mesh.add_cell(np.array([4, 2, 3]), "triangle")

    meshsol = MeshSolution()
    meshsol.mesh = [mesh]
    meshsol.group = dict()
    meshsol.group["stator"] = np.array([0, 1])
    meshsol.group["rotor"] = np.array([2])

    MS_grp = meshsol.get_group("stator")
    cells_grp, nb_cell, indices = MS_grp.get_mesh().get_cell()
    solution = np.array([[0, 1, 2], [1, 2, 3]])
    result_tgl = cells_grp["triangle"]
    testA = np.sum(abs(solution - result_tgl))
    msg = "Wrong output: returned " + str(result_tgl) + ", expected: " + str(solution)
    assert testA == pytest.approx(0, rel=DELTA), msg

    MS_grp = meshsol.get_group("rotor")
    cells_grp, nb_cell, indices = MS_grp.get_mesh().get_cell()
    solution = np.array([[3, 3], [1, 2], [2, 3]])
    results = cells_grp["triangle"]  # The node indices have changed !
    nodes = MS_grp.get_mesh().get_node(results)
    testA = np.sum(abs(solution - nodes))
    msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
    assert testA == pytest.approx(0, rel=DELTA), msg

def test_MeshMat_2group():
    """unittest for 1 group"""

    mesh = MeshMat()
    mesh.cell["triangle"] = CellMat(nb_node_per_cell=3)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([1, 0]))
    mesh.node.add_node(np.array([1, 2]))
    mesh.node.add_node(np.array([2, 3]))
    mesh.node.add_node(np.array([3, 3]))

    mesh.node.add_node(np.array([-1, 0]))
    mesh.node.add_node(np.array([-1, -2]))
    mesh.node.add_node(np.array([-2, -3]))
    mesh.node.add_node(np.array([-3, -3]))

    mesh.add_cell(np.array([0, 1, 2]), "triangle")
    mesh.add_cell(np.array([1, 2, 3]), "triangle")
    mesh.add_cell(np.array([4, 2, 3]), "triangle")
    mesh.add_cell(np.array([0, 5, 6]), "triangle")
    mesh.add_cell(np.array([5, 6, 7]), "triangle")
    mesh.add_cell(np.array([8, 6, 7]), "triangle")

    mesh.cell["triangle"].indice = np.array([11, 12, 13, 98, 100, 101])

    solution = SolutionMat()
    solution.field = np.array([[1, 2, 3], [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4], [7, 8, 9]])
    solution.axis_name = ["indice", "time"]
    solution.axis_size = [6, 3]
    solution.indice = np.array([11, 12, 13, 98, 100, 101])
    solution.type_cell = "triangle"
    solution.label = "B"

    meshsol = MeshSolution()
    meshsol.mesh = [mesh]
    meshsol.solution = [solution]
    meshsol.group = dict()
    meshsol.group["stator"] = np.array([11, 12])
    meshsol.group["rotor"] = np.array([98, 100, 101])

    MS_grp = meshsol.get_group(["stator", "rotor"])
    cells_grp, nb_cell, indices = MS_grp.get_mesh().get_cell()
    solution = np.array([[0, 1, 2], [1, 2, 3], [0, 5, 6], [5, 6, 7], [8, 6, 7]])
    result_tgl = cells_grp["triangle"]
    testA = np.sum(abs(solution - result_tgl))
    msg = "Wrong output: returned " + str(result_tgl) + ", expected: " + str(solution)
    assert testA == pytest.approx(0, rel=DELTA), msg

    field = MS_grp.get_field()
    solution = np.array([[1, 2, 3], [2, 3, 4], [2, 3, 4], [2, 3, 4], [7, 8, 9]])
    testA = np.sum(abs(solution - field))
    msg = "Wrong output: returned " + str(field) + ", expected: " + str(solution)
    assert testA == pytest.approx(0, rel=DELTA), msg

if __name__ == "__main__":
    Xout = test_MeshMat_2group()
