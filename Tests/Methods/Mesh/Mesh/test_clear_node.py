# -*- coding: utf-8 -*-
import numpy as np
import pytest

from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.NodeMat import NodeMat

DELTA = 1e-10


@pytest.mark.MeshSol
def test_MeshMat():
    """Test for 1 group"""

    mesh = MeshMat()
    mesh.element_dict["triangle"] = ElementMat(nb_node_per_element=3)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([1, 0]))
    mesh.node.add_node(np.array([1, 2]))
    mesh.node.add_node(np.array([2, 3]))
    mesh.node.add_node(np.array([3, 3]))
    mesh.node.add_node(np.array([99, 99]))

    mesh.add_element(np.array([0, 1, 2]), "triangle")
    mesh.add_element(np.array([1, 2, 3]), "triangle")
    mesh.add_element(np.array([4, 2, 3]), "triangle")

    mesh.clear_node()
    nodes_cleared = mesh.get_node_coordinate()
    nb_nd_clear = len(nodes_cleared)

    msg = "Wrong output: returned " + str(nb_nd_clear) + ", expected: " + str(5)
    assert nb_nd_clear == 5, msg


if __name__ == "__main__":
    out = test_MeshMat()
