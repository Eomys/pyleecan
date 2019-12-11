# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
import numpy as np


class unittest_getnode2element(TestCase):
    """unittest to get elements containing specific node(s)"""

    def test_ElementMat(self):
        # Init 1
        mesh = Mesh()
        mesh.element["Triangle3"] = ElementMat()
        mesh.element["Triangle3"].connectivity = np.array(
            [[11, 12, 13], [0, 1, 2], [1, 2, 3], [120, 11, 12]]
        )
        mesh.element["Triangle3"].nb_elem = 4
        mesh.element["Triangle3"].nb_node_per_element = 3
        mesh.element["Triangle3"].tag = np.array([0, 1, 2, 3])
        # Method test 1
        elem_tag = mesh.element["Triangle3"].get_node2element(1)
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
