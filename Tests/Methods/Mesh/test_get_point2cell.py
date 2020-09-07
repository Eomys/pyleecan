# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.PointMat import PointMat
import numpy as np


@pytest.mark.MeshSol
@pytest.mark.METHODS
class Test_get_point2cell(object):
    """unittest to get cell containing specific point"""

    def setup_method(self, method):
        self.mesh = MeshMat()
        self.mesh.cell["triangle"] = CellMat(nb_pt_per_cell=3)
        self.mesh.point = PointMat()
        self.mesh.point.add_point(np.array([0, 0]))
        self.mesh.point.add_point(np.array([1, 0]))
        self.mesh.point.add_point(np.array([1, 2]))
        self.mesh.point.add_point(np.array([2, 3]))
        self.mesh.point.add_point(np.array([3, 3]))

        self.mesh.add_cell(np.array([0, 1, 2]), "triangle")
        self.mesh.add_cell(np.array([1, 2, 3]), "triangle")
        self.mesh.add_cell(np.array([4, 2, 3]), "triangle")

        self.DELTA = 1e-10

    def test_MeshMat_point(self):
        """unittest for an existing point """
        ind_elem = self.mesh.cell["triangle"].get_point2cell(1)
        solution = np.array([0, 1])
        testA = np.sum(abs(solution - ind_elem))
        msg = "Wrong output: returned " + str(ind_elem) + ", expected: " + str(solution)
        assert abs(testA-0) < self.DELTA, msg

    def test_MeshMat_fakepoint(self):
        """unittest for one non-existing point """
        ind_elem = self.mesh.cell["triangle"].get_point2cell(-99)
        solution = None
        testA = np.sum(abs(solution - ind_elem))
        msg = "Wrong output: returned " + str(ind_elem) + ", expected: " + str(solution)
        DELTA = 1e-10
        assert abs(testA-0) < DELTA, msg

        elem_tag = self.mesh.cell["triangle"].get_point2cell(None)
        testA = np.sum(abs(solution - elem_tag))
        msg = "Wrong output: returned " + str(ind_elem) + ", expected: " + str(solution)
        assert abs(testA-0) < self.DELTA, msg
