# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


@pytest.mark.MeshSol
class Test_interface(object):
    """unittest for elements and nodes getter methods"""

    def setup_method(self, method):
        self.mesh = MeshMat()
        self.mesh.element["triangle"] = ElementMat(nb_node_per_element=3)
        self.mesh.element["line"] = ElementMat(nb_node_per_element=2)
        self.mesh.node = NodeMat()

        self.other_mesh = MeshMat()
        self.other_mesh.element["triangle"] = ElementMat(nb_node_per_element=3)
        self.other_mesh.element["line"] = ElementMat(nb_node_per_element=2)
        self.other_mesh.node = self.mesh.node

    def test_MeshMat_flat(self):
        """unittest with a flat interface"""

        self.mesh.add_element([0, 1, 2], "triangle")
        self.mesh.add_element([2, 3, 4], "triangle")

        self.mesh.node.add_node([0, 0])
        self.mesh.node.add_node([0.5, 1])
        self.mesh.node.add_node([1, 0])
        self.mesh.node.add_node([1.5, 1])
        self.mesh.node.add_node([2, 0])
        self.mesh.node.add_node([0.5, -1])
        self.mesh.node.add_node([1.5, -1])

        self.other_mesh.add_element([0, 5, 2], "triangle")
        self.other_mesh.add_element([4, 6, 2], "triangle")

        new_seg_mesh = self.mesh.interface(self.other_mesh)
        solution = np.array([[0, 2], [4, 2]])
        resultat = new_seg_mesh.element["line"].connectivity
        testA = np.sum(abs(resultat - solution))
        msg = (
            "Wrong projection: returned "
            + str(resultat)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg

    def test_ElementMat_NodeMat_corner_ext(self):
        """unittest with an external corner interface"""
        self.mesh.add_element([0, 1, 2], "triangle")
        self.mesh.add_element([1, 2, 3], "triangle")
        self.mesh.add_element([1, 5, 4], "triangle")

        self.mesh.node.add_node([2, 0])
        self.mesh.node.add_node([3, 0])
        self.mesh.node.add_node([2.5, 1])
        self.mesh.node.add_node([4, 0])
        self.mesh.node.add_node([3.5, 1])
        self.mesh.node.add_node([3, -1])
        self.mesh.node.add_node([10, 10])

        self.other_mesh.add_element([0, 1, 5], "triangle")
        self.other_mesh.add_element([0, 5, 6], "triangle")

        # Method test 1
        new_seg_mesh = self.mesh.interface(self.other_mesh)

        # Check result
        solution = np.array([[0, 1], [1, 5]])
        result = new_seg_mesh.element["line"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg

    def test_ElementMat_NodeMat_corner_int(self):
        """unittest with an internal corner interface"""
        self.mesh.add_element([0, 1, 2], "triangle")
        self.mesh.add_element([1, 2, 3], "triangle")
        self.mesh.add_element([1, 5, 4], "triangle")

        self.mesh.node.add_node([2, 0])
        self.mesh.node.add_node([3, 0])
        self.mesh.node.add_node([2.5, 1])
        self.mesh.node.add_node([4, 0])
        self.mesh.node.add_node([3.5, 1])
        self.mesh.node.add_node([3, -1])
        self.mesh.node.add_node([10, 10])

        self.other_mesh.add_element([0, 1, 5], "triangle")
        self.other_mesh.add_element([0, 5, 6], "triangle")

        # Method test 1
        new_seg_mesh = self.other_mesh.interface(self.mesh)

        # Check result
        solution = np.array([[0, 1], [1, 5]])
        result = new_seg_mesh.element["line"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg

    def test_ElementMat_NodeMat_self(self):
        """unittest with interface of a mesh on itself"""
        self.mesh.add_element([0, 1, 2], "triangle")
        self.mesh.add_element([0, 2, 3], "triangle")

        self.mesh.node.add_node([0, 0])
        self.mesh.node.add_node([0, 1])
        self.mesh.node.add_node([1, 0])
        self.mesh.node.add_node([-1, 0])

        # Method test 1
        new_seg_mesh = self.mesh.interface(self.mesh)

        # Check result
        solution = np.array([[0, 1], [0, 2], [0, 3], [1, 2], [2, 3]])
        result = new_seg_mesh.element["line"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg
