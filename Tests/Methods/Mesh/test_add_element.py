# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_add_element(TestCase):
    """unittest for add_element methods in Mesh and Element classes"""

    def setUp(self):
        self.mesh = Mesh()
        self.mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        self.mesh.element["Segment2"] = ElementMat(nb_node_per_element=2)

    def test_Mesh_ElementMat_1seg(self):
        """unittest with ElementMat and only 1 segment element"""

        node_tags = np.array([0, 1])
        self.mesh.add_element(node_tags, "Segment2")
        # Check result
        testA = np.sum(abs(self.mesh.element["Segment2"].connectivity - node_tags))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.element["Segment2"].connectivity)
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        msg = (
            "Wrong result: returned "
            + str(self.mesh.element["Segment2"].nb_elem)
            + ", expected: "
            + str(1)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(
            self.mesh.element["Segment2"].nb_elem, 1, msg=msg, delta=DELTA
        )

    def test_Mesh_ElementMat_2elem(self):
        """unittest with ElementMat and 2 segment element"""

        node_tags = np.array([0, 1])
        self.mesh.add_element(node_tags, "Segment2")
        node_tags = np.array([1, 2])
        self.mesh.add_element(node_tags, "Segment2")

        # Check result
        solution = np.array([[0, 1], [1, 2]])
        testA = np.sum(abs(self.mesh.element["Segment2"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.element["Segment2"].connectivity)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_Mesh_ElementMat_2elem_1tgl(self):
        """unittest with ElementMat and 2 segment element and 1 triangle"""

        self.mesh.add_element(np.array([0, 1]), "Segment2")
        self.mesh.add_element(np.array([1, 2]), "Segment2")
        solution = np.array([1, 2, 3])
        self.mesh.add_element(solution, "Triangle3")

        testA = np.sum(abs(self.mesh.element["Triangle3"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.element["Triangle3"].connectivity)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_Mesh_ElementMat_2elem_1tgl_add_seg_exist(self):
        """unittest with ElementMat and 2 segment element and 1 triangle, try to add an already existing segment."""

        self.mesh.add_element(np.array([0, 1]), "Segment2")
        self.mesh.add_element(np.array([1, 2]), "Segment2")
        self.mesh.add_element(np.array([1, 2, 3]), "Triangle3")
        self.mesh.add_element(np.array([0, 1]), "Segment2")  # already exist

        solution = np.array([[0, 1], [1, 2]])
        testA = np.sum(abs(self.mesh.element["Segment2"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.element["Segment2"].connectivity)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_Mesh_ElementMat_2elem_1tgl_add_tgl_exist(self):
        """unittest with ElementMat and 2 segment element and 1 triangle, try to add an already existing triangle."""

        self.mesh.add_element(np.array([0, 1]), "Segment2")
        self.mesh.add_element(np.array([1, 2]), "Segment2")
        self.mesh.add_element(np.array([1, 2, 3]), "Triangle3")
        self.mesh.add_element(np.array([2, 3, 1]), "Triangle3")  # already exist

        solution = np.array([1, 2, 3])
        testA = np.sum(abs(self.mesh.element["Triangle3"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.element["Triangle3"].connectivity)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_Mesh_ElementMat_2elem_2tgl(self):
        """unittest with ElementMat and 2 segment element and 1 triangle, add 1 triangle."""

        self.mesh.add_element(np.array([0, 1]), "Segment2")
        self.mesh.add_element(np.array([1, 2]), "Segment2")
        self.mesh.add_element(np.array([1, 2, 3]), "Triangle3")
        self.mesh.add_element(np.array([2, 3, 0]), "Triangle3")  # already exist

        solution = np.array([[1, 2, 3], [2, 3, 0]])
        testA = np.sum(abs(self.mesh.element["Triangle3"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.element["Triangle3"].connectivity)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_Mesh_ElementMat_2elem_2tgl_add_tgl_group(self):
        """unittest with ElementMat and 2 segment element and 1 triangle, add 1 triangle with a group number."""

        self.mesh.add_element(np.array([0, 1]), "Segment2")
        self.mesh.add_element(np.array([1, 2]), "Segment2")
        self.mesh.add_element(np.array([1, 2, 3]), "Triangle3")
        self.mesh.add_element(np.array([2, 3, 0]), "Triangle3")  # already exist
        self.mesh.add_element(np.array([2, 0, 1]), "Triangle3", group=3)

        solution = np.array([-1, -1, 3], dtype=int)
        result = self.mesh.element["Triangle3"].group
        testA = (result == solution).all()
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        self.assertTrue(testA, msg=msg)

    def test_Mesh_ElementMat_add_stupid(self):
        """unittest with ElementMat and 2 segment element and 1 triangle, add 1 triangle with a group number."""

        self.mesh.add_element(np.array([0, 1]), "Segment2")
        self.mesh.add_element(None, "Segment2")
        self.mesh.add_element(np.array([0, 1, 2]), "Segment2")
        self.mesh.add_element(np.array([1, 1]), "Segment2")

        solution = np.array([0, 1], dtype=int)
        result = self.mesh.element["Segment2"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
