# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_get_node_tags(TestCase):
    """unittest for elements and nodes getter methods"""

    def setUp(self):
        self.mesh = Mesh()
        self.mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        self.mesh.element["Segment2"] = ElementMat(nb_node_per_element=2)
        self.mesh.node = NodeMat()
        self.mesh.node.add_node(np.array([0, 0]))
        self.mesh.node.add_node(np.array([1, 0]))
        self.mesh.node.add_node(np.array([1, 2]))
        self.mesh.node.add_node(np.array([2, 3]))
        self.mesh.node.add_node(np.array([3, 3]))

        self.mesh.add_element(np.array([0, 1, 2]), "Triangle3", group=int(3))
        self.mesh.add_element(np.array([1, 2, 3]), "Triangle3", group=int(3))
        self.mesh.add_element(np.array([4, 2, 3]), "Triangle3", group=int(2))
        self.mesh.add_element(np.array([4, 3]), "Segment2", group=int(2))

    def test_ElementMat_NodeMat_Triangle3(self):
        """unittest with CellMat and PointMat objects, only Triangle3 elements are defined"""

        node_tags = self.mesh.get_node_tags(elem_tag=np.array([1, 2], dtype=int))
        solution = np.array([1, 2, 3, 4])

        testA = np.sum(abs(solution - node_tags))
        msg = (
            "Wrong projection: returned "
            + str(node_tags)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat_NodeMat_MixedElement(self):
        """unittest with CellMat and PointMat objects, both Triangle3 and Segment2 elements are defined"""
        # Method test 2
        node_tags = self.mesh.get_node_tags(np.array([2, 3]))
        # Check result
        solution = np.array([2, 3, 4])
        testA = np.sum(abs(solution - node_tags))
        msg = (
            "Wrong projection: returned "
            + str(node_tags)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
