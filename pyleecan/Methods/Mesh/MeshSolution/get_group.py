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
    the group. Solutions are converted as SolutionMat.

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
    is_interface = False

    # 1) get the indices of all targeted cell corresponding to group(s)
    sep_list = list()
    if isinstance(group_names, list):
        for grp in group_names:
            if (
                grp == "/"
            ):  # The groups before and after "/" are stored in different lists to perform the interface.
                is_interface = True
                group_indices_init = group_indices.copy()
                group_indices = list()
                sep_list.append(group_indices_init)
            else:
                group_indices.extend(self.group[grp])
                label = label + grp + "_"
    elif isinstance(group_names, str):
        group_indices.extend(self.group[group_names])
        label = label + group_names

    sep_list.append(group_indices)

    # 2) extract the corresponding connectivity and create a new mesh
    mesh_init = self.get_mesh()
    point_init = mesh_init.get_point()
    mesh_list = list()
    for sep in sep_list:
        connect_dict, nb_cell, indice_dict = mesh_init.get_cell(sep)

        node_indice = list()
        mesh_new = MeshMat()
        for key in connect_dict:
            node_indice.extend(np.unique(connect_dict[key]))
            mesh_new.cell[key] = CellMat(
                connectivity=connect_dict[key],
                nb_cell=len(connect_dict[key]),
                nb_pt_per_cell=mesh_init.cell[key].nb_pt_per_cell,
                indice=indice_dict[key],
            )
        node_indice = np.unique(node_indice)

        mesh_new.point = PointMat(init_dict=mesh_init.point.as_dict())
        mesh_new.label = label

        mesh_list.append(mesh_new)

    # 3) if interface, create the corresponding new mesh (e.g. with triangle mesh, it creates only segment cells)
    if is_interface:
        mesh_interface = mesh_list[0].interface(mesh_list[1])
        connect_interface, nb_cell_interf, indices_interf = mesh_interface.get_cell()
        node_indice_interf = list()
        for key in connect_interface:
            node_indice_interf.extend(np.unique(connect_interface[key]))

        node_indice = np.unique(node_indice_interf)

    # 4) select the corresponding solutions
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
            sol_list.append(new_sol)

        elif not is_interface:  # Interface is only available for point solution.
            if "component" in axis_dct:
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

    # 5) Create the corresponding MeshSolution object
    if is_interface:
        mesh_interface.renum()
        mesh = mesh_interface
    else:
        mesh_new.renum()
        mesh = mesh_new

    meshsol_grp = self.copy()
    meshsol_grp.label = label
    meshsol_grp.mesh = [mesh]
    meshsol_grp.is_same_mesh = is_same_mesh
    meshsol_grp.solution = sol_list
    meshsol_grp.dimension = dimension

    return meshsol_grp
