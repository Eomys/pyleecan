# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np


@pytest.mark.MeshSol
@pytest.mark.METHODS
class Test_get_vertice(object):
    """unittest for Mesh and Element get_all_connectivity methods"""

    def setup_method(self, method):
        self.mesh = MeshMat()
        self.mesh.cell["triangle"] = CellMat(nb_node_per_cell=3)
        self.mesh.cell["segment"] = CellMat(nb_node_per_cell=2)
        self.mesh.node = NodeMat()
        self.mesh.node.add_node(np.array([0, 0]))
        self.mesh.node.add_node(np.array([1, 0]))
        self.mesh.node.add_node(np.array([1, 2]))
        self.mesh.node.add_node(np.array([2, 3]))
        self.mesh.node.add_node(np.array([3, 3]))

        self.mesh.add_cell(np.array([0, 1, 2]), "triangle", group_name="stator")
        self.mesh.add_cell(np.array([1, 2, 3]), "triangle", group_name="stator")
        self.mesh.add_cell(np.array([4, 2, 3]), "triangle", group_name="rotor")
        self.mesh.add_cell(np.array([4, 2]), "segment")
        self.DELTA = 1e-10

    def test_MeshMat(self):
        """unittest with Meshmat object"""

        solution = np.array([[3, 3], [1, 2], [2, 3]])
        vert = self.mesh.get_vertice([2, 3])
        results = vert["triangle"]
        testA = np.sum(abs(solution - results))
        msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
        assert abs(testA - 0) < self.DELTA, msg

        solution = np.array([[3, 3], [1, 2]])
        results = vert["segment"]
        testA = np.sum(abs(solution - results))
        msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
        assert abs(testA - 0) < self.DELTA, msg

        solution = np.array(
            [
                [[0, 0], [1, 0], [1, 2]],
                [[1, 0], [1, 2], [2, 3]],
                [[3, 3], [1, 2], [2, 3]],
            ]
        )
        vert = self.mesh.get_vertice([0, 1, 2])
        results = vert["triangle"]
        testA = np.sum(abs(solution - results))
        msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
        assert abs(testA - 0) < self.DELTA, msg
