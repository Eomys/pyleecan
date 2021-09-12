# -*- coding: utf-8 -*-

import pytest
import numpy as np
from unittest import TestCase

from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.ScalarProductL2 import ScalarProductL2
from pyleecan.Classes.Interpolation import Interpolation
from pyleecan.Classes.RefSegmentP1 import RefSegmentP1
from pyleecan.Classes.FPGNSeg import FPGNSeg


@pytest.mark.MeshSol
class unittest_real_nodes(TestCase):
    """Tests for interpolation method"""

    def test_line(self):
        DELTA = 1e-10

        mesh = MeshMat()
        mesh.cell["line"] = CellMat(nb_node_per_cell=2)
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([0, 0]))
        mesh.node.add_node(np.array([1, 0]))
        mesh.node.add_node(np.array([0, 1]))
        mesh.node.add_node(np.array([2, 3]))
        mesh.node.add_node(np.array([3, 3]))

        mesh.add_cell(np.array([0, 1]), "line")
        mesh.add_cell(np.array([0, 2]), "line")
        mesh.add_cell(np.array([1, 2]), "line")

        c_line = mesh.cell["line"]

        c_line.interpolation = Interpolation()
        c_line.interpolation.ref_cell = RefSegmentP1()
        c_line.interpolation.scalar_product = ScalarProductL2()
        c_line.interpolation.gauss_point = FPGNSeg()

        meshsol = MeshSolution()
        meshsol.mesh = [mesh]

        vert = mesh.get_vertice(0)["line"]
        test_pt = np.array([0.7, 0])
        test_field = np.array([1, 1])
        sol = [1]
        func = c_line.interpolation.ref_cell.interpolation(test_pt, vert, test_field)
        testA = np.sum(abs(func - sol))
        msg = "Wrong result: returned " + str(func) + ", expected: " + str(test_field)
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_vertice(0)["line"]
        test_pt = np.array([0.7, 0])
        test_field = np.ones(
            (2, 120, 3)
        )  # Simulate a 3D vector field for 120 time step
        func = c_line.interpolation.ref_cell.interpolation(test_pt, vert, test_field)
        sol = np.ones((120, 3))
        testA = np.sum(abs(func - sol))
        msg = "Wrong result: returned " + str(func) + ", expected: " + str(sol)
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_vertice(2)["line"]
        test_pt = np.array([0.6, 0.4])
        test_field = np.zeros((2, 120, 3))
        test_field[0, :] = np.ones(
            (1, 120, 3)
        )  # Simulate a 3D vector field for 120 time step
        func = c_line.interpolation.ref_cell.interpolation(test_pt, vert, test_field)
        sol = 0.6 * np.ones((120, 3))
        testA = np.sum(abs(sol - func))
        msg = "Wrong result: returned " + str(func) + ", expected: " + str(sol)
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        vert = mesh.get_vertice(1)["line"]
        test_pt = np.array([0, 0.4])
        test_field = np.zeros((2, 120, 3))
        test_field[1, :] = np.ones(
            (1, 120, 3)
        )  # Simulate a 3D vector field for 120 time step
        func = c_line.interpolation.ref_cell.interpolation(test_pt, vert, test_field)
        sol = 0.4 * np.ones((120, 3))
        testA = np.sum(abs(sol - func))
        msg = "Wrong result: returned " + str(func) + ", expected: " + str(sol)
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
