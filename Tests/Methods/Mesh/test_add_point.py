# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.PointMat import PointMat
import numpy as np


@pytest.mark.MeshSol
@pytest.mark.METHODS
class Test_add_point(object):
    """unittest for points getter methods"""

    @pytest.fixture
    def setup(self):
        mesh = MeshMat()
        mesh.point = PointMat()
        mesh.point.add_point(np.array([0, 0]))
        mesh.point.add_point(np.array([1, 0]))
        mesh.point.add_point(np.array([1, 2]))
        mesh.point.add_point(np.array([2, 3]))
        mesh.point.add_point(np.array([3, 3]))

        return mesh

    def test_add_point(self, setup):
        """unittest with CellMat and PointMat objects, only Triangle3 elements are defined"""

        assert setup.point.add_point(np.array([1, 2])) == None
