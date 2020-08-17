# -*- coding: utf-8 -*-
import pytest
from unittest import TestCase
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
import numpy as np

@pytest.mark.MeshSol
class unittest_add_element(TestCase):
    """unittest for add_cell method in Mesh classes"""

    @classmethod
    def setUp(self):
        self.mesh = MeshMat()
        self.mesh.cell["triangle3"] = CellMat(nb_pt_per_cell=3)
        self.mesh.cell["segment2"] = CellMat(nb_pt_per_cell=2)
        self.DELTA = 1e-10

    def test_MeshMat_add_1cell(self):
        """unittest with CellMat, add 1 cell"""

        points_test = np.array([0, 1])
        self.mesh.add_cell(np.array([0, 1]), "segment2")
        # Check result
        testA = np.sum(abs(self.mesh.cell["segment2"].connectivity - points_test))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.cell["segment2"].connectivity)
            + ", expected: "
            + str(points_test)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=self.DELTA)

        msg = (
            "Wrong result: returned "
            + str(self.mesh.cell["segment2"].nb_cell)
            + ", expected: "
            + str(1)
        )
        self.assertAlmostEqual(
            self.mesh.cell["segment2"].nb_cell, 1, msg=msg, delta=self.DELTA
        )

    def test_MeshMat_add_3cell(self):
        """unittest with MeshMat, add 3 different cells"""

        points_test = np.array([0, 1])
        self.mesh.add_cell(points_test, "segment2")
        points_test = np.array([1, 2])
        self.mesh.add_cell(points_test, "segment2")
        points_test = np.array([0, 1, 2])
        self.mesh.add_cell(points_test, "triangle3")

        # Check result
        solution = np.array([[0, 1], [1, 2]])
        testA = np.sum(abs(self.mesh.cell["segment2"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.cell["segment2"].connectivity)
            + ", expected: "
            + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=self.DELTA)

        msg = (
            "Wrong result: returned "
            + str(self.mesh.cell["segment2"].nb_cell)
            + ", expected: "
            + str(2)
        )
        self.assertAlmostEqual(
            self.mesh.cell["segment2"].nb_cell, 2, msg=msg, delta=self.DELTA
        )

        solution = np.array([[0, 1, 2]])
        testA = np.sum(abs(self.mesh.cell["triangle3"].connectivity - solution))
        msg = (
            "Wrong result: returned "
            + str(self.mesh.cell["triangle3"].connectivity)
            + ", expected: "
            + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=self.DELTA)

        msg = (
            "Wrong result: returned "
            + str(self.mesh.cell["segment2"].nb_cell)
            + ", expected: "
            + str(1)
        )
        self.assertAlmostEqual(
            self.mesh.cell["triangle3"].nb_cell, 1, msg=msg, delta=self.DELTA
        )

    def test_MeshMat_add_exist(self):
        """unittest with MeshMat, try to add an already existing cell."""
        points_test = np.array([0, 1])
        self.mesh.add_cell(points_test, "segment2")
        points_test = np.array([1, 2])
        self.mesh.add_cell(points_test, "segment2")
        points_test = np.array([0, 1, 2])
        self.mesh.add_cell(points_test, "triangle3")

        points_test = np.array([1, 2])
        self.mesh.add_cell(points_test, "segment2")

        msg = (
            "Wrong result: returned "
            + str(self.mesh.cell["segment2"].nb_cell)
            + ", expected: "
            + str(2)
        )
        self.assertAlmostEqual(
            self.mesh.cell["segment2"].nb_cell, 2, msg=msg, delta=self.DELTA
        )

    def test_MeshMat_add_stupid(self):
        """unittest with CellMat and 2 segment element and 1 triangle, add 1 triangle with a group number."""

        self.mesh.add_cell(np.array([0, 1]), "segment2")
        test1 = self.mesh.add_cell(None, "segment2")
        self.assertFalse(test1)
        test2 = self.mesh.add_cell(np.array([0, 1, 2]), "segment2")
        self.assertFalse(test2)
        test3 = self.mesh.add_cell(np.array([1, 1]), "segment2")
        self.assertFalse(test2)

        solution = np.array([0, 1], dtype=int)
        result = self.mesh.cell["segment2"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
