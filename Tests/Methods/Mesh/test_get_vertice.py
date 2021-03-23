# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np


@pytest.mark.MeshSol
@pytest.mark.METHODS
def test_MeshMat():
    """unittest with Meshmat object"""
    mesh = MeshMat()
    mesh.cell["triangle"] = CellMat(nb_node_per_cell=3)
    mesh.cell["segment"] = CellMat(nb_node_per_cell=2)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([1, 0]))
    mesh.node.add_node(np.array([1, 2]))
    mesh.node.add_node(np.array([2, 3]))
    mesh.node.add_node(np.array([3, 3]))

    mesh.add_cell(np.array([0, 1, 2]), "triangle", group_name="stator")
    mesh.add_cell(np.array([1, 2, 3]), "triangle", group_name="stator")
    mesh.add_cell(np.array([4, 2, 3]), "triangle", group_name="rotor")
    mesh.add_cell(np.array([4, 2]), "segment")
    DELTA = 1e-10

    solution = np.array([[3, 3], [1, 2], [2, 3]])
    vert = mesh.get_vertice([2, 3])
    results = vert["triangle"]
    testA = np.sum(abs(solution - results))
    msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
    assert abs(testA - 0) < DELTA, msg

    solution = np.array([[3, 3], [1, 2]])
    results = vert["segment"]
    testA = np.sum(abs(solution - results))
    msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
    assert abs(testA - 0) < DELTA, msg

    solution = np.array(
        [
            [[0, 0], [1, 0], [1, 2]],
            [[1, 0], [1, 2], [2, 3]],
            [[3, 3], [1, 2], [2, 3]],
        ]
    )
    vert = mesh.get_vertice([0, 1, 2])
    results = vert["triangle"]
    testA = np.sum(abs(solution - results))
    msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
    assert abs(testA - 0) < DELTA, msg


if __name__ == "__main__":
    test_MeshMat()
