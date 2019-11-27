# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementDict import ElementDict
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_convert_element(TestCase):
    """unittest to get elements containing specific node(s)"""

    def test_ElementMat_to_ElementDict(self):
        # Init 1
        mesh1 = Mesh()
        mesh1.element = ElementDict()
        mesh1.element.connectivity = {"Triangle": np.array([[0, 1, 2], [1, 2, 3]])}
        mesh1.element.tag = {"Triangle": np.array([1, 2])}
        mesh1.element.nb_elem = {"Triangle": 2}
        mesh1.element.nb_node_per_element = {"Triangle": 3}

        mesh2 = Mesh()
        mesh2.element = ElementMat()
        mesh2.element.connectivity = np.array(
            [[0, 1, 2], [1, 2, 3]]
        )
        mesh2.element.nb_elem = 2
        mesh2.element.nb_node_per_element = 3

        mesh_new = Mesh()
        mesh_new.element = ElementDict()

        # Method test 1
        mesh_new.element.convert_element(mesh2.element)

        # Check results
        solution =np.array([[0, 1, 2], [1, 2, 3]])  # Warning, elements tags, not line position !
        testA = np.sum(abs(solution - mesh_new.element.connectivity["Triangle"]))
        msg = (
            "Wrong projection: returned "
            + str(mesh_new.element.connectivity["Triangle"])
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 2
        solution = np.array([0, 1])  # Warning, elements tags, not line position !
        testA = np.sum(abs(solution - mesh_new.element.tag["Triangle"]))
        msg = (
            "Wrong projection: returned "
            + str(mesh_new.element.connectivity["Triangle"])
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 3
        solution = 2  # Warning, elements tags, not line position !
        testA = np.sum(abs(solution - mesh_new.element.nb_elem["Triangle"]))
        msg = (
            "Wrong projection: returned "
            + str(mesh_new.element.connectivity["Triangle"])
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Method test 3
        solution = 3  # Warning, elements tags, not line position !
        testA = np.sum(abs(solution - mesh_new.element.nb_node_per_element["Triangle"]))
        msg = (
            "Wrong projection: returned "
            + str(mesh_new.element.connectivity["Triangle"])
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
