# -*- coding: utf-8 -*-

import numpy as np

from ....Classes.ElementMat import ElementMat
from ....Classes.MeshMat import MeshMat
from ....Classes.NodeMat import NodeMat


def get_group(self, group_names):
    """Return all attributes of a MeshSolution object with only the elements, nodes
    and corresponding solutions of the group.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    group_name : [str]
        list of the name of the group(s) (e.g. ["stator"])

    Returns
    -------
    meshsol_grp: MeshSolution
        a new MeshSolution object which is subpart of self
    """

    dimension = self.dimension

    group_indices = list()
    meshsolution_label = ""
    is_interface = False

    # 1) get the indices of all targeted element corresponding to group(s)
    sep_list = list()
    if isinstance(group_names, list):
        for grp in group_names:
            if grp == "/":
                # The groups before and after "/" are stored in different lists
                # to perform the interface.
                is_interface = True
                group_indices_init = group_indices.copy()
                group_indices = list()
                sep_list.append(group_indices_init)
            else:
                group_indices.extend(self.group[grp])
                meshsolution_label += f"{grp}_"
    elif isinstance(group_names, str):
        if group_names not in self.group:
            raise KeyError(
                group_names
                + " group doesn't exist (available groups: "
                + str(list(self.group.keys()))
                + ")"
            )
        group_indices.extend(self.group[group_names])
        meshsolution_label += group_names

    sep_list.append(np.sort(group_indices))

    # 2) extract the corresponding connectivity and create a new mesh
    mesh_init = self.mesh
    mesh_list = list()
    for sep in sep_list:
        connect_dict, nb_element, indice_dict = mesh_init.get_element(sep)

        node_indice = list()
        mesh_new = MeshMat(
            _is_renum=True, sym=mesh_init.sym, is_antiper_a=mesh_init.is_antiper_a
        )
        for key in connect_dict:
            node_indice.extend(np.unique(connect_dict[key]))
            mesh_new.element_dict[key] = ElementMat(
                connectivity=connect_dict[key],
                nb_element=len(connect_dict[key]),
                nb_node_per_element=mesh_init.element_dict[key].nb_node_per_element,
                indice=indice_dict[key],
                ref_element=mesh_init.element_dict[key].ref_element,
                gauss_point=mesh_init.element_dict[key].gauss_point,
                scalar_product=mesh_init.element_dict[key].scalar_product,
            )
        node_indice = np.unique(node_indice)

        mesh_new.node = NodeMat(init_dict=mesh_init.node.as_dict())

        mesh_list.append(mesh_new)

    # 3) if interface, create the corresponding new mesh (e.g. with triangle mesh,
    #    it creates only segment elements)
    if is_interface:
        mesh_interface = mesh_list[0].interface(mesh_list[1])
        connect_interface, *_ = mesh_interface.get_element()

        node_indice_interf = []
        for key in connect_interface:
            node_indice_interf.extend(np.unique(connect_interface[key]))

        node_indice = np.unique(node_indice_interf)

    # 4) select the corresponding solutions
    solution_dict = {}
    for key, solution in self.items():
        type_element_sol = solution.type_element

        new_sol = None
        if type_element_sol == "node":
            new_sol = solution.get_solution(indice=node_indice.tolist())
        elif not is_interface:  # Interface is only available for node solution.
            new_sol = solution.get_solution(indice=indice_dict[type_element_sol])

        if new_sol is not None:
            solution_dict[key] = new_sol

    # 5) Create the corresponding MeshSolution object
    if is_interface:
        mesh_interface.clear_node()
        mesh = mesh_interface
    else:
        mesh_new.clear_node()
        mesh = mesh_new

    meshsol_grp = self.copy()
    meshsol_grp.label = meshsolution_label
    meshsol_grp.mesh = mesh
    meshsol_grp.solution_dict = solution_dict
    meshsol_grp.dimension = dimension
    meshsol_grp.group = self.group

    return meshsol_grp
