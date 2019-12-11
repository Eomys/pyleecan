# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_get_all_connectivity(TestCase):
    """unittest for elements and nodes getter methods"""

    def test_ElementMat(self):
        """unittest with ElementDict and NodeMat objects"""
        # Init
        mesh = Mesh()
        mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        mesh.element["Segment2"] = ElementMat(nb_node_per_element=2)

        # Method test 1
        solution = np.array([])
        result, tags = mesh.get_all_connectivity("Segment2")
        # Check result
        testA = result.size
        msg = (
            "Wrong output: returned "
            + str(result.size)
            + ", expected: "
            + str(0)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 2
        node_tags = np.array([0, 1])
        mesh.add_element(node_tags, "Segment2")
        result, tags = mesh.get_all_connectivity("Segment2")

        # Check result
        testA = np.sum(abs(result - node_tags))
        msg = (
            "Wrong output: returned "
            + str(mesh.element["Segment2"].connectivity)
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 3
        node_tags = np.array([1, 2])
        mesh.add_element(node_tags, "Segment2")
        result, tags = mesh.get_all_connectivity("Segment2")

        # Check result
        solution = np.array([[0, 1], [1, 2]])
        testA = np.sum(abs(result - solution))
        msg = (
            "Wrong output: returned "
            + str(result)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 4
        node_tags = np.array([1, 2, 3])
        mesh.add_element(node_tags, "Triangle3")
        result, tags = mesh.get_all_connectivity("Triangle3")
        # Check result
        testA = np.sum(abs(result - node_tags))
        msg = (
            "Wrong projection: returned "
            + str(result)
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 5
        mesh.add_element(np.array([0, 1]), "Segment2")
        result, tags = mesh.get_all_connectivity("Segment2")

        # Check result
        testA = np.sum(abs(result - solution))
        msg = (
            "Wrong projection: returned "
            + str(result)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 6
        node_tags = np.array([1, 2, 3])
        mesh.add_element(node_tags, "Triangle3")
        result, tags = mesh.get_all_connectivity("Triangle3")
        # Check result
        testA = np.sum(abs(result - node_tags))
        msg = (
            "Wrong projection: returned "
            + str(result)
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 7
        node_tags = np.array([2, 3, 0])
        mesh.add_element(node_tags, "Triangle3")
        result, tags = mesh.get_all_connectivity("Triangle3")

        # Check result
        solution = np.array([[1, 2, 3], [2, 3, 0]])
        testA = np.sum(abs(result - solution))
        msg = (
            "Wrong projection: returned "
            + str(result)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 8
        node_tags = np.array([2, 1, 0])
        mesh.add_element(node_tags, "Triangle3", group=int(3))

        result, tags = mesh.get_all_connectivity("Triangle3", group=np.array([3], dtype=int))

        # Check result
        solution = node_tags
        testA = np.sum(abs(result - solution))
        msg = (
            "Wrong projection: returned "
            + str(result)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
