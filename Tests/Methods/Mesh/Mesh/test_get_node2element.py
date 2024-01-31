# -*- coding: utf-8 -*-
import numpy as np
import pytest

from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat


@pytest.mark.MeshSol
class Test_get_node2element(object):
    """unittest to get element containing specific node"""

    def setup_method(self, method):
        self.mesh = MeshMat()
        self.mesh.element_dict["triangle"] = ElementMat(nb_node_per_element=3)
        self.mesh.node = NodeMat()
        self.mesh.node.add_node(np.array([0, 0]))
        self.mesh.node.add_node(np.array([1, 0]))
        self.mesh.node.add_node(np.array([1, 2]))
        self.mesh.node.add_node(np.array([2, 3]))
        self.mesh.node.add_node(np.array([3, 3]))

        self.mesh.add_element(np.array([0, 1, 2]), "triangle")
        self.mesh.add_element(np.array([1, 2, 3]), "triangle")
        self.mesh.add_element(np.array([4, 2, 3]), "triangle")

        self.DELTA = 1e-10

    def test_ElementMat_get_node2element(self):
        """unittest for an existing node"""
        ind_elem = self.mesh.element_dict["triangle"].get_node2element(1)
        solution = np.array([0, 1])
        testA = np.sum(abs(solution - ind_elem))
        msg = "Wrong output: returned " + str(ind_elem) + ", expected: " + str(solution)
        assert abs(testA - 0) < self.DELTA, msg

    def test_MeshMat_get_node2element(self):
        """unittest for an existing node"""
        ind_elem = self.mesh.get_node2element(1)
        solution = np.array([0, 1])
        testA = np.sum(abs(solution - ind_elem))
        msg = "Wrong output: returned " + str(ind_elem) + ", expected: " + str(solution)
        assert abs(testA - 0) < self.DELTA, msg

    def test_MeshMat_fakenode(self):
        """unittest for one non-existing node"""
        ind_elem = self.mesh.element_dict["triangle"].get_node2element(-99)
        solution = None
        testA = np.sum(abs(solution - ind_elem))
        msg = "Wrong output: returned " + str(ind_elem) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg

        elem_tag = self.mesh.element_dict["triangle"].get_node2element(None)
        testA = np.sum(abs(solution - elem_tag))
        msg = "Wrong output: returned " + str(ind_elem) + ", expected: " + str(solution)
        assert abs(testA - 0) < self.DELTA, msg


if __name__ == "__main__":
    test_obj = Test_get_node2element()
    test_obj.setup_method(None)
    test_obj.test_ElementMat_get_node2element()
    test_obj.setup_method(None)
    test_obj.test_MeshMat_get_node2element()
    test_obj.setup_method(None)
    test_obj.test_MeshMat_fakenode()
