# -*- coding: utf-8 -*-

import pytest
import numpy as np
from unittest import TestCase

from pyleecan.Classes.ElementMat import ElementMat

from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.MeshMat import MeshMat

from pyleecan.Classes.ScalarProductL2 import ScalarProductL2
from pyleecan.Classes.Interpolation import Interpolation
from pyleecan.Classes.RefSegmentP1 import RefSegmentP1
from pyleecan.Classes.FPGNSeg import FPGNSeg


@pytest.mark.MeshSol
class unittest_scalar_product(TestCase):
    """Tests for scalar_product methods"""

    def test_line_line(self):
        DELTA = 1e-10

        mesh = MeshMat()
        mesh.element["line"] = ElementMat(nb_node_per_element=2)
        mesh.node = NodeMat()
        mesh.node.add_node(np.array([-1, 0]))
        mesh.node.add_node(np.array([1, 0]))
        mesh.node.add_node(np.array([-1, 1]))
        mesh.node.add_node(np.array([2, 3]))
        mesh.node.add_node(np.array([3, 3]))

        mesh.add_element(np.array([0, 1]), "line")
        mesh.add_element(np.array([0, 2]), "line")
        mesh.add_element(np.array([1, 2]), "line")

        c_line = mesh.element["line"]

        c_line.interpolation = Interpolation()
        c_line.interpolation.ref_element = RefSegmentP1()
        c_line.interpolation.scalar_product = ScalarProductL2()
        c_line.interpolation.gauss_point = FPGNSeg(nb_gauss_point=4)

        meshsol = MeshSolution()
        meshsol.mesh = [mesh]

        # Ref element line
        vert = mesh.get_vertice(0)["line"]
        sol = [2 / 3, 1 / 3]

        [
            gauss_points,
            weights,
            nb_gauss_points,
        ] = c_line.interpolation.gauss_point.get_gauss_points()
        [
            func_ref,
            nb_func_per_element,
        ] = c_line.interpolation.ref_element.shape_function(
            gauss_points, nb_gauss_points
        )
        jacob = np.zeros((nb_gauss_points, 2, 2))
        detJ = np.zeros((nb_gauss_points))
        for ig in range(nb_gauss_points):
            [jacob[ig, :], detJ[ig]] = c_line.interpolation.ref_element.jacobian(
                gauss_points[ig, :], vert
            )

        # scal_mat_ij = < w_i , w_j >
        scal_mat = c_line.interpolation.scalar_product.scalar_product(
            func_ref, func_ref, detJ, weights, nb_gauss_points
        )

        testA = np.sum(abs(scal_mat[0, :] - sol))
        msg = (
            "Wrong result: returned " + str(scal_mat[0, :]) + ", expected: " + str(sol)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

        # Vertical element line
        vert = mesh.get_vertice(1)["line"]
        sol = [1 / 3, 1 / 6]

        [
            gauss_points,
            weights,
            nb_gauss_points,
        ] = c_line.interpolation.gauss_point.get_gauss_points()
        [
            func_ref,
            nb_func_per_element,
        ] = c_line.interpolation.ref_element.shape_function(
            gauss_points, nb_gauss_points
        )
        jacob = np.zeros((nb_gauss_points, 2, 2))
        detJ = np.zeros((nb_gauss_points))
        for ig in range(nb_gauss_points):
            [jacob[ig, :], detJ[ig]] = c_line.interpolation.ref_element.jacobian(
                gauss_points[ig, :], vert
            )

        # scal_mat_ij = < w_i , w_j >
        scal_mat = c_line.interpolation.scalar_product.scalar_product(
            func_ref, func_ref, detJ, weights, nb_gauss_points
        )

        testA = np.sum(abs(scal_mat[0, :] - sol))
        msg = (
            "Wrong result: returned " + str(scal_mat[0, :]) + ", expected: " + str(sol)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
