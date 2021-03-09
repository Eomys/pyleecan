# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.ForceTensor import ForceTensor
from pyleecan.Methods.Simulation.ForceTensor import element_loop

from pyleecan.Classes.Output import Output
from pyleecan.Classes.OutMagFEMM import OutMagFEMM

from pyleecan.Functions.MeshSolution.build_solution_vector import build_solution_vector
from pyleecan.Functions.MeshSolution.build_solution_data import build_solution_data
from pyleecan.Functions.MeshSolution.build_meshsolution import build_meshsolution
from SciDataTool import Data1D

from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat

import numpy as np


@pytest.mark.skip
@pytest.mark.Force
def test_Force_Tensor_compforce():
    """Validation of compforce method from ForceTensor module by comparing with analytical solution on an elementary triangle."""

    # 'axes_dict' input
    axes_dict = {
        "Time": [0],
        "Angle": [0],
    }

    # 'output' input

    # Mesh object

    mesh = MeshMat()
    mesh.cell["triangle3"] = CellMat(nb_node_per_cell=3)
    mesh.node = NodeMat()

    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([0, 1]))
    mesh.node.add_node(np.array([1, 0]))

    nodes_test = np.array([0, 1, 2])
    mesh.add_cell(nodes_test, "triangle3")

    # Mag object
    Time = Data1D(name="time", values=[0], is_components=True)
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


def test_element_loop_1cell():
    """Validation of element_loop method from ForceTensor module by comparing with analytical solution on an elementary triangle."""

    # Mesh object
    mesh = MeshMat()
    mesh.cell["triangle3"] = CellMat(nb_node_per_cell=3)
    mesh.node = NodeMat()

    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([1, 0]))
    mesh.node.add_node(np.array([0, 1]))

    nodes_test = np.array([0, 1, 2])
    mesh.add_cell(nodes_test, "triangle3")

    indice = [0]

    # Physical quantities
    dim = 2
    Nt_tot = 1
    

    mu = 1
    Be = np.array([[[mu / 2, 0]]])
    He = np.array([[[- 1 / 2, 0]]])
    mue = np.array([[mu]])

    Me = np.reshape(Be / mue - He, (dim, 1, Nt_tot))

    alphaij = [[1,0,0],[1,0,0]]

    alpha1 = 1
    alpha2 = 1

    # Computation
    tensor = ForceTensor()

    f, connect = tensor.element_loop(mesh, Be, He, mue, indice, dim, Nt_tot,alphaij)

    f1_analytic = 1/2*mu*np.array([  alpha1 + alpha2,  alpha2]) 
    f2_analytic = 1/2*mu*np.array([  -(alpha1 + alpha2), 0 ])
    f3_analytic = 1/2*mu*np.array([ 0,  -alpha2 ])

    assert (f[0,:,0] == f1_analytic).all()
    assert (f[1,:,0] == f2_analytic).all()
    assert (f[2,:,0] == f3_analytic).all()

    print('test_element_loop succeeded')

    return True 


def test_comp_magnetostrictive_tensor_1cell():
    """Validation of comp_magnetostrictive_tensor method from ForceTensor module by comparing with analytical solution on an elementary triangle."""

    # Physical quantities
    dim = 2
    Nt_tot = 1

    mu = 1
    Be = np.array([[[mu / 2, 0]]])
    He = np.array([[[- 1 / 2, 0]]])
    mue = np.array([[mu]])

    Me = np.reshape(Be / mue - He, (dim, 1, Nt_tot))

    alphaij = [[1,0,0],[1,0,0]]

    alpha1 = 1
    alpha2 = 1
    
    # Computation
    tensor = ForceTensor()

    
    tensor_comp = tensor.comp_magnetrosctrictive_tensor(mue, Me, Nt_tot,alphaij) # Should be equal to -alpha1*mu*MM' - alpha2*mu*M²*I2

    assert tensor_comp[0,0,0] == -mu*(alpha1+alpha2)
    assert tensor_comp[0,1,0] == 0
    assert tensor_comp[1,0,0] == 0
    assert tensor_comp[1,1,0] == -mu*alpha2


    print('test_comp_magnetostrictive_tensor succeeded')

    return True 


if __name__ == "__main__":

    test_element_loop()
