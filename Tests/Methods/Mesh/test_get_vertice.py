# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np


class unittest_get_vertice(TestCase):
    """unittest for Mesh and Element get_all_connectivity methods"""

    def setUp(self):
        self.mesh = Mesh()
        self.mesh.element["Quad4"] = ElementMat(nb_node_per_element=4)
        self.mesh.element["Triangle3"] = ElementMat(nb_node_per_element=3)
        self.mesh.element["Segment2"] = ElementMat(nb_node_per_element=2)
        self.mesh.node = NodeMat()
        self.mesh.node.add_node(np.array([0, 0]))
        self.mesh.node.add_node(np.array([1, 0]))
        self.mesh.node.add_node(np.array([1, 2]))
        self.mesh.node.add_node(np.array([2, 3]))
        self.mesh.node.add_node(np.array([3, 3]))

        self.mesh.add_element(np.array([0, 1, 2]), "Triangle3", group=int(3))
        self.mesh.add_element(np.array([1, 2, 3]), "Triangle3", group=int(3))
        self.mesh.add_element(np.array([4, 2, 3]), "Triangle3", group=int(2))
        self.mesh.add_element(np.array([4, 3]), "Segment2", group=int(2))

    def test_ElementMat_empty(self):
        """unittest with CellMat object. Test for empty Mesh"""

        solution = 0
        result = self.mesh.get_vertice("Quad4")[0]
        testA = result.size
        msg = (
            "Wrong output: returned "
            + str(result.size)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, solution, msg=msg, delta=DELTA)

    def test_ElementMat_seg(self):
        """unittest with CellMat object. Test for empty Mesh"""

        solution = 4
        result = self.mesh.get_vertice("Segment2")[0]
        testA = result.size
        msg = (
            "Wrong output: returned "
            + str(result.size)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, solution, msg=msg, delta=DELTA)

    def test_ElementMat_tgl(self):
        """unittest with CellMat object. Test for empty Mesh"""

        solution = 18
        result = self.mesh.get_vertice("Triangle3")[0]
        testA = result.size
        msg = (
            "Wrong output: returned "
            + str(result.size)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, solution, msg=msg, delta=DELTA)
