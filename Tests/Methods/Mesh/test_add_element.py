# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_add_element(TestCase):
    """unittest for elements and nodes getter methods"""

    def test_ElementMat(self):
        """unittest with ElementDict and NodeMat objects"""
        # Init
        mesh = Mesh()
        mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        mesh.element["Segment2"] = ElementMat(nb_node_per_element=2)

        # Method test 1
        node_tags = np.array([0, 1])
        mesh.add_element(node_tags, "Segment2")
        # Check result
        testA = np.sum(abs(mesh.element["Segment2"].connectivity - node_tags))
        msg = (
            "Wrong result: returned "
            + str(mesh.element["Segment2"].connectivity)
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        msg = (
            "Wrong result: returned "
            + str(mesh.element["Segment2"].nb_elem)
            + ", expected: "
            + str(1)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(
            mesh.element["Segment2"].nb_elem, 1, msg=msg, delta=DELTA
        )

        # Method test 2
        node_tags = np.array([1, 2])
        mesh.add_element(node_tags, "Segment2")

        # Check result
        solution = np.array([[0, 1], [1, 2]])
        testA = np.sum(abs(mesh.element["Segment2"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(mesh.element["Segment2"].connectivity)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 3
        node_tags = np.array([1, 2, 3])
        mesh.add_element(node_tags, "Triangle3")
        # Check result
        testA = np.sum(abs(mesh.element["Triangle3"].connectivity - node_tags))
        msg = (
            "Wrong result: returned "
            + str(mesh.element["Triangle3"].connectivity)
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 4
        mesh.add_element(np.array([0, 1]), "Segment2")
        # Check result
        testA = np.sum(abs(mesh.element["Segment2"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(mesh.element["Segment2"].connectivity)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 5
        node_tags = np.array([1, 2, 3])
        mesh.add_element(node_tags, "Triangle3")
        # Check result
        testA = np.sum(abs(mesh.element["Triangle3"].connectivity - node_tags))
        msg = (
            "Wrong result: returned "
            + str(mesh.element["Triangle3"].connectivity)
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 6
        node_tags = np.array([2, 3, 0])
        mesh.add_element(node_tags, "Triangle3")
        # Check result
        solution = np.array([[1, 2, 3], [2, 3, 0]])
        testA = np.sum(abs(mesh.element["Triangle3"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(mesh.element["Triangle3"].connectivity)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 7
        node_tags = np.array([2, 0, 1])
        mesh.add_element(node_tags, "Triangle3", group=3)
        # Check result
        solution = np.array([np.NaN, np.NaN, 3])
        result = mesh.element["Triangle3"].group
        testA = ((result == solution) | (np.isnan(result) & np.isnan(solution))).all()
        msg = (
            "Wrong result: returned "
            + str(result)
            + ", expected: "
            + str(solution)
        )
        self.assertTrue(testA, msg=msg)
