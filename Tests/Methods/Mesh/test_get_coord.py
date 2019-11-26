# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementDict import ElementDict
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_get_node(TestCase):
    """unittest for nodes getter methods"""

    def test_NodeMat_ElementDict(self):
        # Init
        mesh = Mesh()
        mesh.element = ElementDict()
        mesh.node = NodeMat()
        mesh.node.coordinate = np.array([[0, 0], [1, 0], [1, 2], [2, 3]])
        mesh.element.connectivity = {"Triangle": np.array([[0, 1, 2], [1, 2, 3]])}
        mesh.element.tag = {"Triangle": np.array([1, 2])}
        mesh.element.nb_elem = {"Triangle": 2}
        mesh.element.nb_node_per_element = {"Triangle": 3}
        node_tags = mesh.element.get_node_tags(2)
        # Method to test
        nodes_coord = mesh.node.get_coord(node_tags)
        # Check result
        solution = np.array([[1, 0], [1, 2], [2, 3]])
        testA = np.sum(abs(solution - nodes_coord))
        msg = (
            "Wrong projection: returned "
            + str(nodes_coord)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_NodeMat_ElementMat(self):
        """unittest with ElementMat and NodeMat objects"""
        # Init
        mesh = Mesh()
        mesh.element = ElementMat()
        mesh.node = NodeMat()
        mesh.node.coordinate = np.array([[0, 0], [1, 0], [1, 2], [2, 3]])
        mesh.element.connectivity = np.array([[0, 1, 2], [1, 2, 3]])
        mesh.element.nb_elem = 2
        mesh.element.nb_node_per_element = 3
        node_tags = mesh.element.get_node_tags(1)
        # Method test 1
        nodes_coord = mesh.node.get_coord(node_tags)
        # Check result
        solution = np.array([[1, 0], [1, 2], [2, 3]])
        testA = np.sum(abs(solution - nodes_coord))
        msg = (
            "Wrong projection: returned "
            + str(node_tags)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
