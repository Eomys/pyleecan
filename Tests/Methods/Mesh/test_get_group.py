# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.PointMat import PointMat
import numpy as np

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

meshsol = MeshSolution()
meshsol.mesh = [mesh]
# self.meshsol.group = dict()
meshsol.group["stator"] = np.array([0, 1])
meshsol.group["rotor"] = np.array([2])
DELTA = 1e-10


@pytest.mark.METHODS
@pytest.mark.MeshSol
def test_MeshMat_1group():
    """unittest for 1 group"""

    MS_grp = meshsol.get_group("stator")
    cells_grp, nb_cell, indices = MS_grp.get_mesh().get_cell()
    solution = np.array([[0, 1, 2], [1, 2, 3]])
    result_tgl = cells_grp["triangle"]
    testA = np.sum(abs(solution - result_tgl))
    msg = "Wrong output: returned " + str(result_tgl) + ", expected: " + str(solution)
    assert testA == pytest.approx(0, rel=DELTA), msg

    MS_grp = meshsol.get_group("rotor")
    cells_grp, nb_cell, indices = MS_grp.get_mesh().get_cell()
    solution = np.array([[3, 3], [1, 2], [2, 3]])
    results = cells_grp["triangle"]  # The point indices have changed !
    points = MS_grp.get_mesh().get_point(results)
    testA = np.sum(abs(solution - points))
    msg = "Wrong output: returned " + str(results) + ", expected: " + str(solution)
    assert testA == pytest.approx(0, rel=DELTA), msg


if __name__ == "__main__":
    Xout = test_MeshMat_1group()
