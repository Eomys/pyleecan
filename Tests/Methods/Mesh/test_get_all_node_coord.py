# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np

@pytest.mark.METHODS
class Test_get_all_node_coord(object):
    """unittest for Mesh get_all_node_coord method. Indirect testing of get_group, get_all_node_tags, get_coord"""
    def setup_method(self, method):
        self.mesh = Mesh()
        self.mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        self.mesh.add_element([2, 1, 0], "Triangle3", group=int(3))
        self.mesh.add_element([1, 2, 3], "Triangle3", group=int(2))
        self.mesh.add_element([3, 1, 4], "Triangle3", group=int(2))

        self.mesh.node = NodeMat()
        self.mesh.node.add_node([0, 0])
        self.mesh.node.add_node([1, 0])
        self.mesh.node.add_node([0, 1])
        self.mesh.node.add_node([1, -1])
        self.mesh.node.add_node([2, -1])

    def test_NodeMat_ElementMat_coord(self):
        """unittest with NodeMat and ElementMat objects"""

        result, res_tags = self.mesh.get_all_node_coord()
        solution = np.array([[0, 0], [1, 0], [0, 1], [1, -1], [2, -1]])
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA-0) < DELTA, msg

    def test_NodeMat_ElementMat_tags(self):
        """unittest with NodeMat and ElementMat objects"""

        result, res_tags = self.mesh.get_all_node_coord()
        solution = np.array([0, 1, 2, 3, 4])
        testA = np.sum(abs(res_tags - solution))
        msg = "Wrong result: returned " + str(res_tags) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA-0) < DELTA, msg

    def test_NodeMat_ElementMat_group(self):
        """unittest with NodeMat and ElementMat objects"""
        
        result, res_tags = self.mesh.get_all_node_coord(2)
        solution = np.array([1, 2, 3, 4])
        testA = np.sum(abs(res_tags - solution))
        msg = "Wrong result: returned " + str(res_tags) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA-0) < DELTA, msg
