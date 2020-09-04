# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np

@pytest.mark.METHODS
class Test_interface(object):
    """unittest for elements and nodes getter methods"""
    def setup_method(self, method):
        self.mesh = Mesh()
        self.mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        self.mesh.element["Segment2"] = ElementMat(nb_node_per_element=2)
        self.mesh.node = NodeMat()

        self.other_mesh = Mesh()
        self.other_mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        self.other_mesh.element["Segment2"] = ElementMat(nb_node_per_element=2)
        self.other_mesh.node = self.mesh.node

    def test_ElementMat_NodeMat_flat(self):
        """unittest with ElementDict and NodeMat objects"""

        self.mesh.add_element([0, 1, 2], "Triangle3")
        self.mesh.add_element([2, 3, 4], "Triangle3")

        self.mesh.node.add_node([0, 0])
        self.mesh.node.add_node([0.5, 1])
        self.mesh.node.add_node([1, 0])
        self.mesh.node.add_node([1.5, 1])
        self.mesh.node.add_node([2, 0])
        self.mesh.node.add_node([0.5, -1])
        self.mesh.node.add_node([1.5, -1])

        self.other_mesh.add_element([0, 5, 2], "Triangle3")
        self.other_mesh.add_element([4, 6, 2], "Triangle3")

        new_seg_mesh = self.mesh.interface(self.other_mesh)
        solution = np.array([[0, 2], [2, 4]])
        resultat = new_seg_mesh.element["Segment2"].connectivity
        testA = np.sum(abs(resultat - solution))
        msg = (    
            "Wrong projection: returned "    
            + str(resultat)    
            + ", expected: "    
            + str(solution)    
        )
        DELTA = 1e-10
        assert abs(testA-0) < DELTA, msg

    def test_ElementMat_NodeMat_corner_ext(self):
        """unittest with ElementMat and NodeMat objects, extract interface from the external mesh point of view"""
        self.mesh.add_element([0, 1, 2], "Triangle3")
        self.mesh.add_element([1, 2, 3], "Triangle3")
        self.mesh.add_element([1, 5, 4], "Triangle3")

        self.mesh.node.add_node([2, 0])
        self.mesh.node.add_node([3, 0])
        self.mesh.node.add_node([2.5, 1])
        self.mesh.node.add_node([4, 0])
        self.mesh.node.add_node([3.5, 1])
        self.mesh.node.add_node([3, -1])

        self.other_mesh.add_element([0, 1, 5], "Triangle3")

        # Method test 1
        new_seg_mesh = self.mesh.interface(self.other_mesh)

        # Check result
        solution = np.array([[0, 1], [1, 5]])
        result = new_seg_mesh.element["Segment2"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA-0) < DELTA, msg

    def test_ElementMat_NodeMat_corner_int(self):
        """unittest with ElementMat and NodeMat objects, extract interface from the internal mesh point of view"""
        self.mesh.add_element([0, 1, 2], "Triangle3")
        self.mesh.add_element([1, 2, 3], "Triangle3")
        self.mesh.add_element([1, 5, 4], "Triangle3")

        self.mesh.node.add_node([2, 0])
        self.mesh.node.add_node([3, 0])
        self.mesh.node.add_node([2.5, 1])
        self.mesh.node.add_node([4, 0])
        self.mesh.node.add_node([3.5, 1])
        self.mesh.node.add_node([3, -1])

        self.other_mesh.add_element([0, 1, 5], "Triangle3")

        # Method test 1
        new_seg_mesh = self.other_mesh.interface(self.mesh)

        # Check result
        solution = np.array([[0, 1], [1, 5]])
        result = new_seg_mesh.element["Segment2"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA-0) < DELTA, msg

    def test_ElementMat_NodeMat_self(self):
        """unittest with ElementMat and NodeMat objects, extract interface on itself"""
        self.mesh.add_element([0, 1, 2], "Triangle3")
        self.mesh.add_element([0, 2, 3], "Triangle3")
        self.mesh.add_element([0, 3, 4], "Triangle3")
        self.mesh.add_element([0, 4, 1], "Triangle3")

        self.mesh.node.add_node([0, 0])
        self.mesh.node.add_node([0, 1])
        self.mesh.node.add_node([1, 0])
        self.mesh.node.add_node([-1, 0])
        self.mesh.node.add_node([0, -1])

        # Method test 1
        new_seg_mesh = self.mesh.interface(self.mesh)

        # Check result
        solution = np.array([])
        result = new_seg_mesh.element["Segment2"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA-0) < DELTA, msg
