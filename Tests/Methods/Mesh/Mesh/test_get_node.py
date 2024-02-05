# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


@pytest.mark.MeshSol
class Test_get_node_coordinate(object):
    """unittest for nodes getter methods"""

    @classmethod
    def setup_method(self, method):
        self.mesh = MeshMat()
        self.mesh.node = NodeMat()
        self.mesh.node.add_node(np.array([0, 0]))
        self.mesh.node.add_node(np.array([1, 0]))
        self.mesh.node.add_node(np.array([1, 2]))
        self.mesh.node.add_node(np.array([2, 3]))
        self.mesh.node.add_node(np.array([3, 3]))

    def test_MeshMat_triangle3(self):
        """unittest with ElementMat and NodeMat objects, only Triangle3 elements are defined"""

        nodes = self.mesh.get_node_coordinate(indices=[1, 2])
        solution = np.array([[1, 0], [1, 2]])

        testA = np.sum(abs(solution - nodes))
        msg = (
            "Wrong projection: returned " + str(nodes) + ", expected: " + str(solution)
        )
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg
