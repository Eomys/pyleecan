# -*- coding: utf-8 -*-
import pytest
from unittest import TestCase
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.PointMat import PointMat
import numpy as np


@pytest.mark.MeshSol
class unittest_get_group(TestCase):
    """unittest to extract a group as a Mesh object"""

    @classmethod
    def setUp(self):

        mesh = MeshMat()
        mesh.cell["triangle"] = CellMat(nb_pt_per_cell=3)
        mesh.point = PointMat()
        mesh.point.add_point(np.array([0, 0]))
        mesh.point.add_point(np.array([1, 0]))
        mesh.point.add_point(np.array([1, 2]))
        mesh.point.add_point(np.array([2, 3]))
        mesh.point.add_point(np.array([3, 3]))

        mesh.add_cell(np.array([0, 1, 2]), "triangle")
        mesh.add_cell(np.array([1, 2, 3]), "triangle")
        mesh.add_cell(np.array([4, 2, 3]), "triangle")

        self.meshsol = MeshSolution()
        self.meshsol.mesh = [mesh]
        # self.meshsol.group = dict()
        self.meshsol.group["stator"] = np.array([0, 1])
        self.meshsol.group["rotor"] = np.array([2])
        self.DELTA = 1e-10

    def test_MeshMat_1group(self):
        """unittest for 1 group"""

        MS_grp = self.meshsol.get_group("stator")
        cells_grp, nb_cell, indices = MS_grp.get_mesh().get_cell()
        solution = np.array([[0, 1, 2], [1, 2, 3]])
        result_tgl = cells_grp["triangle"]
        testA = np.sum(abs(solution - result_tgl))
        msg = (
            "Wrong output: returned " + str(result_tgl) + ", expected: " + str(solution)
        )
        self.assertAlmostEqual(testA, 0, msg=msg, delta=self.DELTA)

        MS_grp = self.meshsol.get_group("rotor")
        cells_grp, nb_cell, indices = MS_grp.get_mesh().get_cell()
        solution = np.array([[3, 3], [1, 2], [2, 3]])
        results = cells_grp["triangle"]  # The point indices have changed !
        points = MS_grp.get_mesh().get_point(results)
        testA = np.sum(abs(solution - points))
        msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
        self.assertAlmostEqual(testA, 0, msg=msg, delta=self.DELTA)
