# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshVTK import MeshVTK
# from pyleecan.Classes.MeshSolution import MeshSolution
from Tests import TEST_DATA_DIR
import numpy as np
from os.path import join


@pytest.mark.MeshSol
@pytest.mark.METHODS
# @pytest.mark.DEV
def test_convert_MeshVTK():
    """test convert method of MeshVTK with some vtu file"""
    mesh = MeshVTK(
        path=join(TEST_DATA_DIR, "StructElmer"), name="case_t0001", format="vtu"
    )

    meshmat = mesh.convert(meshtype="MeshMat", scale=1)

    # meshsol = MeshSolution(mesh=[meshmat])
    # meshsol.plot_mesh(is_show_fig=False)
