# -*- coding: utf-8 -*-

from unittest import TestCase
from ....Classes.Mesh import Mesh
from ....Classes.ElementMat import ElementMat
import numpy as np


class unittest_get_all_connectivity(TestCase):
    """unittest for Mesh and Element get_all_connectivity methods"""

    def setUp(self):
        self.mesh = Mesh()
        self.mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        self.mesh.element["Segment2"] = ElementMat(nb_node_per_element=2)

    def test_ElementMat_empty(self):
        """unittest with ElementMat object. Test for empty Mesh"""

        solution = np.array([])
        result, tags = self.mesh.get_all_connectivity("Segment2")
        testA = result.size
        msg = "Wrong output: returned " + str(result.size) + ", expected: " + str(0)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat_1seg(self):
        """unittest with ElementMat object. Test for 1 segment."""

        node_tags = np.array([0, 1])
        self.mesh.add_element(node_tags, "Segment2")
        result, tags = self.mesh.get_all_connectivity("Segment2")

        testA = np.sum(abs(result - node_tags))
        msg = "Wrong output: returned " + str(result) + ", expected: " + str(node_tags)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat_2seg(self):
        """unittest with ElementMat object. Test with 2 segment."""

        self.mesh.add_element([0, 1], "Segment2")
        self.mesh.add_element([1, 2], "Segment2")
        result, tags = self.mesh.get_all_connectivity("Segment2")
        solution = np.array([[0, 1], [1, 2]])
        testA = np.sum(abs(result - solution))
        msg = "Wrong output: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat_2seg_1tgl(self):
        """unittest with ElementMat object. Test with 2 segment and 1 tgl."""

        self.mesh.add_element([0, 1], "Segment2")
        self.mesh.add_element([1, 2], "Segment2")
        node_tags = np.array([1, 2, 3])
        self.mesh.add_element(node_tags, "Triangle3")
        result, tags = self.mesh.get_all_connectivity("Triangle3")
        testA = np.sum(abs(result - node_tags))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(node_tags)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat_2seg_2tgl(self):
        """unittest with ElementMat object. Test with 2 segment and 2 tgl."""

        self.mesh.add_element([0, 1], "Segment2")
        self.mesh.add_element([1, 2], "Segment2")
        self.mesh.add_element([1, 2, 3], "Triangle3")
        self.mesh.add_element([2, 3, 0], "Triangle3")
        result, tags = self.mesh.get_all_connectivity("Triangle3")
        solution = np.array([[1, 2, 3], [2, 3, 0]])
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat_3seg_2tgl_1group(self):
        """unittest with ElementMat object. Test for 1 triangle in a group."""

        self.mesh.add_element([0, 1], "Segment2")
        self.mesh.add_element([1, 2], "Segment2")
        self.mesh.add_element([1, 2, 3], "Triangle3")
        self.mesh.add_element([2, 3, 0], "Triangle3")
        node_tags = np.array([2, 1, 0])
        self.mesh.add_element(node_tags, "Triangle3", group=3)
        result, tags = self.mesh.get_all_connectivity(
            "Triangle3", group=np.array([3], dtype=int)
        )
        solution = node_tags
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        result, tags = self.mesh.get_all_connectivity("Triangle3", group=3)
        solution = node_tags
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat_3seg_2tgl_2group(self):
        """unittest with ElementMat object. Test for 2 triangle in a group."""

        self.mesh.add_element([0, 1], "Segment2")
        self.mesh.add_element([1, 2], "Segment2")
        self.mesh.add_element([1, 2, 3], "Triangle3")
        self.mesh.add_element([2, 3, 0], "Triangle3", group=3)
        self.mesh.add_element([2, 1, 0], "Triangle3", group=3)
        result, tags = self.mesh.get_all_connectivity("Triangle3", group=3)
        solution = np.array([[2, 3, 0], [2, 1, 0]])
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
