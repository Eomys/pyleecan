# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.PointMat import PointMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.MeshSolution import MeshSolution
from Tests import TEST_DATA_DIR
import numpy as np
from os.path import join


@pytest.mark.MeshSol
@pytest.mark.METHODS
# @pytest.mark.DEV
def test_plot_mesh():
    mesh = MeshMat(dimension=3)
    mesh.point = PointMat()
    mesh.point.add_point([0, 0, 0])
    mesh.point.add_point([0, 1, 0])
    mesh.point.add_point([1, 0, 0])
    mesh.point.add_point([1, 1, 0])
    mesh.point.add_point([2, 1, 0])

    mesh.cell["triangle"] = CellMat(nb_pt_per_cell=3)
    mesh.add_cell([0, 1, 2], "triangle")
    mesh.add_cell([1, 2, 3], "triangle")
    mesh.add_cell([2, 3, 4], "triangle")

    MSol = MeshSolution(mesh=[mesh])

    MSol.plot_mesh(is_show_fig=False)
