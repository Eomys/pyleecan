# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.ForceTensor import ForceTensor

from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.CellMat import CellMat

import numpy as np
import matplotlib.pyplot as plt
from Tests import save_plot_path as save_path


@pytest.mark.skip
@pytest.mark.NodeMat
@pytest.mark.MeshMat
@pytest.mark.CellMat
@pytest.mark.ForceTensor
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
    He = np.array([[[-1 / 2, 0]]])
    mue = np.array([[mu]])

    Me = np.reshape(Be / mue - He, (dim, 1, Nt_tot))

    alphaij = [[1, 0, 0], [1, 0, 0]]

    alpha1 = 1
    alpha2 = 1

    # Computation
    tensor = ForceTensor()

    f, connect = tensor.element_loop(mesh, Be, He, mue, indice, dim, Nt_tot, alphaij)

    f1_analytic = 1 / 2 * mu * np.array([alpha1 + alpha2, alpha2])
    f2_analytic = 1 / 2 * mu * np.array([-(alpha1 + alpha2), 0])
    f3_analytic = 1 / 2 * mu * np.array([0, -alpha2])

    assert (f[0, :, 0] == f1_analytic).all()
    assert (f[1, :, 0] == f2_analytic).all()
    assert (f[2, :, 0] == f3_analytic).all()

    # print("test_element_loop succeeded")

    return True


@pytest.mark.ForceTensor
def test_comp_magnetostrictive_tensor_1cell():
    """Validation of comp_magnetostrictive_tensor method from ForceTensor module by comparing with analytical solution on an elementary triangle."""

    # Physical quantities
    dim = 2
    Nt_tot = 1

    mu_0 = 4 * np.pi * 1e-7
    mu = 1
    Be = np.array([[[mu / 2, 0]]])
    He = np.array([[[-1 / 2, 0]]])
    mue = np.array([[mu]])

    Me = np.reshape(Be / mue - He, (dim, 1, Nt_tot))

    alphaij = [[1, 0, 0], [1, 0, 0]]

    alpha1 = 1
    alpha2 = 1

    # Computation
    tensor = ForceTensor()

    tensor_comp = tensor.comp_magnetostrictive_tensor(
        Me, Nt_tot, alphaij
    )  # Should be equal to -alpha1*mu*MM' - alpha2*mu*M²*I2

    assert tensor_comp[0, 0, 0] == -mu_0 * (alpha1 + alpha2)
    assert tensor_comp[0, 1, 0] == 0
    assert tensor_comp[1, 0, 0] == 0
    assert tensor_comp[1, 1, 0] == -mu_0 * alpha2

    # print("test_comp_magnetostrictive_tensor succeeded")

    return True


def test_comp_normal_to_edge():
    vec_x = []
    vec_y = []
    x_normal = []
    y_normal = []
    x_nodes = []
    y_nodes = []

    ## Mesh object
    mesh = MeshMat()
    mesh.cell["triangle3"] = CellMat(nb_node_per_cell=3)
    mesh.node = NodeMat()

    mesh.node.add_node(np.array([1, 1.22]))
    mesh.node.add_node(np.array([0.33, 0]))
    mesh.node.add_node(np.array([-1, 1]))

    nodes_test = np.array([0, 1, 2])
    mesh.add_cell(nodes_test, "triangle3")

    indice = [0]

    ## Normal comp

    dim = 2

    for key in mesh.cell:
        nb_node_per_cell = mesh.cell[
            key
        ].nb_node_per_cell  # Number of nodes per element

        mesh_cell_key = mesh.cell[key]
        connect = mesh.cell[key].get_connectivity()  # Each row of connect is an element
        nb_elem = len(connect)

        nb_node = mesh.node.nb_node  # Total nodes number

        # Loop on element (elt)
        for elt_indice, elt_number in enumerate(indice):
            node_number = mesh_cell_key.get_connectivity(
                elt_number
            )  # elt nodes numbers, can differ from indices
            vertice = mesh.get_vertice(elt_number)[key]  # elt nodes coordonates

            # Triangle orientation, needed for normal orientation. 1 if trigo oriented, -1 otherwise
            orientation_sign = np.sign(
                np.cross(vertice[1] - vertice[0], vertice[2] - vertice[0])
            )

            for n in range(nb_node_per_cell):
                edge_vector = (
                    vertice[(n + 1) % nb_node_per_cell] - vertice[n % nb_node_per_cell]
                )  # coordonées du vecteur nn+1

                L = np.linalg.norm(edge_vector)
                # Normalized normal vector n, that has to be directed outside the element (i.e. normal ^ edge same sign as the orientation)
                normal_to_edge_unoriented = (
                    np.array((edge_vector[1], -edge_vector[0])) / L
                )
                normal_to_edge = (
                    normal_to_edge_unoriented
                    * np.sign(np.cross(normal_to_edge_unoriented, edge_vector))
                    * orientation_sign
                )
                normal_to_edge.reshape(dim, 1)

                # x_normal.append(
                #     normal_to_edge[0]
                #     + (vertice[n][0] + vertice[(n + 1) % nb_node_per_cell][0]) / 2
                # )
                vec_x.append(normal_to_edge[0])
                vec_y.append(normal_to_edge[1])
                x_normal.append(
                    (vertice[n][0] + vertice[(n + 1) % nb_node_per_cell][0]) / 2
                )
                x_nodes.append(vertice[n][0])
                # y_normal.append(
                #     normal_to_edge[1]
                #     + (vertice[n][1] + vertice[(n + 1) % nb_node_per_cell][1]) / 2
                # )
                y_normal.append(
                    (vertice[n][1] + vertice[(n + 1) % nb_node_per_cell][1]) / 2
                )
                y_nodes.append(vertice[n][1])
                # print(np.linalg.norm(normal_to_edge))
                # plt.plot(edge_vector[0],edge_vector[1],'b')
                # plt.plot(normal_to_edge[0],normal_to_edge[1],'r')

    lim = 4
    plt.quiver(x_normal, y_normal, vec_x, vec_y)
    plt.plot(x_nodes, y_nodes, "ob")
    plt.plot([0], [0], "o", color="black")
    plt.axis("square")

    plt.xlim([-lim, lim])
    plt.ylim([-lim, lim])
    plt.savefig(save_path + "\\normal_edge_.png")


if __name__ == "__main__":
    test_comp_normal_to_edge()
    test_comp_magnetostrictive_tensor_1cell()
    # test_element_loop_1cell()
