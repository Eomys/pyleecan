# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np


class unittest_get_all_node_coord(TestCase):
    """unittest for elements and nodes getter methods"""

    def test_NodeMat_ElementMat(self):
        """unittest with ElementDict and NodeMat objects"""
        # Init
        mesh = Mesh()
        mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        node_tags = np.array([2, 1, 0])
        mesh.add_element(node_tags, "Triangle3", group=int(3))
        node_tags = np.array([1, 2, 3])
        mesh.add_element(node_tags, "Triangle3", group=int(2))
        node_tags = np.array([3, 1, 4])
        mesh.add_element(node_tags, "Triangle3", group=int(2))

        mesh.node = NodeMat()
        nodes_coord = np.array([[0, 0], [1, 0], [0, 1], [1, -1], [2, -1]])
        tags = np.array([2, 1, 0, 3, 4])
        mesh.node.coordinate = nodes_coord
        mesh.node.tag = tags
        mesh.node.nb_node = 5

        # Method test 1
        result, res_tags = mesh.get_all_node_coord()

        # Check result 1
        solution = nodes_coord
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Check result 2
        solution = tags
        testA = np.sum(abs(res_tags - solution))
        msg = "Wrong result: returned " + str(res_tags) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 2
        result, res_tags = mesh.get_all_node_coord(2)

        # Check result 1
        solution = np.array([1, 2, 3, 4])
        testA = np.sum(abs(res_tags - solution))
        msg = "Wrong result: returned " + str(res_tags) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Check result 2
        solution = mesh.node.get_coord(res_tags)
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
