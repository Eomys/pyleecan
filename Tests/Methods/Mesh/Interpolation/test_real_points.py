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


@pytest.mark.MeshSol
class unittest_real_nodes(TestCase):
    """Tests for get_real_point methods"""

    def test_line(self):
        DELTA = 1e-10

        mesh = MeshMat()
        mesh.element_dict["line"] = ElementMat(
            nb_node_per_element=2, ref_element=RefSegmentP1(), gauss_point=FPGNSeg()
        )
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([0, 0]))
        mesh.node.add_node(np.array([1, 0]))
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
        test = np.array([0, 0])
        solution = np.array([0.5, 0])
        ref_nodes = c_line.ref_element.get_real_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_element_coordinate(1)["line"]
        test = np.array([0, 0])
        solution = np.array([0, 0.5])
        ref_nodes = c_line.ref_element.get_real_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_element_coordinate(2)["line"]
        test = np.array([0, 0])
        solution = np.array([0.5, 0.5])
        ref_nodes = c_line.ref_element.get_real_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_element_coordinate(2)["line"]
        test = np.array([-1, 0])
        solution = np.array([1, 0])
        ref_nodes = c_line.ref_element.get_real_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_element_coordinate(2)["line"]
        test = np.array([-0.2, 0])
        solution = np.array([0.6, 0.4])
        ref_nodes = c_line.ref_element.get_real_point(vert, test)
        testA = np.sum(abs(solution - ref_nodes))
        msg = (
            "Wrong result: returned " + str(ref_nodes) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
