# -*- coding: utf-8 -*-

import pytest
import numpy as np
from unittest import TestCase

from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.MeshMat import MeshMat

from pyleecan.Classes.RefTriangle3 import RefTriangle3
from pyleecan.Classes.ScalarProductL2 import ScalarProductL2
from pyleecan.Classes.Interpolation import Interpolation
from pyleecan.Classes.RefSegmentP1 import RefSegmentP1
from pyleecan.Classes.FPGNSeg import FPGNSeg


@pytest.mark.MeshSol
class unittest_ref_nodes(TestCase):
    """Tests for get_ref_point methods"""

    def test_line2(self):
        DELTA = 1e-10

        mesh = MeshMat(dimension=2)
        mesh.element["line"] = ElementMat(nb_node_per_element=2)
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([0, 0]))
        mesh.node.add_node(np.array([1, 0]))
        mesh.node.add_node(np.array([0, 1]))
        mesh.node.add_node(np.array([2, 3]))
        mesh.node.add_node(np.array([3, 3]))

        mesh.add_element(np.array([0, 1]), "line")
        mesh.add_element(np.array([0, 2]), "line")
        mesh.add_element(np.array([1, 2]), "line")

        c_line = mesh.element["line"]

        c_line.interpolation = Interpolation()
        c_line.interpolation.ref_element = RefSegmentP1()
        c_line.interpolation.scalar_product = ScalarProductL2()
        c_line.interpolation.gauss_point = FPGNSeg()

        meshsol = MeshSolution()
        meshsol.mesh = [mesh]

        vert = mesh.get_vertice(0)["line"]
        solution = np.array([0, 0])
        test = np.array([0.5, 0])
        ref_nodes = c_line.interpolation.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_vertice(1)["line"]
        solution = np.array([0, 0])
        test = np.array([0, 0.5])
        ref_nodes = c_line.interpolation.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_vertice(2)["line"]
        solution = np.array([0, 0])
        test = np.array([0.5, 0.5])
        ref_nodes = c_line.interpolation.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_vertice(2)["line"]
        solution = np.array([0.8, 0])
        test = np.array([0.1, 0.9])
        ref_nodes = c_line.interpolation.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_triangle3(self):
        DELTA = 1e-10

        mesh = MeshMat(dimension=2)
        mesh.element["triangle"] = ElementMat(nb_node_per_element=3)
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([0, 0]))
        mesh.node.add_node(np.array([1, 0]))
        mesh.node.add_node(np.array([0, 1]))
        mesh.node.add_node(np.array([1, 1]))
        mesh.node.add_node(np.array([2, 0]))

        mesh.add_element(np.array([0, 1, 2]), "triangle")
        mesh.add_element(np.array([1, 2, 3]), "triangle")
        mesh.add_element(np.array([1, 3, 4]), "triangle")

        c_line = mesh.element["triangle"]

        c_line.interpolation = Interpolation()
        c_line.interpolation.ref_element = RefTriangle3()
        c_line.interpolation.scalar_product = ScalarProductL2()
        c_line.interpolation.gauss_point = FPGNSeg()

        meshsol = MeshSolution()
        meshsol.mesh = [mesh]

        vert = mesh.get_vertice(0)["triangle"]
        solution = np.array([0.5, 0])
        test = np.array([0.5, 0])
        ref_nodes = c_line.interpolation.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_vertice(1)["triangle"]
        solution = np.array([0.5, 0])
        test = np.array([0.5, 0.5])
        ref_nodes = c_line.interpolation.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_vertice(2)["triangle"]
        solution = np.array([0.5, 0.25])
        test = np.array([1.25, 0.5])
        ref_nodes = c_line.interpolation.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
