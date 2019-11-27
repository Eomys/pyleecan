# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementDict import ElementDict
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_getnode2element(TestCase):
    """unittest to get elements containing specific node(s)"""

    def test_ElementDict(self):
        # Init 1
        mesh = Mesh()
        mesh.element = ElementDict()
        mesh.element.connectivity = {"Triangle": np.array([[0, 1, 2], [1, 2, 3]])}
        mesh.element.tag = {"Triangle": np.array([1, 2])}
        mesh.element.nb_elem = {"Triangle": 2}
        mesh.element.nb_node_per_element = {"Triangle": 3}
        # Method test 1
        elem_tag = mesh.element.get_node2element(1)
        # Check results
        solution = np.array([1, 2])  # Warning, elements tags, not line position !
        testA = np.sum(abs(solution - elem_tag))
        msg = (
            "Wrong projection: returned "
            + str(elem_tag)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 2
        elem_tag = mesh.element.get_node2element(3)
        solution = np.array([2])
        testA = np.sum(abs(solution - elem_tag))
        msg = (
            "Wrong projection: returned "
            + str(elem_tag)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_ElementMat(self):
        # Init 1
        mesh = Mesh()
        mesh.element = ElementMat()
        mesh.element.connectivity = np.array(
            [[11, 12, 13], [0, 1, 2], [1, 2, 3], [120, 11, 12]]
        )
        mesh.element.nb_elem = 2
        mesh.element.nb_node_per_element = 3
        # Method test 1
        elem_tag = mesh.element.get_node2element(1)
        # Check results
        solution = np.array([1, 2])  # In this case, element tag = line position
        testA = np.sum(abs(solution - elem_tag))
        msg = (
            "Wrong projection: returned "
            + str(elem_tag)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
