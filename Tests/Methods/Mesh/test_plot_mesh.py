# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.MeshSolution import MeshSolution

import numpy as np
from os.path import join

from Tests import save_plot_path as save_path

@pytest.mark.MeshSol
@pytest.mark.METHODS
# @pytest.mark.DEV
def test_plot_mesh():
    mesh = MeshMat(dimension=3)
    mesh.node = NodeMat()
    mesh.node.add_node([0, 0, 0])
    mesh.node.add_node([0, 1, 0])
    mesh.node.add_node([1, 0, 0])
    mesh.node.add_node([1, 1, 0])
    mesh.node.add_node([2, 1, 0])

    mesh.cell["triangle"] = CellMat(nb_node_per_cell=3)
    mesh.add_cell([0, 1, 2], "triangle")
    mesh.add_cell([1, 2, 3], "triangle")
    mesh.add_cell([2, 3, 4], "triangle")

    MSol = MeshSolution(mesh=[mesh])

    MSol.plot_mesh(is_show_fig=False, save_path=save_path + "/plot_mesh.png")

if __name__ == "__main__":
    test_plot_mesh()