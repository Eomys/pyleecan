# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementDict import ElementDict
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_interface(TestCase):
    """unittest for elements and nodes getter methods"""

    def test_ElementDict_NodeMat_flat(self):
        """unittest with ElementDict and NodeMat objects"""
        # Init
        mesh = Mesh()
        mesh.element = ElementDict()
        mesh.node = NodeMat()
        mesh.node.coordinate = np.array(
            [[0, 0], [0.5, 0.5], [1, 0], [1.5, 0.5], [2, 0], [0.5, -0.5], [1.5, -0.5]]
        )
        mesh.element.connectivity = {"Triangle": np.array([[0, 1, 2], [2, 3, 4]])}
        mesh.element.tag = {"Triangle": np.array([1, 2])}
        mesh.element.nb_elem = {"Triangle": 2}
        mesh.element.nb_node_per_element = {"Triangle": 3}

        other_mesh = Mesh()
        other_mesh.element = ElementDict()
        other_mesh.node = mesh.node
        other_mesh.element.connectivity = {"Triangle": np.array([[0, 5, 2], [4, 6, 2]])}
        other_mesh.element.tag = {"Triangle": np.array([3, 4])}
        other_mesh.element.nb_elem = {"Triangle": 2}
        other_mesh.element.nb_node_per_element = {"Triangle": 3}

        # Method test 1
        new_seg_mesh = mesh.interface(other_mesh)

        # Check result
        solution = np.array([[0, 2], [2, 4]])
        testA = np.sum(abs(new_seg_mesh.element.connectivity["Segment"] - solution))
        msg = (
            "Wrong projection: returned "
            + str(new_seg_mesh.element.connectivity["Segment"])
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementDict_NodeMat_corner(self):
        """unittest with ElementDict and NodeMat objects"""
        # Init
        mesh = Mesh()
        mesh.element = ElementDict()
        mesh.node = NodeMat()
        mesh.node.coordinate = np.array([[0, 0], [1, 0], [1, -1], [1, 1], [2, 0]])
        mesh.element.connectivity = {"Triangle": np.array([[0, 1, 2]])}
        mesh.element.tag = {"Triangle": np.array([1])}
        mesh.element.nb_elem = {"Triangle": 2}
        mesh.element.nb_node_per_element = {"Triangle": 3}

        other_mesh = Mesh()
        other_mesh.element = ElementDict()
        other_mesh.node = mesh.node
        other_mesh.element.connectivity = {
            "Triangle": np.array([[0, 1, 3], [2, 1, 4], [3, 1, 4]])
        }
        other_mesh.element.tag = {"Triangle": np.array([3, 4, 5])}
        other_mesh.element.nb_elem = {"Triangle": 2}
        other_mesh.element.nb_node_per_element = {"Triangle": 3}

        # Method test 1
        new_seg_mesh = mesh.interface(other_mesh)

        # Check result
        solution = np.array([[0, 1], [2, 1]])
        testA = np.sum(abs(new_seg_mesh.element.connectivity["Segment"] - solution))
        msg = (
            "Wrong projection: returned "
            + str(new_seg_mesh.element.connectivity["Segment"])
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat_NodeMat(self):
        """unittest with ElementMat and NodeMat objects"""
        # Init
        # TODO
