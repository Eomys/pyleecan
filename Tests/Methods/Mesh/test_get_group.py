# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np


class unittest_getnode2element(TestCase):
    """unittest to get elements containing specific node(s)"""

    def test_ElementMat(self):
        # Init 1
        # Init
        mesh = Mesh()
        mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([0, 0]))
        mesh.node.add_node(np.array([1, 0]))
        mesh.node.add_node(np.array([1, 2]))
        mesh.node.add_node(np.array([2, 3]))
        mesh.node.add_node(np.array([3, 3]))

        mesh.add_element(np.array([0, 1, 2]), "Triangle3", group=int(3))
        mesh.add_element(np.array([1, 2, 3]), "Triangle3", group=int(3))
        mesh.add_element(np.array([4, 2, 3]), "Triangle3", group=int(2))
        # Method test 1
        elem_grp4 = mesh.element["Triangle3"].get_group([3])
        # Check results
        solution = np.array(
            [[0, 1, 2], [1, 2, 3]]
        )  # In this case, element tag = line position
        results = elem_grp4.connectivity
        testA = np.sum(abs(solution - results))
        msg = (
            "Wrong projection: returned "
            + str(results)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
