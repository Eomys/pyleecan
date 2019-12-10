# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementDict import ElementDict
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_add_element(TestCase):
    """unittest for elements and nodes getter methods"""

    def test_ElementDict_NodeMat(self):
        """unittest with ElementDict and NodeMat objects"""
        # Init
        mesh = Mesh()
        mesh.element = ElementDict()
        # mesh.node = NodeMat()
        # mesh.node.coordinate = np.array([[0, 0], [1, 0], [1, 2], [2, 3]])
        # mesh.element.connectivity = {"Triangle": np.array([[0, 1, 2], [1, 2, 3]])}
        #         # mesh.element.tag = {"Triangle": np.array([1, 2])}
        #         # mesh.element.nb_elem = {"Triangle": 2}
        #         # mesh.element.nb_node_per_element = {"Triangle": 3}

        # Method test 1
        node_tags = np.array([0, 1])
        mesh.element.add_element(node_tags)
        # Check result
        testA = np.sum(abs(mesh.element.connectivity["Segment"] - node_tags))
        msg = (
            "Wrong projection: returned "
            + str(mesh.element.connectivity["Segment"])
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 2
        node_tags = np.array([1, 2])
        mesh.element.add_element(node_tags)

        # Check result
        solution = np.array([[0, 1], [1, 2]])
        testA = np.sum(abs(solution - mesh.element.connectivity["Segment"]))
        msg = (
            "Wrong projection: returned "
            + str(mesh.element.connectivity["Segment"])
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 3
        node_tags = np.array([1, 2, 3])
        mesh.element.add_element(node_tags)
        # Check result
        testA = np.sum(abs(mesh.element.connectivity["Triangle"] - node_tags))
        msg = (
            "Wrong projection: returned "
            + str(mesh.element.connectivity["Segment"])
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 4
        mesh.element.add_element(np.array([0, 1]))
        # Check result
        testA = np.sum(abs(mesh.element.connectivity["Segment"] - solution))
        msg = (
            "Wrong projection: returned "
            + str(mesh.element.connectivity["Segment"])
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 5
        node_tags = np.array([1, 2, 3])
        mesh.element.add_element(node_tags)
        # Check result
        testA = np.sum(abs(mesh.element.connectivity["Triangle"] - node_tags))
        msg = (
            "Wrong projection: returned "
            + str(mesh.element.connectivity["Triangle"])
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 6
        node_tags = np.array([2, 3, 0])
        mesh.element.add_element(node_tags)
        # Check result
        solution = np.array([[1, 2, 3], [2, 3, 0]])
        testA = np.sum(abs(mesh.element.connectivity["Triangle"] - solution))
        msg = (
            "Wrong projection: returned "
            + str(mesh.element.connectivity["Triangle"])
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat_NodeMat(self):
        """unittest with ElementMat and NodeMat objects"""
        # Init
        # TODO
