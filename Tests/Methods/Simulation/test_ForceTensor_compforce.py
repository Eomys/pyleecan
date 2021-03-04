# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.ForceTensor import ForceTensor

from pyleecan.Classes.Output import Output
from pyleecan.Classes.OutMagFEMM import OutMagFEMM

from pyleecan.Classes.PointMat import PointMat
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat

import numpy as np




# 'axes_dict' input
axes_dict = {
    "Time": [0, 0.1, 0.2],
    "Angle": [0],
}

# 'output' input

# Mesh object

mesh = MeshMat()
mesh.cell["triangle3"] = CellMat(nb_pt_per_cell=3)
mesh.point = PointMat()

mesh.point.add_point(np.array([0, 0]))
mesh.point.add_point(np.array([0, 1]))
mesh.point.add_point(np.array([1, 0]))

points_test = np.array([0, 1, 2])
mesh.add_cell(points_test, "triangle3")




# Mag object
Time = axes_dict["Time"]
indices_cell = meshFEMM[0].cell["triangle"].indice
Indices_Cell = Data1D(name="indice", values=indices_cell, is_components=True)
axis_list = [Time, Indices_Cell]

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
    symbol="\mu",
    unit="H/m",
)

list_solution = [B_sol, H_sol, mu_sol]

out_dict["meshsolution"] = build_meshsolution(
    list_solution=list_solution,
    label="FEMM 2D Magnetostatic",
    list_mesh=meshFEMM,
    group=groups,
)
