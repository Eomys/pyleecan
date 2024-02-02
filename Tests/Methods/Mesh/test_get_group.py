# -*- coding: utf-8 -*-
import numpy as np
import pytest

from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.SolutionMat import SolutionMat

DELTA = 1e-10


@pytest.mark.MeshSol
def test_MeshMat_1group():
    """unittest for 1 group"""

    mesh = MeshMat()
    mesh.element_dict["triangle"] = ElementMat(nb_node_per_element=3)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([1, 0]))
    mesh.node.add_node(np.array([1, 2]))
    mesh.node.add_node(np.array([2, 3]))
    mesh.node.add_node(np.array([3, 3]))

    mesh.add_element(np.array([0, 1, 2]), "triangle")
    mesh.add_element(np.array([1, 2, 3]), "triangle")
    mesh.add_element(np.array([4, 2, 3]), "triangle")

    meshsol = MeshSolution()
    meshsol.mesh = mesh
    meshsol.group = dict()
    meshsol.group["stator"] = np.array([0, 1])
    meshsol.group["rotor"] = np.array([2])

    MS_grp = meshsol.get_group("stator")
    elements_grp, nb_element, indices = MS_grp.mesh.get_element()
    solution = np.array([[0, 1, 2], [1, 2, 3]])
    result_tgl = elements_grp["triangle"]
    testA = np.sum(abs(solution - result_tgl))
    msg = "Wrong output: returned " + str(result_tgl) + ", expected: " + str(solution)
    assert testA == pytest.approx(0, rel=DELTA), msg

    MS_grp = meshsol.get_group("rotor")
    elements_grp, nb_element, indices = MS_grp.mesh.get_element()
    solution = np.array([[3, 3], [1, 2], [2, 3]])
    results = elements_grp["triangle"]  # The node indices have changed !
    nodes = MS_grp.mesh.get_node_coordinate(results)
    testA = np.sum(abs(solution - nodes))
    msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
    assert testA == pytest.approx(0, rel=DELTA), msg


def test_MeshMat_2group():
    """unittest for 1 group"""

    mesh = MeshMat()
    mesh.element_dict["triangle"] = ElementMat(nb_node_per_element=3)
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

    mesh.add_element(np.array([0, 1, 2]), "triangle")
    mesh.add_element(np.array([1, 2, 3]), "triangle")
    mesh.add_element(np.array([4, 2, 3]), "triangle")
    mesh.add_element(np.array([0, 5, 6]), "triangle")
    mesh.add_element(np.array([5, 6, 7]), "triangle")
    mesh.add_element(np.array([8, 6, 7]), "triangle")

    mesh.element_dict["triangle"].indice = np.array([11, 12, 13, 98, 100, 101])

    solution = SolutionMat()
    solution.field = np.array(
        [[1, 2, 3], [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4], [7, 8, 9]]
    )
    solution.axis_name = ["indice", "time"]
    solution.axis_size = [6, 3]
    solution.indice = np.array([11, 12, 13, 98, 100, 101])
    solution.type_element = "triangle"
    solution.label = "B"

    meshsol = MeshSolution()
    meshsol.mesh = mesh
    meshsol.solution_dict = {solution.label: solution}
    meshsol.group = dict()
    meshsol.group["stator"] = [11, 12]
    meshsol.group["rotor"] = [98, 100, 101]

    MS_grp = meshsol.get_group(["stator", "rotor"])
    elements_grp, nb_element, indices = MS_grp.mesh.get_element()
    solution = np.array([[0, 1, 2], [1, 2, 3], [0, 5, 6], [5, 6, 7], [8, 6, 7]])
    result_tgl = elements_grp["triangle"]
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
