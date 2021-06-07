# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.NodeMat import NodeMat
import numpy as np


@pytest.mark.MeshSol
class Test_get_cell_MeshMat(object):
    """unittest for Mesh get_cell methods. Indirect test add_element"""

    def setup_method(self, method):
        self.mesh = MeshMat()
        self.mesh.cell["triangle3"] = CellMat(nb_node_per_cell=3)
        self.mesh.cell["segment2"] = CellMat(nb_node_per_cell=2)
        self.mesh.add_cell([2, 1, 0], "triangle3")
        self.mesh.add_cell([1, 2, 3], "triangle3")
        self.mesh.add_cell([3, 1, 4], "triangle3")
        self.mesh.add_cell([0, 1], "segment2")

        self.mesh.node = NodeMat()
        self.mesh.node.add_node([0, 0])
        self.mesh.node.add_node([1, 0])
        self.mesh.node.add_node([0, 1])
        self.mesh.node.add_node([1, -1])
        self.mesh.node.add_node([2, -1])

    def test_MeshMat_all(self):
        """unittest MeshMat return all cells"""
        solution = dict()
        solution["triangle3"] = np.array([[2, 1, 0], [1, 2, 3], [3, 1, 4]])
        solution["segment2"] = np.array([0, 1])
        result, nb, ind = self.mesh.get_cell()

        for key in result:
            testA = np.array_equal(result[key], solution[key])
            msg = (
                "Wrong result: returned "
                + str(result[key])
                + ", expected: "
                + str(solution[key])
            )
            assert testA, msg

    def test_MeshMat_1seg2tri(self):
        """unittest MeshMat return 1 segment"""
        solution = dict()
        solution["triangle3"] = np.array(
            []
        )  # np.array([[2, 1, 0], [1, 2, 3], [3, 1, 4]])
        solution["segment2"] = np.array([0, 1])
        result, nb, ind = self.mesh.get_cell(3)

        for key in result:
            testA = np.array_equal(result[key], solution[key])
            msg = (
                "Wrong result: returned "
                + str(result[key])
                + ", expected: "
                + str(solution[key])
            )
            assert testA, msg

        solution["triangle3"] = np.array([2, 1, 0]), np.array([1, 2, 3])
        solution["segment2"] = np.array([0, 1])
        result, nb, ind = self.mesh.get_cell([0, 1, 3])

        for key in result:
            testA = np.array_equal(result[key], solution[key])
            msg = (
                "Wrong result: returned "
                + str(result[key])
                + ", expected: "
                + str(solution[key])
            )
            assert testA, msg

    def test_MeshMat_add(self):
        """unittest with MeshMat, add and get_cell for 1 cell"""
        tag_test = self.mesh.add_cell([2, 1], "segment2")
        result, nb, ind = self.mesh.get_cell(tag_test)
        solution = np.array([2, 1])
        testA = np.sum(abs(result["segment2"] - solution))
        msg = "Wrong output: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg

        tag_test = self.mesh.add_cell([4, 2, 1], "triangle3")
        result, nb, ind = self.mesh.get_cell(tag_test)
        solution = np.array([4, 2, 1])
        testA = np.sum(abs(result["triangle3"] - solution))
        msg = "Wrong output: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA - 0) < DELTA, msg

    def test_MeshMat_stupid(self):
        """unittest with MeshMat for wrong entry"""
        solution = dict()
        solution["triangle3"] = np.array([])
        solution["segment2"] = np.array([])

        result, nb_cell, indice_dict = self.mesh.get_cell(
            -99999
        )  # We test what happened with stupid entry

        # Check result
        for key in result:
            testA = np.array_equal(result[key], solution[key])
            msg = (
                "Wrong result: returned "
                + str(result[key])
                + ", expected: "
                + str(solution[key])
            )
            assert testA, msg

    def test_get_connectivity_None(self):
        """Check if get_connectivity works correctly"""
        assert self.mesh.cell["triangle3"].get_connectivity(5) == None
