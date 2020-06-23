# -*- coding: utf-8 -*-

from unittest import TestCase
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.PointMat import PointMat
import numpy as np


class unittest_get_group(TestCase):
    """unittest to extract a group as a Mesh object"""

    def setUp(self):
        self.mesh = MeshMat()
        self.mesh.cell["triangle"] = CellMat(nb_pt_per_cell=3)
        self.mesh.point = PointMat()
        self.mesh.point.add_node(np.array([0, 0]))
        self.mesh.point.add_node(np.array([1, 0]))
        self.mesh.point.add_node(np.array([1, 2]))
        self.mesh.point.add_node(np.array([2, 3]))
        self.mesh.point.add_node(np.array([3, 3]))

        self.mesh.add_cell(np.array([0, 1, 2]), "triangle", group_name="stator")
        self.mesh.add_cell(np.array([1, 2, 3]), "triangle", group_name="stator")
        self.mesh.add_cell(np.array([4, 2, 3]), "triangle", group_name="rotor")

        self.DELTA = 1e-10

    def test_MeshMat_1group(self):
        """unittest for 1 group"""

        cells_grp = self.mesh.get_group("stator")
        solution = np.array([[0, 1, 2], [1, 2, 3]])
        results = cells_grp["triangle"]
        testA = np.sum(abs(solution - results))
        msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
        self.assertAlmostEqual(testA, 0, msg=msg, delta=self.DELTA)

        cells_grp = self.mesh.get_group("rotor")
        solution = np.array([4, 2, 3])
        results = cells_grp["triangle"]
        testA = np.sum(abs(solution - results))
        msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
        self.assertAlmostEqual(testA, 0, msg=msg, delta=self.DELTA)
