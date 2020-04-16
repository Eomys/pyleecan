# -*- coding: utf-8 -*-

from unittest import TestCase
from ....Classes.Mesh import Mesh
from ....Classes.ElementMat import ElementMat
from ....Classes.NodeMat import NodeMat
import numpy as np


class unittest_get_all_connectivity(TestCase):
    """unittest for Mesh and Element get_all_connectivity methods. Indirect test add_element """

    def setUp(self):
        self.mesh = Mesh()
        self.mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        self.mesh.element["Segment2"] = ElementMat(nb_node_per_element=2)
        self.mesh.add_element([2, 1, 0], "Triangle3", group=int(3))
        self.mesh.add_element([1, 2, 3], "Triangle3", group=int(2))
        self.mesh.add_element([3, 1, 4], "Triangle3", group=int(2))
        self.mesh.add_element([0, 1], "Segment2", group=int(3))

        self.mesh.node = NodeMat()
        self.mesh.node.add_node([0, 0])
        self.mesh.node.add_node([1, 0])
        self.mesh.node.add_node([0, 1])
        self.mesh.node.add_node([1, -1])
        self.mesh.node.add_node([2, -1])

    def test_ElementMat_NodeMat_1seg(self):
        """unittest with ElementDict and NodeMat objects, get 1 segment"""
        tag_test = self.mesh.add_element([2, 1], "Segment2", group=int(3))
        result = self.mesh.get_connectivity(tag_test)
        solution = np.array([2, 1])
        testA = np.sum(abs(result - solution))
        msg = "Wrong output: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat_NodeMat_1tgl(self):
        """unittest with ElementDict and NodeMat objects, with input None"""
        result = self.mesh.get_connectivity(None)

        testA = result is None
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(None)
        self.assertTrue(testA, msg=msg)

    def test_ElementMat_NodeMat_1seg_stupid(self):
        """unittest with ElementDict and NodeMat objects, with only 1 segment"""
        result = self.mesh.get_connectivity(
            -99999
        )  # We test what happened with stupid entry
        # Check result
        testA = result is None
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(None)
        self.assertTrue(testA, msg=msg)
