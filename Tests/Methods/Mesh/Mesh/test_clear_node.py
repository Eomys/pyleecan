# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np

DELTA = 1e-10


@pytest.mark.MeshSol
def test_MeshMat():
    """Test for 1 group"""

    mesh = MeshMat()
    mesh.cell["triangle"] = CellMat(nb_node_per_cell=3)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([1, 0]))
    mesh.node.add_node(np.array([1, 2]))
    mesh.node.add_node(np.array([2, 3]))
    mesh.node.add_node(np.array([3, 3]))
    mesh.node.add_node(np.array([99, 99]))

    mesh.add_cell(np.array([0, 1, 2]), "triangle")
    mesh.add_cell(np.array([1, 2, 3]), "triangle")
    mesh.add_cell(np.array([4, 2, 3]), "triangle")

    mesh.clear_node()
    nodes_cleared = mesh.get_node()
    nb_nd_clear = len(nodes_cleared)

    msg = "Wrong output: returned " + str(nb_nd_clear) + ", expected: " + str(5)
    assert nb_nd_clear == 5, msg


if __name__ == "__main__":
    out = test_MeshMat()
