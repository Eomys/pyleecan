# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np


class unittest_get_all_connectivity(TestCase):
    """unittest for elements and nodes getter methods"""

    def test_ElementMat_NodeMat(self):
        """unittest with ElementDict and NodeMat objects"""
        # Init
        mesh = Mesh()
        mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        mesh.element["Segment2"] = ElementMat(nb_node_per_element=2)
        node_tags = np.array([2, 1, 0])
        mesh.add_element(node_tags, "Triangle3", group=int(3))
        node_tags = np.array([1, 2, 3])
        mesh.add_element(node_tags, "Triangle3", group=int(2))
        node_tags = np.array([3, 1, 4])
        mesh.add_element(node_tags, "Triangle3", group=int(2))
        node_tags = np.array([2, 1])
        tag_test = mesh.add_element(node_tags, "Segment2", group=int(3))

        mesh.node = NodeMat()
        nodes_coord = np.array([[0, 0], [1, 0], [0, 1], [1, -1], [2, -1]])
        tags = np.array([2, 1, 0, 3, 4])
        mesh.node.coordinate = nodes_coord
        mesh.node.tag = tags
        mesh.node.nb_node = 5

        # Method test 1
        solution = np.array([2, 1])
        result = mesh.get_connectivity(tag_test)

        # Check result
        testA = np.sum(abs(result - solution))
        msg = (
            "Wrong output: returned "
            + str(mesh.element["Segment2"].connectivity)
            + ", expected: "
            + str(node_tags)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 2
        node_tags = np.array([1, 2]) # This element already exist
        tag_test = mesh.add_element(node_tags, "Segment2") # This should return None
        result = mesh.get_connectivity(tag_test) #We test what happened with None entry

        # Check result
        solution = None
        testA = result is None
        msg = "Wrong output: returned " + str(result) + ", expected: " + str(solution)
        self.assertTrue(testA, msg=msg)

        # Method test 3
        result = mesh.get_connectivity(-99999) # We test what happened with stupid entry
        # Check result
        testA = result is None
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(node_tags)
        self.assertTrue(testA, msg=msg)

