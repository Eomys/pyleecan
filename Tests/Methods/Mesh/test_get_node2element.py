# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np


@pytest.mark.METHODS
class Test_get_node2element(object):
    """unittest to get elements containing specific node(s)"""

    def setup_method(self, method):
        self.mesh = Mesh()
        self.mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        self.mesh.add_element(np.array([0, 1, 2]), "Triangle3", group=int(3))
        self.mesh.add_element(np.array([1, 2, 3]), "Triangle3", group=int(3))
        self.mesh.add_element(np.array([4, 2, 3]), "Triangle3", group=int(2))

    def test_ElementMat_1node(self):
        """unittest for one existing node """
        elem_tag = self.mesh.element["Triangle3"].get_node2element(1)
        solution = np.array([0, 1])
        testA = np.sum(abs(solution - elem_tag))
        msg = "Wrong output: returned " + str(elem_tag) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg

    def test_ElementMat_fakenode(self):
        """unittest for one non-existing node """
        elem_tag = self.mesh.element["Triangle3"].get_node2element(-99)
        solution = None
        testA = np.sum(abs(solution - elem_tag))
        msg = "Wrong output: returned " + str(elem_tag) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg

    def test_ElementMat_None(self):
        """unittest for None input """
        elem_tag = self.mesh.element["Triangle3"].get_node2element(None)
        solution = None
        testA = np.sum(abs(solution - elem_tag))
        msg = "Wrong output: returned " + str(elem_tag) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg
