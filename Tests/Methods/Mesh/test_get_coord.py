# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_get_coord(TestCase):
    """unittest for PointMat get_node methods"""

    def setUp(self):
        self.mesh = Mesh()
        self.mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        self.mesh.node = NodeMat()
        self.mesh.node.add_node(np.array([0, 0]))
        self.mesh.node.add_node(np.array([1, 0]))
        self.mesh.node.add_node(np.array([1, 2]))
        self.mesh.node.add_node(np.array([2, 3]))

        self.mesh.add_element(np.array([0, 1, 2]), "Triangle3")
        self.mesh.add_element(np.array([1, 2, 3]), "Triangle3")

    def test_NodeMat_1node(self):
        """unittest for a node"""
        node_tags = self.mesh.get_connectivity(1)
        # Method test 1
        coord = self.mesh.node.get_coord(node_tags)
        # Check result
        solution = np.array([[1, 0], [1, 2], [2, 3]])
        testA = np.sum(abs(solution - coord))
        msg = "Wrong output: returned " + str(coord) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_NodeMat_false(self):
        """unittest for a false node tag"""

        coord = self.mesh.node.get_coord(-999)
        solution = None
        testA = coord is None
        msg = "Wrong out: returned " + str(coord) + ", expected: " + str(solution)
        self.assertTrue(testA, msg=msg)

    def test_NodeMat_None(self):
        """unittest for a None node tag"""

        coord = self.mesh.node.get_coord(None)
        solution = None
        testA = coord is None
        msg = "Wrong output: returned " + str(coord) + ", expected: " + str(solution)
        self.assertTrue(testA, msg=msg)
