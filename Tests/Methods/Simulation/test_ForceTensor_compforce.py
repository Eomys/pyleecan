# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.ForceTensor import ForceTensor

from pyleecan.Classes.Output import Output
from pyleecan.Classes.OutMagFEMM import OutMagFEMM

from pyleecan.Functions.MeshSolution.build_solution_vector import build_solution_vector
from pyleecan.Functions.MeshSolution.build_solution_data import build_solution_data
from SciDataTool import Data1D

from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat

import numpy as np


@pytest.mark.skip
@pytest.mark.Force
def test_Force_Tensor_compforce():
    """Validation of compforce method from ForceTensor moduleby comparing with analytical solution on an elementary triangle."""

    # 'axes_dict' input
    axes_dict = {
        "Time": [0],
        "Angle": [0],
    }

    # 'output' input

    # Mesh object

    mesh = MeshMat()
    mesh.cell["triangle3"] = CellMat(nb_pt_per_cell=3)
    mesh.node = NodeMat()

    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([0, 1]))
    mesh.node.add_node(np.array([1, 0]))

    nodes_test = np.array([0, 1, 2])
    mesh.add_cell(nodes_test, "triangle3")

    # Mag object
    Time = axes_dict["Time"]
    indices_cell = [0]
    Indices_Cell = Data1D(name="indice", values=indices_cell, is_components=True)
    axis_list = [Time, Indices_Cell]

    mu = 1

    B_elem = np.array([[[mu / 2, 0]]])
    H_elem = np.array([[[1 / 2, 0]]])
    mu_elem = np.array([[mu]])

    B_sol = build_solution_vector(
        field=B_elem,
        axis_list=axis_list,
        name="Magnetic Flux Density",
        symbol="B",
        unit="T",
    )
    H_sol = build_solution_vector(
        field=H_elem,
        axis_list=axis_list,
        name="Magnetic Field",
        symbol="H",
        unit="A/m",
    )
    mu_sol = build_solution_data(
        field=mu_elem,
        axis_list=axis_list,
        name="Magnetic Permeability",
        symbol="mu",
        unit="H/m",
    )

    list_solution = [B_sol, H_sol, mu_sol]

    out_dict["meshsolution"] = build_meshsolution(
        list_solution=list_solution,
        label="FEMM 2D Magnetostatic",
        list_mesh=meshFEMM,
        group=groups,
    )


if __name__ == "__main__":

    test_Force_Tensor_compforce()
