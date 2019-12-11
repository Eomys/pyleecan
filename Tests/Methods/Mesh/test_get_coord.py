# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_get_node(TestCase):
    """unittest for nodes getter methods"""

    def test_NodeMat_ElementMat(self):
        """unittest with ElementMat and NodeMat objects"""
        # Init
        mesh = Mesh()
        mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([0, 0]))
        mesh.node.add_node(np.array([1, 0]))
        mesh.node.add_node(np.array([1, 2]))
        mesh.node.add_node(np.array([2, 3]))

        mesh.add_element(np.array([0, 1, 2]), "Triangle3")
        mesh.add_element(np.array([1, 2, 3]), "Triangle3")

        node_tags = mesh.get_connectivity(1)
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

        # Method test 2
        nodes_coord = mesh.node.get_coord(-999)
        # Check result
        solution = None
        testA = nodes_coord is None
        msg = (
            "Wrong projection: returned "
            + str(nodes_coord)
            + ", expected: "
            + str(solution)
        )
        self.assertTrue(testA, msg=msg)

        # Method test 3
        nodes_coord = mesh.node.get_coord(None)
        # Check result
        solution = None
        testA = nodes_coord is None
        msg = (
            "Wrong projection: returned "
            + str(nodes_coord)
            + ", expected: "
            + str(solution)
        )
        self.assertTrue(testA, msg=msg)
