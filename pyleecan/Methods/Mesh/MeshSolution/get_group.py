# -*- coding: utf-8 -*-

import numpy as np
import copy

from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.PointMat import PointMat
from pyleecan.Classes.SolutionMat import SolutionMat
from pyleecan.definitions import PACKAGE_NAME


def get_group(self, group_names):
    """Return all attributes of a MeshSolution object with only the cells, points and corresponding solutions of
    the group.

     Parameters
     ----------
     self : MeshSolution
         an MeshSolution object
     group_name : str
         the name of the group (e.g. "stator")

     Returns
     -------
     grp_cells: dict
         a dict sorted by cell type containing connectivity of the group

     """

    is_same_mesh = self.is_same_mesh
    dimension = self.dimension

    group_indices = list()
    label = ""

    if isinstance(group_names, list):
        for grp in group_names:
            group_indices.extend(self.group[grp])
            label = label + grp + "_"
    elif isinstance(group_names, str):
        group_indices.extend(self.group[group_names])
        label = label + group_names

    mesh_init = self.get_mesh()
    point_init = mesh_init.get_point()

    connect_dict, nb_cell, indice_dict = mesh_init.get_cell(group_indices)

    node_indice = list()
    for key in connect_dict:
        node_indice.extend(np.unique(connect_dict[key]))

    node_indice = np.unique(node_indice)

    nb_node_new = len(node_indice)
    node_indice_new = np.linspace(0, nb_node_new - 1, nb_node_new, dtype=int)

    connect_dict_new = copy.deepcopy(connect_dict)
    for inode in range(nb_node_new):
        for key in connect_dict:
            connect_dict_new[key][
                connect_dict[key] == node_indice[inode]
            ] = node_indice_new[inode]

    mesh = MeshMat()
    mesh.point = PointMat(
        coordinate=point_init[node_indice, :], nb_pt=nb_node_new, indice=node_indice_new
    )
    for key in connect_dict:
        mesh.cell[key] = CellMat(
            connectivity=connect_dict_new[key],
            nb_cell=len(connect_dict_new[key]),
            nb_pt_per_cell=mesh_init.cell[key].nb_pt_per_cell,
            indice=indice_dict[key],
        )

    mesh.label = label

    sol_list = list()

    for sol in self.solution:

        label_sol = sol.label
        type_cell_sol = sol.type_cell
        field_sol = sol.get_field()
        axis_dct = sol.get_axis()

        if type_cell_sol == "point":
            new_field_sol = field_sol[:, node_indice, :]
            new_sol = SolutionMat(
                label=label_sol,
                type_cell=type_cell_sol,
                field=new_field_sol,
                indice=node_indice,
            )
        else:
            if "direction" in axis_dct:
                new_field_sol = field_sol[:, indice_dict[type_cell_sol], :]
            else:
                new_field_sol = field_sol[:, indice_dict[type_cell_sol]]
            new_sol = SolutionMat(
                label=label_sol,
                type_cell=type_cell_sol,
                field=new_field_sol,
                indice=indice_dict[type_cell_sol],
            )

        sol_list.append(new_sol)

    meshsol_grp = self.copy()
    meshsol_grp.label = label
    meshsol_grp.mesh = [mesh]
    meshsol_grp.is_same_mesh = is_same_mesh
    meshsol_grp.solution = sol_list
    meshsol_grp.dimension = dimension

    return meshsol_grp
