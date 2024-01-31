# -*- coding: utf-8 -*-

from unittest import TestCase

import numpy as np
import pytest

from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.FPGNSeg import FPGNSeg
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.RefSegmentP1 import RefSegmentP1
from pyleecan.Classes.RefTriangle3 import RefTriangle3
from pyleecan.Classes.ScalarProductL2 import ScalarProductL2


@pytest.mark.MeshSol
class unittest_ref_nodes(TestCase):
    """Tests for get_ref_point methods"""

    def test_line2(self):
        DELTA = 1e-10

        mesh = MeshMat(dimension=2)
        mesh.element_dict["line"] = ElementMat(
            nb_node_per_element=2, ref_element=RefSegmentP1(), gauss_point=FPGNSeg()
        )
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([0, 0]))
        mesh.node.add_node(np.array([1, 1]))
        mesh.node.add_node(np.array([0, 1]))
        mesh.node.add_node(np.array([2, 3]))
        mesh.node.add_node(np.array([3, 3]))

        mesh.add_element(np.array([0, 1]), "line")
        mesh.add_element(np.array([0, 2]), "line")
        mesh.add_element(np.array([1, 2]), "line")

        c_line = mesh.element_dict["line"]

        meshsol = MeshSolution()
        meshsol.mesh = mesh

        vert = mesh.get_element_coordinate(0)["line"]
        solution = np.array([0, 0])
        test = np.array([0.5, 0.5])
        ref_nodes = c_line.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_element_coordinate(1)["line"]
        solution = np.array([0, 0])
        test = np.array([0, 0.5])
        ref_nodes = c_line.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_element_coordinate(2)["line"]
        print(vert)
        solution = np.array([-0.6, 0])
        test = np.array([0.8, 1])
        ref_nodes = c_line.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_element_coordinate(2)["line"]
        solution = np.array([1, 0])
        test = np.array([0, 1])
        ref_nodes = c_line.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_triangle3(self):
        DELTA = 1e-10

        mesh = MeshMat(dimension=2)
        mesh.element_dict["triangle"] = ElementMat(
            nb_node_per_element=3, ref_element=RefTriangle3(), gauss_point=FPGNSeg()
        )
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([0, 0]))
        mesh.node.add_node(np.array([1, 0]))
        mesh.node.add_node(np.array([0, 1]))
        mesh.node.add_node(np.array([1, 1]))
        mesh.node.add_node(np.array([2, 0]))

        mesh.add_element(np.array([0, 1, 2]), "triangle")
        mesh.add_element(np.array([1, 2, 3]), "triangle")
        mesh.add_element(np.array([1, 3, 4]), "triangle")

        c_line = mesh.element_dict["triangle"]

        meshsol = MeshSolution()
        meshsol.mesh = mesh

        vert = mesh.get_element_coordinate(0)["triangle"]
        solution = np.array([0.5, 0])
        test = np.array([0.5, 0])
        ref_nodes = c_line.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_element_coordinate(1)["triangle"]
        solution = np.array([0.5, 0])
        test = np.array([0.5, 0.5])
        ref_nodes = c_line.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_element_coordinate(2)["triangle"]
        solution = np.array([0.5, 0.25])
        test = np.array([1.25, 0.5])
        ref_nodes = c_line.ref_element.get_ref_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
