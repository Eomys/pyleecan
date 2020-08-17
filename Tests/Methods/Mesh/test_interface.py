# -*- coding: utf-8 -*-

import pytest
from unittest import TestCase
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.PointMat import PointMat
from pyleecan.Classes.CellMat import CellMat
import numpy as np

@pytest.mark.MeshSol
@pytest.mark.skip
class unittest_interface(TestCase):
    """unittest for elements and nodes getter methods"""

    @classmethod
    def setUp(self):
        self.mesh = MeshMat()
        self.mesh.cell["triangle3"] = CellMat(nb_pt_per_cell=3)
        self.mesh.cell["segment2"] = CellMat(nb_pt_per_cell=2)
        self.mesh.point = PointMat()

        self.other_mesh = MeshMat()
        self.other_mesh.cell["triangle3"] = CellMat(nb_pt_per_cell=3)
        self.other_mesh.cell["segment2"] = CellMat(nb_pt_per_cell=2)
        self.other_mesh.point = self.mesh.point

    def test_MeshMat_flat(self):
        """unittest with ElementDict and PointMat objects"""

        self.mesh.add_cell([0, 1, 2], "triangle3")
        self.mesh.add_cell([2, 3, 4], "triangle3")

        self.mesh.point.add_point([0, 0])
        self.mesh.point.add_point([0.5, 1])
        self.mesh.point.add_point([1, 0])
        self.mesh.point.add_point([1.5, 1])
        self.mesh.point.add_point([2, 0])
        self.mesh.point.add_point([0.5, -1])
        self.mesh.point.add_point([1.5, -1])

        self.other_mesh.add_cell([0, 5, 2], "triangle3")
        self.other_mesh.add_cell([4, 6, 2], "triangle3")

        new_seg_mesh = self.mesh.interface(self.other_mesh)
        solution = np.array([[0, 2], [2, 4]])
        resultat = new_seg_mesh.cell["segment2"].connectivity
        testA = np.sum(abs(resultat - solution))
        msg = (
            "Wrong projection: returned "
            + str(resultat)
            + ", expected: "
            + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_CellMat_PointMat_corner_ext(self):
        """unittest with CellMat and PointMat objects, extract interface from the external mesh point of view"""
        self.mesh.add_cell([0, 1, 2], "triangle3")
        self.mesh.add_cell([1, 2, 3], "triangle3")
        self.mesh.add_cell([1, 5, 4], "triangle3")

        self.mesh.point.add_node([2, 0])
        self.mesh.point.add_node([3, 0])
        self.mesh.point.add_node([2.5, 1])
        self.mesh.point.add_node([4, 0])
        self.mesh.point.add_node([3.5, 1])
        self.mesh.point.add_node([3, -1])

        self.other_mesh.add_cell([0, 1, 5], "triangle3")

        # Method test 1
        new_seg_mesh = self.mesh.interface(self.other_mesh)

        # Check result
        solution = np.array([[0, 1], [1, 5]])
        result = new_seg_mesh.cell["Segment2"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_CellMat_PointMat_corner_int(self):
        """unittest with CellMat and PointMat objects, extract interface from the internal mesh point of view"""
        self.mesh.add_cell([0, 1, 2], "triangle3")
        self.mesh.add_cell([1, 2, 3], "triangle3")
        self.mesh.add_cell([1, 5, 4], "triangle3")

        self.mesh.point.add_node([2, 0])
        self.mesh.point.add_node([3, 0])
        self.mesh.point.add_node([2.5, 1])
        self.mesh.point.add_node([4, 0])
        self.mesh.point.add_node([3.5, 1])
        self.mesh.point.add_node([3, -1])

        self.other_mesh.add_cell([0, 1, 5], "triangle3")

        # Method test 1
        new_seg_mesh = self.other_mesh.interface(self.mesh)

        # Check result
        solution = np.array([[0, 1], [1, 5]])
        result = new_seg_mesh.cell["segment2"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)

    def test_CellMat_PointMat_self(self):
        """unittest with CellMat and PointMat objects, extract interface on itself"""
        self.mesh.add_cell([0, 1, 2], "triangle3")
        self.mesh.add_cell([0, 2, 3], "triangle3")
        self.mesh.add_cell([0, 3, 4], "triangle3")
        self.mesh.add_cell([0, 4, 1], "triangle3")

        self.mesh.point.add_point([0, 0])
        self.mesh.point.add_point([0, 1])
        self.mesh.point.add_point([1, 0])
        self.mesh.point.add_point([-1, 0])
        self.mesh.point.add_point([0, -1])

        # Method test 1
        new_seg_mesh = self.mesh.interface(self.mesh)

        # Check result
        solution = np.array([])
        result = new_seg_mesh.cell["segment2"].connectivity
        testA = np.sum(abs(result - solution))
        msg = "Wrong result: returned " + str(result) + ", expected: " + str(solution)
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
